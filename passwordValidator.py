##Input list of passwords
#Check for validity
##Passwords Must Have: 
    #At least 8 Characters
    #At least 1 lowercase character[a-z]
    #At least 1 uppercase character[A-Z]
    #At least 1 number[0-9]
    #At least one character from [!@#$%^&*_]

import re

passwords = ['Gr3at_T1me5', 'GreatTimes!', 'P30ple1!', 'N0#worr1es', 'Pwd2d@y', 'Sup3rS3cur3']
#Setting variable to confirm validity/invalidity
flag = 0

for password in passwords:
    print(password)
    while True:
        #At Least 8 Characters
        if (len(password)<8):
            flag = -1
            break
        #At least 1 lowercase character
        elif not re.search("[a-z]", password):
            flag = -1
            break
        #At least 1 uppercase character
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        #At least 1 number
        elif not re.search("[0-9]", password):
            flag = -1
            break
        #At least one special character
        elif not re.search("[!@#$%^&*_]", password):
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password\n")
            break
    if flag == -1:
        print("Invalid Password\n")