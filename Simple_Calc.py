###############################################
#File Name: Simple_Calc.py
#Created By: Ard Aunario
#Date Created: 8/31/19
#Description: Simple calculator that does basic math operations
################################################
################################################
KeepGoing = True

Num = input("Enter Number(0 - 9) or 'q' to quit: ")

# Check if user input is a number and continues #       
if Num == 'q':
    print("Goodbye!")
elif int(Num) <= 0 or int(Num) >= 0:
    # Change Num to integer #
    value = float(Num)
    
    try:
        while (KeepGoing):
            Op_input = input("Enter operation ( +, -, *, /, =) or 'q' to quit: ")

            ValidOp = ['+', '-', '*', '/', '=', 'q']
            Op = ValidOp.index(str(Op_input))

            if Op == 4:
                # Print Value #
                 print(str(value))
            elif Op == 5:
                print("Goodbye!")
                KeepGoing = False
            
            else:
                # Second number user input #
                Num2 = input("Enter Number(0 - 9) or 'q' to quit: ")

                if Num2 == 'q':
                    print("Goodbye!")
                    KeepGoing = False
                elif int(Num2) <= 0 or int(Num2) >= 0:
                    int(Num2)
                    #Addition
                    if Op == 0:
                        value += float(Num2)
                    #Subtraction
                    elif Op == 1:
                        value -= float(Num2)
                    #Mulitplication
                    elif Op == 2:
                        value *= float(Num2)
                    #Division
                    elif Op == 3:
                        value /= float(Num2)
                print(str(value))
            
    except ZeroDivisionError:
            print("Invalid operation: Can't divide by zero.")
    except ValueError:
            print("Invalid operation: Not a valid operation.")
else:
    print("Invalid input: User input is not an integer.")
        
            
