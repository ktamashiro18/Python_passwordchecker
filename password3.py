password = str(raw_input("Please enter a password that is at least 8 characters long and contains at least 1 number and at least 1 letter:\n"))#prompts the user for their password
l = list(password)#creates a list to store each of the password's characters individually
def uppercase(password):#function to find uppercase letters in a password - other two definitions follow the same structure
	upper = False#starts off as false, means that there are no uppercase letters	
	for i in range(0,len(l)):#range is the amount of letters in the password
		if l[i].isupper() == True:#if one of the letters is uppercase
			upper = True#changes it to true, there are uppercase letters
			break#breaks the for loop because it's unnecessary to look for more uppercase letters
	if upper == False:#if there are no uppercase letters, requests the user to add uppercase letters
		return "Your password needs an uppercase letter."
	elif upper == True:#if there are uppercase letters, nothing is sent out
		return ""
def lowercase(password):#function to find lowercase letters in a password - follows the same structure as the uppercase function
	lower = False
	for i in range(0,len(l)):
		if l[i].islower() == True:#if one of the letters is lowercase
			lower = True
			break
	if lower == False:#if there are no lowercase letters, requests the user to add lowercase letters
		return "Your password needs a lowercase letter."
	elif lower == True:
		return ""
def number(password):#function to find numbers in a password - follows the same structure as the other two functions
	number = False
	for i in range(0, len(l)):
		if l[i].isalpha() == False:#if one of the characters is a number
			number = True
			break
	if number == False:#if there are no numbers, requests the user to add a number
		return "Your password needs a number."
	elif number == True:
		return ""
def length(password):#function to find the length of the password
	if len(password) < 8:#if the password is less than eight characters, then it requests that the user make it longer
		return "Your password needs to be eight or more characters."
	else:#sends nothing out if it is eight characters
		return ""
def special(password):#function to find special characters in a password
	if password.isalnum() == False or " " in password:#if the password does not contain only alphanumeric characters (numbers or letters)
		return "Your password cannot contain spaces or special characters."
	elif password.isalnum() == True and " " not in password:#if the password doesn't contain any special characters
		return ""
print(uppercase(password)),(lowercase(password)),(number(password)),(length(password)),(special(password))#prints out any suggestions to improve the password
while len(length(password)) > 2 or len(uppercase(password)) > 2 or len(lowercase(password)) > 2 or len(number(password)) > 2 or len(special(password)) > 2:#keeps prompting the user if they don't have a strong password
	password = str(raw_input("Please enter a password that is at least 8 characters long and contains at least 1 number and at least 1 letter:\n"))
	l = list(password)#have to update the list and return the functions again (below)
	print(uppercase(password)),(lowercase(password)),(number(password)),(length(password)),(special(password))#prints out any suggestions to improve the password
if len(password) >= 8 and len(uppercase(password)) < 2 and len(lowercase(password)) < 2 and len(number(password)) < 2 and len(special(password)) < 2:#if the password follows all the guidelines - takes advantage of the length of the return of the functions -, congratulates the user
	print "Good job! Your password is strong."