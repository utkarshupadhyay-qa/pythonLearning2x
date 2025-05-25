class Calc:
    def sum(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


x = Calc()      # Object Reference = Object()

result = x.sum(3, 4)
print(result)

result1 = x.subtract(7, 4)
print(result1)

result2 = x.multiply(4,5)
print(result2)

result3 = x.div(20,10)
print(result3)