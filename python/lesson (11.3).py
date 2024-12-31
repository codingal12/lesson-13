##Write a program to check if the number entered by the user is an Armstrong number or not?
b=int(input("enter your number"))

summ=0
temp=b
while temp>0:
    digit=temp%10 # 153%10=3
    summ += digit**3
    temp //= 10
if b==summ:
    print("your nomber is an armstorg number")
else:
    print("nahi h armstrong")