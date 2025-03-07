#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        odd += 1
        print("The number of odd numbers is: ", odd)