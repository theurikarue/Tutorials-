string =("My name is Bonface Karue")
print(string.upper()) #in upper case
print(string.lower()) #in lower case
print(string.isupper()) #to check whether it is in upper case
print(string.islower()) #to check whether it is in lower case
print(len(string)) # to check the length of the string
print(string[0])# returns character in first position of the string
vowels="aeiouAEIOU"
#print(string.count(vowels))
#vowels = 'AEIOUaeiou'
#for ele in vowels:

#	string=string.replace(ele, K)
#	K="*"
print(string.index("a")) #returns index of first instance of letter a 
print(string.index("face")) #returns index of where face begins
print(string.replace("face","ke").replace("Karue","Reinhard")) #replaces face with ke
print(string.split())#it will split the string into substrings wherever it encounters a whitespace character
