class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        if num and not nums:
            self.result += num
            return self
        else:
            for n in nums:
                self.result += n
            self.result += num
        return self 

    def subtract(self, num, *nums):
        if num and not nums:
            self.result -= num
        else:
            for n2 in nums:
                self.result -= n2
            self.result -= num
        return self
            





md = MathDojo()
abc = MathDojo()
hij = MathDojo()

x = md.add(2, 3, 5).subtract(3)
y = abc.add(5, 5).subtract(5).add(5).subtract(5, 1)
z = hij.subtract(5, 10).add(15, 5, 20, 30, 10)


print(x.result)
print(y.result)
print(z.result)
