#define functions
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b==0:
        return "Error!Division by zero"
    return a/b 
    
#user interface
def show_menu():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
#input
def my_calculator():
   while True:
       show_menu()
       choice = input("Choose an operation between 1-5: ")
       
       if choice == "5":
           print ("Goodbye!")
           break
       if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number "))
        except ValueError:
            print("Invalid input")
            continue
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2": 
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Invalid operation")
            

            
            
           