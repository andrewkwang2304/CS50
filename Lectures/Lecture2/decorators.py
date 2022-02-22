# A decorator takes a function as input, and returns a modified version
# of that function as output.

# This is functional programming paradigm, where functions are values.

# This is something specific to Python

def announce(f):
    def wrapper():
        print("About to run the function.")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()
