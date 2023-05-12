"""
    Name: utils.py
    Author: Bill Edwards
    Created 02/23/2023
    Purpose: contains general utility funcitons.
"""

def get_int(prompt):
    """
    get an intergert from teh user with try catch
    the promt string parameter is used to ask the user
    for the type of input needed
    """

def get_int(prompt):
    #declare local variable
    num = 0

    #ask the user for an input based on teh prompt: string parameter
    num = input(prompt)

    #if the input is numeric, convert to int and retuurn value
    try:
        return int(num)
    
    #if the number is not numeric, inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num} which is not a whole number")
        print("Please try again. \n")

        #call function from the beginning
        #this is a recursive function call
        return get_int(prompt)

def title(statement):
    """
        takes in a string argument
        returns a string with ascii decorations
    """
    #get the length of the statement string variable
    text_length = len(statement)

    #create a title string
    #initialize the result string variable
    result = ""
    result = result + "+--" + "-" * text_length + "--+\n"
    result = result + "|  " + statement + "  |\n"
    result = result + "+--" + "-" * text_length + "--+\n"

    return result

def get_float(prompt):
    """
    get an intergert from teh user with try catch
    the promt string parameter is used to ask the user
    for the type of input needed
    """
    #declare local variable
    num = 0

    #ask the user for an input based on teh prompt: string parameter
    num = input(prompt)

    #if the input is numeric, convert to int and retuurn value
    try:
        return float(num)
    
    #if the number is not numeric, inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num} which is not a number")
        print("Please try again. \n")

        #call function from the beginning
        #this is a recursive function call
        return get_float(prompt)
    
def main():
    #place code here to test modules
    print(title("Print Title Test"))
    int_num = get_int("Please enter a whole number: ")
    print(f"Your whole number is: {int_num}")
    float_num = get_float("Please enter a number: ")
    print(f"Your number is: {float_num}")


if __name__ == "__main__":
    main()