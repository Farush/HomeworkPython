# Zaranee proshu prosheniya za krov iz glaz ot translita. Sgorela klava s kirillicey. Kupil tureckuyu.
# Potom nadpishu na ney kirillicheskiye simvoly.I'll try to write in english where my knowledge of it is enough.


# 1. Реализовать класс Matrix (матрица).

class Matrix:
    def __init__(self, matrix_lines):
        self.matrix = matrix_lines
        self.columns = len(self.matrix[0])
        self.lines = len(self.matrix)
        for line in self.matrix:
            if len(line) != self.columns:
                raise Exception ('All the lines in Matrix should have the same length') # the better way is to
                # find the longest line and add zeros to the shorter ones
        self.dimension = [self.lines, self.columns] # needed to make matrices' dimensions comparable
        #print(self.matrix[0][0])

    def __add__(self, other):
        new_matrix = []
        new_line = []
        if self.dimension != other.dimension: # We refuse to add matrices with different dimensions.
            # The better way is to fill missing lines and columns with zeros which demands writing a more complex
            # code
            raise ArithmeticError('Matrices have different dimensions')
        else:
            for line in range(len(self.matrix)):
                for column in range(len(self.matrix[0])):
                    new_line.append(self.matrix[line][column] + other.matrix[line][column])
                new_matrix.append(new_line)
                new_line = []

            return Matrix(new_matrix)

    def __str__(self):
        matrix_square = ''
        for line in range(len(self.matrix)):
            for column in range(len(self.matrix[0])):
                matrix_square = matrix_square + f'|  {self.matrix[line][column]}  '
            matrix_square = matrix_square + '|\n'
        return matrix_square

    def __mul__(self, multiplier): # just because I can
        new_matrix = []
        new_line = []
        for line in range(len(self.matrix)):
            for column in range(len(self.matrix[0])):
                new_line.append(self.matrix[line][column] * multiplier)
            new_matrix.append(new_line)
            new_line = []

        return Matrix(new_matrix)


matr1 = Matrix([[1, 2, 3], [2, 5, 8], [65, 67894, 0]])

matr2 = Matrix([[2, 5, 9], [789, -17, -36], [0, 0, 56]])

matr3 = matr1 + matr2

matr4 = matr1 + matr2 + matr3 + matr1

matr5 = matr1 * 1

print(matr5 * 15.7)

print(type(matr3))

print(matr3)
print(matr4)



# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def consumption(self):
        pass

class Suit(Clothes):

    def __init__(self, height):
        self.__h = height

    def consumption(self):
        return self.__h*2 + 0.3

    @property
    def height(self):
        return self.__h

    @height.setter
    def height(self, height):
        if height < 1:
            self.__h = 1
        elif height > 2.5:
            self.__h = 2.5
        else:
            self.__h = height

class Coat(Clothes):

    def __init__(self, size):
        self.__s = size

    def consumption(self):
        return self.__s*2 / 6.5 + 0.3

    @property
    def size(self):
        return self.__s

    @size.setter
    def size(self, size):
        if size < 10:
            self.__s = 10
        elif size > 70:
            self.__s = 70
        else:
            self.__s = size

suit1 = Suit(3)
print(suit1.consumption())

suit1.height = 3
print(suit1.consumption())

coat1 = Coat(100)
print(coat1.consumption())

coat1.size = 100
print(coat1.consumption())

coat1.size = 1
print(coat1.consumption())


# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.

class Cell:
    def __init__(self, elements):
        if type(elements) is int:
            self.elements = elements
        else:
            raise 'Argument must be an integer'



    def __add__(self, other):
        return Cell(self.elements + other.elements)

    def __sub__(self, other):
        if self.elements < other.elements:
            raise 'Cannot subtract bigger Cell from smaller Cell'
        else:
            return Cell(self.elements - other.elements)

    def __mul__(self, other):
        return Cell(self.elements * other.elements)

    def __truediv__(self, other):
        return Cell(self.elements // other.elements)

    def make_order(self, row):
        rows = ''
        if row > self.elements:
            raise 'Number of elements in the Cell is out of range'
        else:
            i = 0
            n = self.elements // row
            r = self.elements % row
            while i < n:
                rows = rows + row * '*' + '\n'
                i += 1
            rows = rows + r * '*' + '\n' if r != 0 else rows

            return rows









cell1 = Cell(13)

cell2 = Cell(25)

#a = cell1 - cell2
b = cell2 - cell1
c = cell2 * cell1
d = cell1 / cell2
e = cell2 / cell1
print(b.make_order(2))
print((c - cell2).make_order(70), b.make_order(2)) # adds extra space in the beginning of the second Cell,
# don't understand why. can't get rid of this
print(cell1.make_order(5))
