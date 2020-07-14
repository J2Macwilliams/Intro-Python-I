# Write a function is_even that will return true if the passed-in number is even.

def even_odd(x):
    if x % 2 == 0:
        print("Even!")
    else:
        print("Odd")

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
even_odd(num)


