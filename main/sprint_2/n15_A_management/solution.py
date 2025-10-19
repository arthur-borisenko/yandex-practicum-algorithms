import time
from copy import deepcopy


class MatrixError(Exception):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    @staticmethod
    def _parse_matrix_str(matrix_str):
        matrix = []
        for line in matrix_str.strip().split("\n"):
            matrix.append(line.split())
        return matrix

    def __init__(self, matrix):
        if isinstance(matrix, str):
            self.matrix = self._parse_matrix_str(matrix)
        else:
            self.matrix = deepcopy(matrix)

    def __str__(self):
        """
        CPU - O(n)
        RAM - O(n)
        n - matrix size
        :return: string representation of matrix
        """
        res = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res += str(self.matrix[i][j])
                if j != len(self.matrix[i]) - 1:
                    res += " "
            if i != len(self.matrix) - 1:
                res += "\n"
        return res

    @staticmethod
    def transposed(obj):
        """
        CPU - O(n)
        RAM - O(n)
        n - matrix size
        :param obj:
        :return: transposed copy of matrix
        """
        new_matrix = []
        for i in range(obj.size()[1]):
            new_matrix.append([])
            for j in range(obj.size()[0]):
                new_matrix[i].append(None)
                new_matrix[i][j] = obj.matrix[j][i]
        return Matrix(new_matrix)

    def transpose(self):
        """
        transpose current matrix
        CPU - O(n)
        RAM - O(n)
        n - matrix size
        :return:
        """
        new_matrix = self.transposed(self)
        self.matrix = new_matrix.matrix
        return new_matrix

    def size(self):
        """
        CPU - O(1)
        RAM - O(1)
        :return: [matrix y size, matrix x size]
        """
        return len(self.matrix), len(self.matrix[0])


def main():
    """
    CPU - O(n)
    RAM - O(n)
    n - input matrix size
    """
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        i, j = inp.readline(), inp.readline()
        matrix_str = inp.read()
        matrix = Matrix(matrix_str)
        matrix.transpose()
        print(matrix, file=outp)


if __name__ == "__main__":
    main()
