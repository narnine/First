import random
def way(size, choose):
    if choose == 1:
        a = []
        b = []
        for i in range(size):
            for j in range(size):
                x = random.randint(0, 10)
                b.append(x)
            a.append(b)
            b = []
        return a
    else:
        a = []
        b = []
        for i in range(size):
            for j in range(size):
                x = int(input())
                b.append(x)
            a.append(b)
            b = []
        return a


class SquareMatrix:
    __matrix_count = 0
    def __init__(self, size, choose):
        self.__size = size
        self.choose = choose
        self.matrix = way(size, choose)
        SquareMatrix.__matrix_count += 1

    @property
    def matrix_count(self):
        return self.__matrix_count

    @matrix_count.setter
    def matrix_count(self, value):
        raise ValueError("Matrix count doesn't be change")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        raise ValueError("Matrix count doesn't be change")


    def get(self):
        print("Размер матрицы:")
        return self.__size
        print("Кол-во матриц:")
        return self.__matrix_count


    def __str__(self):
        s = "Матрица:\n"
        for i in range(self.size):
            for j in range(self.size):
                s += str(self.matrix[i][j]) + " "
            s += "\n"
        return s


    def _import(self):
        b = int()
        for i in range(self.size):
            b = self.matrix[i][i] + b
        print("Cумма элементов главной диагонали:")
        return b


    def transposition(self):
        new_s = [[0 for i in range(self.size)] for j in range(self.size)]
        print("Транспонирование:")
        for i in range(self.size):
            for j in range(self.size):
                new_s[i][j] = self.matrix[j][i]
                print(new_s[i][j], end=" ")
            print()


    def __lt__(self, other):
        if self.matrix < other.matrix:
            return True
        else:
            return False


    def __eq__(self, other):
        if self.matrix == other.matrix:
            return True
        else:
            return False


    def __gt__(self, other):
        if self.matrix > other.matrix:
            return True
        else:
            return False


def __add__(self, other):
    print("Сложение")
    if self.size == other.size:
        sum = [[self.matrix[i][j] + other.matrix[i][j] for i in range(self.size)] for j in range(self.size)]
        return sum
    else:
        print("Сложение не возможно!")

# Первая матрица
a = SquareMatrix(5, 1)

# Вторая матрица
b = SquareMatrix(5, 1)

# Третья матрица
c = SquareMatrix(4, 1)

# Четвтертая матрица
d = SquareMatrix(4, 1)

# Пятая матрица
e = SquareMatrix(9, 1)

# Транспартировка 2 матриц размером 4
print(c.__str__())
print (c.transposition())

print(d.__str__())
print(d.transposition())

# Сумма диагональ
sum_diagonal = 0
print("Сумма диагональ:")
print(b._import()+ a._import())

# Cложение матриц с размером 5
print( __add__(a, b))

# Сравнение матриц размером произвольного и 4
if c.__size > d.__size and c.__size > e.__size:
    print("3 матрица имеет наибольший вес")
elif d.__size > c.__size and d.__size > e.__size:
    print("4 матрица имеет наибольший вес")
else:
    print("5 матрица имеет наибольший вес")