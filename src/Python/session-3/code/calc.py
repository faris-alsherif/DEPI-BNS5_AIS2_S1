def add(x: float, y: float):
    '''sum function

    Args:
        param_1 = user must input the first num
        type_param_1 = float
        param_2 = user must input the second num
        type_param_2 = float
        return : this function return the sum of two number
        type_return = float
    '''
    return x+y

def sub(x: float, y: float):
    '''sub function

    Args:
        param_1 = user must input the first num
        type_param_1 = float
        param_2 = user must input the second num
        type_param_2 = float
        return : this function return the sub of two number
        type_return = float
    '''
    return x-y

def div(x: float, y: float):
    '''division function

    Args:
        param_1 = user must input the first num
        type_param_1 = float
        param_2 = user must input the second num
        type_param_2 = float
        return : this function return the division of two number
        type_return = float
    '''
    return x/y

def mul(x: float, y: float):
    '''multiply function

    Args:
        param_1 = user must input the first num
        type_param_1 = float
        param_2 = user must input the second num
        type_param_2 = float
        return : this function return the multiply of two number
        type_return = float
    '''
    return x*y


def main():
    print("calc app")
    print("===================")

    print("1 add")
    print("2 sub")
    print("3 mul")
    print("4 div")

    choice = input("Enter choice (1 - 2 - 3 - 4): ")

    num_1 = float(input("Enter first num: "))
    num_2 = float(input("Enter second num: "))

    if choice == "1":
        print(f"first num {num_1}, second num {num_2}", add(num_1, num_2))

    elif choice == "2":
        print(f"first num {num_1}, second num {num_2}", sub(num_1, num_2))

    elif choice == "3":
        print(f"first num {num_1}, second num {num_2}", mul(num_1, num_2))

    elif choice == "4":
        print(f"first num {num_1}, second num {num_2}", div(num_1, num_2))

    else:
        print("Invalid choice")