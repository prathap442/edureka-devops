'''
Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes.Example: If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9dThen, the output of the program should be:Helloworld
'''
string_given = "H1e2l3l4o5w6o7r8l9d"
counter = 0
for x in string_given:
    if(counter%2 == 0):
        print(x)
    counter += 1