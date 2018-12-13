""" In Python 3.x, a built-in input() function is used to ask a user for an input. The user can stop typing and submitting the input 
    by pressing the ENTER or RETURN key. To capture the input taken by input(), A variable is needed. 
    A variable is a container to hold data """

user_input = input()

""" To tell the user what to type as an input, a quoted text using single or double commas are used inside the parenthesis of input() 
    function """

input_hint = input("type your name - ")

""" A variable can also be passed instead of an hard-coded quoted text inside the parenthesis of input() """

hint      = "type your birthdate - "
birthdate = input(hint) 
