class bank:
    def getratio(self):
        return 10

    def __init__(self):
        self.__Ratio()

    def __Ratio(self):
        print('The raio of banks')


class SBI(bank):
    def getratio(self):
        return 9


class Axis(bank):
    def getratio(self):
        return 7


B = bank()
print(B.getratio())

S = SBI()
print(S.getratio())

A = Axis()
print(A.getratio())
