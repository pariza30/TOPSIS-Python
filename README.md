# TOPSIS Implementation in Python

This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method as a command-line Python program.

## PyPI Package
https://pypi.org/project/topsis-pariza-102303391/

##  Web Service (Frontend)

The web-based TOPSIS service frontend is deployed using **GitHub Pages**.

🔗 **Live Web Interface:**  
https://pariza30.github.io/TOPSIS-Python/

> Note: This frontend connects to a backend that runs locally or on a cloud server.


## ⚙️ Backend (Flask API – Local Run)

### 1️⃣ Install dependencies
```bash
pip install flask flask-cors pandas numpy


## Requirements
- Python 3
- pandas
- numpy

## How to Run
```bash
python topsis.py <inputFile> <weights> <impacts> <outputFile>

EXAMPLE:
python topsis.py Topsis-Dataset.csv "1,1,1,1" "+,-,-,+" output.csv

Input Format:
1) CSV file
2) First column: alternative names
3) Remaining columns: numeric criteria values

Output:
1) Original data
2) TOPSIS Score
3) Rank




