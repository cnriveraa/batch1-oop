#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
sum = 0
for i in range(10):
    num = int(input("Enter a number: "))
    sum += num
    print("The sum of all the numbers is: ", sum)