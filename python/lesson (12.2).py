####Write a program to print all the prime numbers which come in the range entered by the user?
upper_range = int(input("Enter the upper range please: "))
lower_range = int(input("Enter the lower range please: "))

for x in range(lower_range, upper_range + 1):
    if x > 1:  
        for y in range(2, x):
            if x % y == 0:  
                break
        else:  
            print(x)
           
           
