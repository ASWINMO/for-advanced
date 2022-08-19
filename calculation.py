num1=int(input("enter a number"))
num2=int(input("enter the number"))
operator=input("enter the operator (+,-,*,/,%)select 1,2,3,4,5")
result=0
def add(num1,num2):
    return num1+num2
if operator=="1":
    result=add(num1,num2)
    print(result)
def sub(num1,num2) :
    return num1-num2
if operator=="2":
    result=sub(num1,num2)
    print(result)
def mul(num1,num2):
    return num1*num2
if operator=="3":
        result=mul(num1,num2)
        print(result)
def div(num1,num2):
            return num1/num2
if operator=="4":
    result=div(num1,num2)
    print(result)
def mod(num1,num2):
    return num1%num2
if operator=="5":
    result=mod(num1,num2)
    print(result)