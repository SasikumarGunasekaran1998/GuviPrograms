num = input() #Get input
boole = num.isalpha() #fuction to check it's alphabet
if boole == True:
    if num == 'a' or num =='e' or num =='i' or num =='u' or num =='o' : #Check for vowel
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
