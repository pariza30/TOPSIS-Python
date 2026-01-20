const checkbox = document.getElementById("sendEmailCheckbox");
const emailBox = document.getElementById("emailBox");

checkbox.addEventListener("change", () => {
    emailBox.style.display = checkbox.checked ? "block" : "none";
});

document.getElementById("topsisForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const resultDiv = document.getElementById("result");
    resultDiv.innerText = "⏳ Processing...";

    const formData = new FormData(this);

    try {
        const response = await fetch("http://127.0.0.1:5000/topsis", {
            method: "POST",
            body: formData
        });

        const result = await response.json();
        resultDiv.innerText = "✅ TOPSIS calculated successfully";

        renderTable(result.data);

    } catch (err) {
        console.error(err);
        resultDiv.innerText = "❌ Error connecting to backend";
    }
});

function renderTable(data) {
    const section = document.getElementById("results-section");
    const table = document.getElementById("results-table");

    table.innerHTML = "";

    const headers = Object.keys(data[0]);
    let headerRow = "<tr>";
    headers.forEach(h => headerRow += `<th>${h}</th>`);
    headerRow += "</tr>";
    table.innerHTML += headerRow;

    data.forEach(row => {
        let tr = "<tr>";
        headers.forEach(h => tr += `<td>${row[h]}</td>`);
        tr += "</tr>";
        table.innerHTML += tr;
    });

    section.style.display = "block";
}

function downloadCSV() {
    window.location.href = "http://127.0.0.1:5000/download";
}
