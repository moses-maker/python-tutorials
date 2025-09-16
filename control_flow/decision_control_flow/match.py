marks = int(input("Enter your marks?"))

match marks:
    case 30 | 40:
        print("A")

    case 50 | 60:
        print("Bs")

    case _:
        print("Wrong")
        