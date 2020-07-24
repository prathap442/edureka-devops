import re
class BusinessAttendance():
    def __init__(self,pwd):
        self.password = pwd
    
    def encrypt(self):
        business_encryptor(pwd)

    def valid(self):
        if(re.match('^[a-zA-Z0-9_]+$',self.password)) and(len(self.password) == 12):
            return True
        else:
            return False

pwd = input("Enter the password")
b_attendance = BusinessAttendance(pwd)
print(b_attendance.valid())