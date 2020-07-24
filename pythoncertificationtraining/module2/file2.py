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
    
if(__main__ == "name"):
    password_given = input("Enter the Password")
    pv = PasscodeValidator(password_given)
    print(pv.is_valid())