class addition():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def show(self):
        print(f"Addition of {self.num1} & {self.num2} is :- ",self.num1+self.num2)


num1 = int(input("Enter the first value : "))
num2 = int(input("Enter the second value : "))

obj = addition(num1,num2)
obj.show()

