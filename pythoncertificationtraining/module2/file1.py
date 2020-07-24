nums =set([1,1,2,3,3,3,4,4])
# The Set basically returns the unique keys back to us
print(nums)

'''
   This is the problem2
'''

d = {
    "john":40,
    "peter":45
}
print(list(d.keys()))


'''
    A website requires a user to input username and password to register.
    Write a program to check the validity of password given by user.
    Following are the criteria for checking password
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    2. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
'''
d = input("Enter the Passcode")
import re
import pdb
import re
class PasscodeValidator():
    def __init__(self,password):
        self.password = password
    
    def is_valid(self):
        true_values = []
        true_values.append(self.atleast_one_small_letter_validator())
        true_values.append(self.atleast_one_numeric_validator())
        true_values.append(self.atleast_one_capital_letter_validator())
        true_values.append(self.atleast_one_special_char_validator())
        true_values.append(self.password_length_validator())
        print(true_values)
        return False not in true_values
    
    def atleast_one_small_letter_validator(self):
        regex = '.*[a-z]'
        pdb.set_trace()
        if(re.match(regex,self.password)):
            return True
        else:
            return False

    def atleast_one_numeric_validator(self):
        regex = '.*[0-9]'
        pdb.set_trace()
        if(re.match(regex,self.password)):
            return True
        else:
            return False

    def atleast_one_capital_letter_validator(self):
        regex = '.*[A-Z]'
        pdb.set_trace()
        if(re.match(regex,self.password)):
            return True
        else:
            return False

    def atleast_one_special_char_validator(self):
        regex = '.*[$#@]'
        pdb.set_trace()
        if(re.match(regex,self.password)):
            return True
        else:
            return False

    def password_length_validator(self):
        if((len(self.password) >= 6) and (len(self.password) <= 12)):
            return True
        else:
            return False

    
password_given = input("Enter the Password")
pv = PasscodeValidator(password_given)
print(pv.is_valid())

a = [1,2,3,45,34,23]
counter = 0
for x in a:
    print("value = "+str(x)+"index ="+str(counter))
    counter += 1



string_given = "H1e2l3l4o5w6o7r8l9d"
counter = 0
for x in string_given:
    if(counter%2 == 0):
        print(x)
    counter += 1



'''
  reverse the string
'''
givenstring = "reversify"
reversified = ""
for x in givenstring:
    reversified = x + reversified
print(reversified)



'''
  print the number of count for the each letter in the string
'''
dict_formter = {}
for x in givenstring:
    if(dict_formter.get(x)):
        dict_formter[x] += 1
    else:
        dict_formter[x] = 1

print(dict_formter)


'''
   print("common elements")
'''

a = set(['a','b','c','d','a'])
b = set(['x','z','y','a'])
print(a&b)


'''
  print("The unrepeated elements with order being preserved")
'''
given_list = (12,24,35,24,88,120,155,88,120,155)
resultant_list = []
for x in given_list:
    if(x not in resultant_list):
        resultant_list.append(x)
print(resultant_list)


'''
.By using list comprehension, 
 please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
'''
given_list = [12,24,35,24,88,120,155]
duplicate_remover = [x for x in given_list if x!= 24]


'''
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]
When looping with the indexes in python we go by enumerate
'''
given_list = [12,24,35,24,88,120,155]
after_removal_from_positions = []
removal_positions = [0,4,5]
for index,value in enumerate(given_list):
    if index not in removal_positions:
        after_removal_from_positions.append(value)
print(after_removal_from_positions)

'''
By using list comprehension, please write a program to print the list 
after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]
'''
given_list = [12,24,35,70,88,120,155]
residue_list = []
for num in given_list:
    if not((num%5 == 0) or (num%7==0)):
        residue_list.append(num)
print(residue_list)

'''
  Please  write  a  program  to  randomly  generate  
  a  list  with  5  numbers,  
  which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
'''
import random
generated_list = []
while(len(generated_list) < 5):
    current_number = random.randint(1,1001)
    if((current_number%5 == 0)or(current_number%7==0)):
        if not(generated_list.__contains__(current_number)):
            generated_list.append(current_number)

'''
  Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  
  with  a  given  n  input  by console (n>0)
'''

sum = 0
nth_serial_number = 5
last_value = (nth_serial_number/nth_serial_number+1)
start = 1
while(start <= nth_serial_number):
    sum += (start/(start+1))
    start += 1

print(round(sum,2))

