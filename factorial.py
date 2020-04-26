num = int(input("Enter the number to find the factorial of :"))

fact = 1
for i in range (1, num+1):
    fact *= i

print("The factorial of the given number is :", fact)
