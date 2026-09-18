'''
Simply displays a Christmas Tree on stdout.
Three different implementation are available.

Can be used as script to test the three implementations

Note the use of exception in the script mode:
- int() raises a ValueError is the value cannot be parsed as an integer
- an extra validation is added if the result is negative, 1 or 2 and 
also raises a ValueError
- only ValueError is catched for the loop

This is not the best way to do it but it shows how to manipulate Exceptions
'''

def print_naive(height):
    '''
    Naive implementation of the Christmas Tree using embedded loops
    1. Main loop on the height of the tree
    1.2. Inner loop to add spaces
    1.3. Inner loop to add stars
    2. Second loop to add spaces before the trunk

    Note the optional argument `end` in `print()` calls to avoid line breaks
    '''
    for line in range(height): # 1
        for row in range(height - line - 1): # 1.2
            print(" ", end="")
        for row in range(2 * line + 1): # 1.3
            print("*", end="")
        print("")

    for row in range(height - 1): # 2
        print(" ", end="")
    print("|")

def print_generator(height):
    '''
    Implementation of the Christmas Tree using an inline generator
    An inline generator is a "loop within an container", i.e.,
    a container generated on-the-fly using a loop. A simple example:

    `squares = [i*i for i in range(10)]`

    This implementation also uses `str.join(<array>)` to concatenate all
    the strings generated (by the generator). The concatenation is `\n`
    that is the escape character encoding a line break.

    Note also that the strings are created by using operator `*`
    on two different types: int <n> and string <s>.
    /!\ This operator multiplies <n> times the string <s>
    BUT ONLY with Python. Most languages don't do that!
    The operator `+` is used to concatenate the strings.
    /!\ This operator concatenates strings on most languages
    BUT NOT ALL OF THEM (*beep*ing PHP)
    '''
    print("\n".join([" " * (height - n - 1) + "*" * (2 * n + 1)
                     for n in range(height)]))
    print(" " * (height - 1) + "|") 

def print_rjust(height):
    '''
    Implementation of the Christmas Tree using `str.rjust(l, [c])`

    rjust stands for "right justify" and consequently add the
    adequate number of spaces (or optional parameter <c>) so that
    the string is right justified to the given length <l>.

    Note the 'numbers' used in this version are easier to understand.
    '''
    for line in range(height):
        print("*".rjust(2 * line + 1, "*").rjust(height + line))
    print("|".rjust(height))


if __name__ == "__main__":
    height = None

    while height is None or height < 3:
        try:
            height = int(input("Height of the tree (min. 3 or 0 to quit)? "))
            if height == 0:
                exit(0)
            if height < 3:
                height = None
                raise ValueError
        except ValueError:
            print("The value is invalid")

    print("naive")
    print_naive(height)

    print("generator")
    print_generator(height)

    print("rjust")
    print_rjust(height)
