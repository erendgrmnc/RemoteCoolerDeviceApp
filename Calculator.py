class Calculator:
    def __init__(self, x, y):
        self.firstNumb = x
        self.secondNumb = y

    def Add(self):
        result = self.firstNumb + self.secondNumb
        return result

    def Extract(self):
        result = self.firstNumb - self.secondNumb
        return result

    def Multiply(self):
        result = self.firstNumb * self.secondNumb
        return result
