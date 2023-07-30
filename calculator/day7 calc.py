#calculator
# task 1
print(("calculator starts").upper())

a=float(input("enter num 1: "))
b=float(input("enter num 2: "))
operation = input('''
Please type in the math operation you would like to complete: 
just type math operations only''')


if operation=="+":
    print(a ,"+" ,b,"=", a+b) 
elif operation=="-":
    print(a,"-",b,"=", a-b) 
elif operation=="*":
    print(a,"*",b,"=", a*b) 
elif operation=="/":
    print(a,"/",b,"=", a/b) 
elif operation=="//":
    print(a,"//",b,"=", a//b) 
elif operation=="%":
    print(a,"%",b,"=", a%b) 
elif operation=="**":
    print(a,"**" , b ,"=", a**b)
else:
    print('error')

