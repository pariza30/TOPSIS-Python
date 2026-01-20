from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from topsis_logic import run_topsis
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)


def send_email_with_attachment(receiver_email, file_path):
    EMAIL_ADDRESS = "pkandol_be23@thapar.edu"
    EMAIL_PASSWORD = "bjlzbtehcqoudbkl"   # ✅ NO SPACES

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result – Analysis Completed"
    msg["From"] = f"TOPSIS Web Service <{EMAIL_ADDRESS}>"
    msg["To"] = receiver_email

    msg.set_content(
        "Hello,\n\n"
        "Your TOPSIS analysis has been successfully completed.\n\n"
        "Please find the attached CSV file containing:\n"
        "- TOPSIS Score\n"
        "- Rank of each alternative\n\n"
        "Regards,\n"
        "TOPSIS Web Service Team"
    )

    with open(file_path, "rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="csv",
        filename="topsis_result.csv"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


@app.route("/topsis", methods=["POST"])
def topsis_api():

    print("TOPSIS API HIT")

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    weights = request.form.get("weights")
    impacts = request.form.get("impacts")
    email = request.form.get("email")

    print("Email received from form:", email)

    if not file.filename.endswith(".csv"):
        return jsonify({"error": "Only CSV files allowed"}), 400

    input_path = "input.csv"
    output_path = "result.csv"
    file.save(input_path)

    df = run_topsis(input_path, weights, impacts, output_path)

    if email:
        try:
            print("Trying to send email...")
            send_email_with_attachment(email, output_path)
            print("Email send SUCCESS")
        except Exception as e:
            print("Email send FAILED:", e)

    return jsonify({
        "data": df.to_dict(orient="records")
    })


@app.route("/download")
def download():
    return send_file("result.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
