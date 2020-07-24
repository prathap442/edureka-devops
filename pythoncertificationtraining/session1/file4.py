import re
def calculate_number_of_letters_and_digits(given_entity):
    obtained_elements = [element for element in given_entity]
    hash_mapper = {
      "LETTERS": 0,
      "DIGITS": 0  
    }
    for element in obtained_elements:
        if(re.search(r'[\d\.]+',element)):
            hash_mapper["DIGITS"]+=1 
        else:
            hash_mapper["LETTERS"]+=1 
    return hash_mapper

print(calculate_number_of_letters_and_digits("iswara123"))
