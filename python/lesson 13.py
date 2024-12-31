###Write a program to demonstrate a right angle triangle pattern

rows=int(input("enter the number of rows"))
for y in range(rows):
    for x in range(y+1):
        print("*",end="")
    print()    
