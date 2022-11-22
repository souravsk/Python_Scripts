num = int(input("Enter the Number:- "))
n = num
flag = True
while num!= 0:
    num1 = num%10
    print(num,num1)
    num = int(num/10)
    print(num,num1)
    num2 = num%10
    print(num,num2)
    if abs(num1 - num2) != 1:
        flag = False

if flag == True:
    print(n,"it is jumping number")
else:
    print(n,"it is not a jumping number")
