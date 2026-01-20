import pandas as pd
import numpy as np

def run_topsis(input_file, weights, impacts, output_file):
    data = pd.read_csv(input_file)

    names = data.iloc[:, 0]
    matrix = data.iloc[:, 1:]

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    # Normalize
    norm = matrix / np.sqrt((matrix ** 2).sum())

    # Weighted normalized matrix
    weighted = norm * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    result = data.copy()
    result["Topsis Score"] = score
    result["Rank"] = score.rank(ascending=False)

    result.to_csv(output_file, index=False)

    return result
