""" In Python 3.x, a built-in input() function is used to ask a user for an input. The user can stop typing and submitting the input 
    by pressing the ENTER or RETURN key. To capture the input taken by input(), A variable is needed. 
    A variable is a container to hold data """

user_input = input()

""" input() can also work without even storing the submitted data by the user, but it's of no use """
input()

""" To tell the user what to type as an input, a quoted text using single or double commas are used inside the parenthesis of input() 
    function """

input_hint = input("type your name - ")

""" A variable can also be passed (of any type) instead of an hard-coded quoted text inside the parenthesis of input() """

string_hint  = "type your birthdate - "
list_hint    = ['A List was passed']
num_hint     = 123

string_hint_input   = input(string_hint)
list_hint_input     = input(list_hint)
num_hint_input      = input(num_hint)

""" 
    Concatenation of strings(quoted text) OR addition of variables OR addition of a variable and quoted texts are also possible
    inside the parenthesis of input() 
    
    Note :- Spaces should be given after the end of any quoted texts because Python doesn't automatically separate added strings by spaces  
   
"""

text_text_dump = input("type " + "your " + "Password '>' ")  # Adding hard-coded quoted texts inside ()

text_1 = "Are you "
text_2 = "a geek? "
var_var_dump = input(text_1 + text_2)   # Adding variables inside ()

var_text_dump = input(text_1 + "  '>' ")   # Adding a variable and quoted text inside ()
