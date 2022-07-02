"""I broke this into functions to check for different things.
2 reasons: 
1. In your code, if a string of letters is entered, an error occurs 
in the file instead of sending an error message to the user.
2. If a float is entered, you're converting it to an integer
when it should actually be telling the user an error message because the
prompt was not followed correctly. 

So, when the input is given, we run the check_input_for_int function
to determine if the input is an integer.

If the input is a float or letter, the function will throw
an error message (f"{input} is not an integer"). 

Still within the check_input_for_int funciton, if the input is an integer,
we run the check on whether the integer is even or odd in the odd_or_even function. 

The odd_or_even function is written in one line to show you a different
way to write "if' statements. This is called a ternary operation. 
The order of the conditions/expressions is a little different.

Take this one slow when trying to understand it because I did things really differntly.
I also understand you might not know what a try except statement is,
so we will talk that over too."""

# Check if odd or even
def odd_or_even(num):
    return f"{num} is even" if num % 2 == 0 else f"{num} is odd"

# First determine if input is an integer
def check_input_for_int(input):
    try:
        i = int(input)
        return odd_or_even(i)
    except ValueError:
        return f"{input} is not an integer"

i = input("Enter an integer here: ")

print(check_input_for_int(i))
