import sys
def palindrome():
    given_string = sys.argv[1]
    reversed_string = ""
    for x in given_string:
        reversed_string = x + reversed_string
    if(reversed_string == given_string):
        print("Palindrome")
        return "Palindrome"
    else:
        print("Not a palindrome")
        return "Not a palindrome"
palindrome()