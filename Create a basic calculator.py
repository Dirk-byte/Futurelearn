stop = False

while stop == False:

    first_number = int(input("Enter the first number: "))
    second_number= int(input("Enter the second number: "))
    input_of_factor = input("addition, substraction, multiplication or division? ")
    if input_of_factor == "addition":
        print(first_number + second_number)
    elif input_of_factor == "substraction":
        print(first_number - second_number)
    elif input_of_factor == "multiplication":
        print(first_number * second_number)
    elif input_of_factor == "division":
        try:
            print(first_number / second_number)
        except:
            print("Error")
    else:
        stop = True