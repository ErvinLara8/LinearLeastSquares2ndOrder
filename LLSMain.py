import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv

import sys


class LLS:
    def __init__(self):
        # Initiating Data
        self.x_values = [1, 2, 3, 4, 5, 6]
        self.y_values = [3.2, 6.4, 10.5, 17.7, 28.1, 38.5]

    def run(self):

        # Checking data format
        if len(self.x_values) != len(self.y_values) or len(self.x_values) == 0 and len(self.y_values) == 0:
            print("Error data not formatted correctly. No values or un-even number if values for x and y")
            sys.exit(0)

        # Plotting the points
        plt.scatter(self.x_values, self.y_values)

        # Da/Dl parameters
        da_dl_x2 = 0
        da_dl_x = 0
        da_dl_1 = 0
        da_dl_y = 0

        # Db/Dl parameters
        db_dl_x2 = 0
        db_dl_x = 0
        db_dl_1 = 0
        db_dl_y = 0

        # Dc/Dl parameters
        dc_dl_x2 = 0
        dc_dl_x = 0
        dc_dl_1 = 0
        dc_dl_y = 0

        # Calculating all variables
        for i in range(len(self.x_values)):

            # Calculating all Da/DL variables
            da_dl_x2 += -2 * (self.x_values[i] ** 4)
            da_dl_x += -2 * (self.x_values[i] ** 3)
            da_dl_1 += -2 * (self.x_values[i] ** 2)
            da_dl_y += -2 * (self.x_values[i] ** 2) * self.y_values[i]

            # Calculating all Db/DL variables
            db_dl_x2 += -2 * (self.x_values[i] ** 3)
            db_dl_x += -2 * (self.x_values[i] ** 2)
            db_dl_1 += -2 * (self.x_values[i])
            db_dl_y += -2 * (self.x_values[i]) * self.y_values[i]

            # Calculating all Dc/DL variables
            dc_dl_x2 += -2 * (self.x_values[i] ** 2)
            dc_dl_x += -2 * (self.x_values[i])
            dc_dl_1 += -2 * 1
            dc_dl_y += -2 * 1 * self.y_values[i]

        # Creating the matrices
        x_matrix = np.array([[da_dl_x2, da_dl_x, da_dl_1], [db_dl_x2, db_dl_x, db_dl_1], [dc_dl_x2, dc_dl_x, dc_dl_1]])
        y_matrix = np.array([[da_dl_y], [db_dl_y], [dc_dl_y]])

        # Getting the unknowns
        abc_matrix = np.dot(inv(x_matrix), y_matrix)

        # Printing Matrices information
        print("X Matrix:")
        print(x_matrix)
        print("Y Matrix:")
        print(y_matrix)
        print("Unknowns A,B,C:")
        print(abc_matrix)

        # getting solution line
        y_solutions = []
        for x in self.x_values:
            formula_y = abc_matrix[0] * (x**2) + abc_matrix[1] * x + abc_matrix[2]
            y_solutions.append(formula_y)

        # Plotting Solution Line
        plt.plot(self.x_values, y_solutions)
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.title('Linear Least Squares Second Order Derivation')
        plt.show()


if __name__ == "__main__":
    lls = LLS()
    lls.run()