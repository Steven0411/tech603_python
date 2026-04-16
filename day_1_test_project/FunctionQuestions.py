import string

print("\nQ1a\n")

# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list

# e.g. f(12) = [1, 2, 3, 4, 6, 12]

# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:

def divisor(i: int) -> list:
    divisors = []
    for num in range(1, i + 1):
        if i % num == 0:
            divisors.append(num)

    return divisors

print(divisor(12))
print(divisor(1))

print("\nQ1b\n")

# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers

# is a factor of the other, false otherwise

# (bonus points if you call your previous function within this function


# A1b:

def factor(a: int, b: int) -> bool:
    # So I don't need to worry about which input is bigger
    if b > a:
        c=b
        b=a
        a=c

    if b in divisor(a):
        return True
    else:
        return False

print(factor(6, 24))
# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")

# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:

def alphapos(a: string) -> int:
    for char in alphabet:
        if char == a:
            return alphabet.index(char)
    return None

print(alphapos("g"))


print("\nQ2b\n")

# Q2b: create a function which takes a persons name as an input string and returns an

# ID number consisting of the positions of each letter in the name

# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# A2b:

def nametoid(name: string) -> int:
    ID = ""
    for char in name:
        ID += str(alphapos(char))

    return ID

print(nametoid("batman"))

print("\nQ2c\n")

# Q2c: Create a function which turns this ID into a password. The function should subtract

# the sum of the numbers in the id that was generated from the whole number of the id.

# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


# A2c:

def nametopassword(name):
    remove = 0
    for char in name:
        remove += alphapos(char)
    return int(nametoid(name)) - remove

print(nametopassword("batman"))

# -------------------------------------------------------------------------------------- #


print("\nQ3a\n")

# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


# A3a:

def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            return False

    print(f"{n} is prime")
    return True

def isprime2(n):
    if len(divisor(n)) == 2:
        print(f"{n} is prime")
        return True
    else:
        print(f"{n} is not prime")
        return False

isprime(105000787278)

print("\nQ3b\n")

# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:

def isprimecatch(n):
    if isinstance(n, int):
        isprime(n)

    else:
        print("not an integer")
        return None

# when taking user input use string.isdigit() function
def isprimecatch2():
    running = True
    while running:
        n = input("Enter number: ")
        if n.isdigit():
            isprime(n)
        else:
            print("not an integer")

isprimecatch("3")
isprimecatch(6)
# -------------------------------------------------------------------------------------- #