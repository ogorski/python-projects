age = int(input("How old are you?"))
if (age >= 21): 
   print('You can enter by yourself')
elif (age >= 18) and (age < 21):
   print('You can enter here with parent')
else:
   print('You are forbidden here')

# Basic tutorial of operators if, elif, else;
# Variable age answers for how old is user; int transforms input into numeric from string; if here responsible for correct age of user here from 21 to even more age; elif here answers for if user are underage or fully aged person; else here answers with rejection for our user if he/she underage