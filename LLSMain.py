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

        # DL/Da parameters
        dl_da_x2 = 0
        dl_da_x = 0
        dl_da_1 = 0
        dl_da_y = 0

        # DL/Db parameters
        dl_db_x2 = 0
        dl_db_x = 0
        dl_db_1 = 0
        dl_db_y = 0

        # DL/Dc parameters
        dl_dc_x2 = 0
        dl_dc_x = 0
        dl_dc_1 = 0
        dl_dc_y = 0

        # Calculating all variables
        for i in range(len(self.x_values)):

            # Calculating all DL/Da variables
            dl_da_x2 += -2 * (self.x_values[i] ** 4)
            dl_da_x += -2 * (self.x_values[i] ** 3)
            dl_da_1 += -2 * (self.x_values[i] ** 2)
            dl_da_y += -2 * (self.x_values[i] ** 2) * self.y_values[i]

            # Calculating all DL/Db variables
            dl_db_x2 += -2 * (self.x_values[i] ** 3)
            dl_db_x += -2 * (self.x_values[i] ** 2)
            dl_db_1 += -2 * (self.x_values[i])
            dl_db_y += -2 * (self.x_values[i]) * self.y_values[i]

            # Calculating all DL/Dc variables
            dl_dc_x2 += -2 * (self.x_values[i] ** 2)
            dl_dc_x += -2 * (self.x_values[i])
            dl_dc_1 += -2
            dl_dc_y += -2 * self.y_values[i]

        # Creating the matrices
        x_matrix = np.array([[dl_da_x2, dl_da_x, dl_da_1], [dl_db_x2, dl_db_x, dl_db_1], [dl_dc_x2, dl_dc_x, dl_dc_1]])
        y_matrix = np.array([[dl_da_y], [dl_db_y], [dl_dc_y]])

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