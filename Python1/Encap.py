class prof:
    __name = 'python'
    age = 28

    def __init__(self):
        print(self.__name)

    def disp1(self, fname):
        self.__name = fname
        print(self.__name, self.age)


p = prof()
p.disp1('Pyt')
