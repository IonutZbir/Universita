from typing import *
import numpy as np
from numpy.typing import NDArray
import pandas as pd
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, n_iter: int = 10, eta: float = 0.01):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, x: np.ndarray, y: np.ndarray):
        self.w = np.zeros(1 + x.shape[1])  # Inizializza i pesi a zero
        self.errors = []
        for _ in range(self.n_iter):
            err = 0
            for (xi, yi) in zip(x, y):
                update_cond = yi * (np.dot(self.w[1:], xi) + self.w[0])
                if update_cond <= 0:
                    self.w[1:] += self.eta * yi * xi
                    self.w[0] += self.eta * yi
                    err += int(update_cond)
                self.errors.append(err)
            if err == 0:
                break

    def plot_decision_line(self, x):
        # Estrai i valori minimi e massimi per la prima feature (Sepal Length)
        x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
        x_values = np.arange(x_min, x_max, 0.02)

        # Calcola i valori di y (Petal Length) per la decision boundary
        # Calcola i valori della retta: y = (-w_0 - w_1 * x) / w_2
        y_values = (-self.w[0] - self.w[1] * x_values) / self.w[2]

        # Plotta i punti del dataset
        plt.scatter(x[:50, 0], x[:50, 1], color="red", marker="o", label="setosa")
        plt.scatter(x[50:100, 0], x[50:100, 1], color="blue", marker="x", label="versicolor")

        # Plotta la retta di decisione
        plt.plot(x_values, y_values, color="yellow", linewidth=2, label="Decision Boundary")

        # Etichette e legenda
        plt.xlabel("Sepal Length")
        plt.ylabel("Petal Length")
        plt.legend(loc="upper left")
        plt.show()

if __name__ == "__main__":
    df = pd.read_csv("Iris.csv")

    y = df.iloc[0:100, 5]
    y = np.where(y == "Iris-setosa", -1, 1)

    x = df.iloc[0:100, [1, 3]].values

    ppn = Perceptron(eta=0.2, n_iter=10)
    ppn.fit(x, y)

    ppn.plot_decision_line(x)


