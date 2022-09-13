##In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues.
##The game offers one of the following hints in response to your guess:
##"Pico" when your guess has a correct digit in the wrong place, "Fermi" when your
##guess has a correct digit in correct place, and Bagels if your guess has no correct digits.
##You have 10 tries to guess the secret number.
import random
def secretNumber(): #Generates the secret number
    digits = list("123456789")
    random.shuffle(digits)
    number = ''
    for item in range(0,3):
        number = number + str(digits[item])
    return number

def numToList(num): #Converts the number to a list
    temp_list = []
    num = int(num)
    while num>=1:
        rem = num%10
        temp_list.append(rem)
        num = num//10
    temp_list.reverse()
    return temp_list
    
#secretNumber = secretNumber() #random number
secretNumber = 367
secretNumber_list = numToList(secretNumber)
print("""I am thinking of a 3-digit number with no repeated digits.Try to guess what it is.
Here are some clues:
When I say:  That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.
For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
I have thought up a number. You have 10 guesses to get it.""")
userNumber = int(input("Enter a three-digit number: "))
win = False #To determine win/lose
numChances = 1 #Maximum 10
while (numChances <=10 and win == False):
    if numChances > 1:
        print("Try again. Chance",numChances,":")
        userNumber = int(input())
    userNumber_list = numToList(userNumber)
    numDigits = len(userNumber_list) #Number of digits in the number entered by user
    num_incorrect = 0 #To determine unequal digits
    num_correct = 0 #To determine equal digits
    clue = "" #Clue to be displayed
    while(numDigits !=3): #check if number is of three digits
        print("You can enter only three digit numbers")
        userNumber = int(input("Enter a three-digit number: "))
        userNumber_list = numToList(userNumber)
        numDigits = len(userNumber_list)
    else: #Enters this block if the number entered by user is of three-digits
        for i in (0,1,2):
            result = (secretNumber_list[i] == userNumber_list[0]) or (secretNumber_list[i] == userNumber_list[1]) or (secretNumber_list[i] == userNumber_list[2]) #check if digits match
            if result : #equal
                if i == userNumber_list.index(secretNumber_list[i]): #check if same index or not
                    clue = clue +"Fermi"+" "
                    num_correct = num_correct + 1
                else : #do not match
                    clue = clue+"Pico"+" "
            else: #Unequal
                num_incorrect = num_incorrect + 1
        if num_incorrect == 3: # all three digits are different
            clue = ""
            clue = "Bagels"
        if num_correct == 3: #all three digits are same
            clue = ""
            clue = "Congratulations! You guessed it right!"
            win = True
        print(clue)
    numChances = numChances + 1
if win != True: #chances exhausted but number is not guessed
    print("Sorry! Your chances have exhausted! The number is ",secretNumber)        
