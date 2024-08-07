import time
from copy import deepcopy


class MatrixError(Exception):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def _parse_string(self, string):
        matrix = []
        for line in string.strip().split("\n"):
            matrix.append(line.split())
        return matrix

    def __init__(self, matrix):
        if isinstance(matrix, str):
            self.matrix = self._parse_string(matrix)
        else:
            self.matrix = deepcopy(matrix)

    def __str__(self):
        res = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res += str(self.matrix[i][j])
                if j != len(self.matrix[i]) - 1:
                    res += " "
            if i != len(self.matrix) - 1:
                res += "\n"
        return res

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixError(self, other)
        else:
            res = Matrix(self.matrix)
            for i in range(len(res.matrix)):
                for j in range(len(res.matrix[i])):
                    res.matrix[i][j] += other.matrix[i][j]
            return res

    @staticmethod
    def transposed(obj):
        new_matrix = []
        for i in range(obj.size()[1]):
            new_matrix.append([])
            for j in range(obj.size()[0]):
                new_matrix[i].append(None)
                new_matrix[i][j] = obj.matrix[j][i]
        return Matrix(new_matrix)

    def transpose(self):
        new_matrix = self.transposed(self)
        self.matrix = new_matrix.matrix
        return new_matrix

    def __mul__(self, other):
        res = Matrix(self.matrix)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[i])):
                res.matrix[i][j] *= other
        return res

    __rmul__ = __mul__

    def size(self):
        return len(self.matrix), len(self.matrix[0])


def main():
    with open("input.txt") as inp, open("output.txt", "w") as outp:
        i, j = inp.readline(), inp.readline()
        matrix_str = inp.read()
        matrix = Matrix(matrix_str)
        matrix.transpose()
        print(matrix, file=outp)


if __name__ == "__main__":
    main()
