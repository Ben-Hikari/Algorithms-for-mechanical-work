#1.2 build
#Definition: MA calculater, Incomplete work.
#adding 2 numbers
def add(x, y):
    return x + y
    
#subracting 2 numbers
def subtract(x, y):
    return x - y

#multiplies 2 numbers
def multiply(x, y):
    return x * y

#divides 2 numbers
def divide(x, y):
    return x / y

#simple interface

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("IMA is Fr / Fe")
print("MA is OUTf / INf")
print("efficiency is INf / OUTf")

while True
    #takes input from user
    choice = input("Enter Choice(1/2/3/4): ")
    
    #check if choice is one of 4 options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number): "))
        num2 = float(input("Enter second number): "))
        
        if choice == '1':
            print(num1, "+" num2 "=", (add num1, num2))
            
             elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
