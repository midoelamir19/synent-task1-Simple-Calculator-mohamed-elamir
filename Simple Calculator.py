def Simple_Calculator(op_sample,x,y):
    if op_sample=='+':
        return x+y
    elif op_sample=='-':
        return x-y
    elif op_sample=='/':
        if y==0:
            print("don't allow divided by zero")
            return 0
        else:
            return x/y
    elif op_sample=='*':
        return x*y

def main():
    work="y"
    while work=="y":
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
        operation = input("Enter operation (+,-,*,/) : ")
        result=Simple_Calculator(operation, num1, num2)
        print("Result =",result)
        work=input("Do you want continue ?(y/n): ")



if __name__ == '__main__':
    main()
