import math
import subprocess
def calc():
    print("Welcome to the Utsey Python Calculator v1.0!\n")
    print("Please select an operation:\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exit\n")
    def numbers():
        global num1
        num1 = int(input("\nEnter first number: "))
        global num2
        num2 = int(input("Enter second number: "))
    def calc2():
        user_input = input("\nPress Enter to perform another calculation or type 'q' and press Enter to quit.\n\n\n")
        if user_input == 'q':
            print('Goodbye!')
        else:
            calc()
    def clip(cb_txt):
      cmd='echo '+cb_txt.strip()+'|clip'
      return subprocess.check_call(cmd, shell=True)
    selection = input("Select an option: (1,2,3,4,5,6): ")
    if selection == '1':
        print("\nYou chose Addition!")
        numbers()
        total = num1 + num2
        print("\nSolution:",num1,"+",num2,"=",total)
        clip(str(total))
        print("\nThe solution(",total,")has been successfully copied to the clipboard!")
        calc2()
    elif selection == '2':
        print("\nYou chose Subtraction!")
        numbers()
        total = num1 - num2
        print("\nSolution:",num1,"-",num2,"=",total)
        clip(str(total))
        print("\nThe solution(",total,")has been successfully copied to the clipboard!")
        calc2()
    elif selection == '3':
        print("\nYou chose Multiplication!")
        numbers()
        total = num1 * num2
        print("\nSolution:",num1,"*",num2,"=",total)
        clip(str(total))
        print("\nThe solution(",total,")has been successfully copied to the clipboard!")
        calc2()
    elif selection == '4':
        print("\nYou chose Division!")
        numbers()
        total = num1 / num2
        print("\nSolution:",num1,"/",num2,"=",total)
        clip(str(total))
        print("\nThe solution(",total,")has been successfully copied to the clipboard!")
        calc2()
    elif selection == '5':
        print("\nYou chose Square Root!")
        num3 = int(input("\nEnter number: "))
        total = math.sqrt(num3)
        print("\nSolution: The square root of", num3, "is:",total)
        clip(str(total))
        print("\nThe solution(",total,")has been successfully copied to the clipboard!")
        calc2()
    elif selection == '6':
        print('Goodbye!')
    else:
        print("\nInvalid selection! Please enter a valid operation.\n")
        input("Press any key to continue...\n\n\n")
        calc()
calc()
