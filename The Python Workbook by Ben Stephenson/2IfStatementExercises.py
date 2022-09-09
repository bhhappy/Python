#Exercise 34: Even or Odd?
#Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.
def Exercise34():
    num = int(input("Enter a integer:"))
    remainder = num%2
    if remainder == 0 : print("The integer is even")
    else : print("The integer is odd")


#Exercise 35: Dog Years
#It is commonly said that one human year is equivalent to 7 dog years. However this simple conversion fails to recognize that dogs reach adulthood in approximately two
#years. As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog
#years. Write a program that implements the conversion from human years to dog years described in the previous paragraph. Ensure that your program works correctly for
#conversions of less than two human years and for conversions of two or more human years. Your program should display an appropriate error message if the user enters
#a negative number.
def Exercise35():
    humanYears = float(input("Enter human years:"))
    if humanYears <= 0 : print("Sorry, please enter a positive number")
    elif humanYears <= 2 :
        dogYears = humanYears*5.25
        print("Number of dog years:",dogYears)
    else:
        temp = humanYears - 2
        dogYears = 10.5 + (4*temp)
        print("Number of dog years:",dogYears)

#Exercise 36:Vowel or Consonant
#In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message
#indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is
#a consonant. Otherwise your program should display a message indicating that the letter is a consonant.
def Exercise36():
    ch = input("Enter a character:")
    vowels = ('a','e','i','o','u')
    if ch in vowels: print("The entered letter is a vowel")
    elif ch == 'y': print("Sometimes y is a vowel, and sometimes y is a consonant")
    else: print("The letter is a consonant")


#Exercise 37: Name that Shape
#Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user and then report the appropriate name as part of
#a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of this range is entered
#then your program should display an appropriate error message.
def Exercise37():
    shapes = {
        "3":"Triangle",
        "4":"Rectangle",
        "5":"Pentagon",
        "6":"Hexagon",
        "7":"Septagon",
        "8":"Octagon",
        "9":"Nonagon",
        "10":"Decagon"
        }
    numSides = int(input("Enter number of sides:"))
    if numSides >= 3 and numSides <= 10:
        print(shapes.get(str(numSides)))
    else: print("Please enter side within range 3-10")

#Exercise 38: Month Name to Number of Days
#The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month from the user as a string. Then your
#program should display the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.
def Exercise38():
    month = input("Enter month(Mmm):")
    if month == 'Sep' or month == 'Apr' or month== 'Jun' or month == 'Nov' :
        print("Number of days are 30 days")
    elif month == 'Feb' :
        print("Number of days are 28 or 29 days")
    elif month == 'Jan' or month == 'Mar' or month== 'May' or month == 'Jul' or month == 'Aug' or month == 'Oct' or month == 'Dec' :
        print("Number of days are 31 days")
    else: print("Invalid month")


##Exercise 39: Sound Levels
##The following table lists the sound level in decibels for several common noises.
##
##Noise Decibel level (dB)
##Jackhammer 130
##Gas lawnmower 106
##Alarm clock 70
##Quiet room 40
##
##Write a program that reads a sound level in decibels from the user. If the user enters a decibel level that matches one of the noises in the table then your program
##should display a message containing only that noise. If the user enters a number of decibels between the noises listed then your program should display a message
##indicating which noises the level is between. Ensure that your program also generates reasonable output for a value smaller than the quietest noise in the table, and for a
##value larger than the loudest noise in the table.
def Exercise39():
    sound = float(input("Enter sound level in decibels: "))
    sound_levels = { #in decibels
        "Jackhammer": 130,
        "Gas lawnmower": 106,
        "Alarm clock": 70,
        "Quiet room": 40
        }
    for noise,level in sound_levels.items():
        if sound == float(level):
            print(noise)
            break;
        elif sound < min(sound_levels.values()) or sound > max(sound_levels.values()):
            print("values out of bounds")
            break;
        else:
            sound_levels_list = list(sound_levels.values())
            index = sound_levels_list.index(level)
            if index+1 < len(sound_levels):
                level2 = sound_levels_list[index+1]
                if sound < float(level) and sound > float(level2):
                    print("sound level between",level,"decibels and",level2,"decibels")



#Exercise 41: Note To Frequency
#The following table lists an octave of music notes, beginning with middle C, along with their frequencies.
#Note Frequency (Hz)
#C4 261.63
#D4 293.66
#E4 329.63
#F4 349.23
#G4 392.00
#A4 440.00
#B4 493.88
#Begin by writing a program that reads the name of a note from the user and displays the note’s frequency. Your program should support all of the notes listed
#previously. Once you have your program working correctly for the notes listed previously you should add support for all of the notes from C0 to C8.
#While this could be done by adding many additional cases to your if statement, such a solution is cumbersome, inelegant and unacceptable for the purposes of this exercise.
#Instead, you should exploit the relationship between notes in adjacent octaves. In particular, the frequency of any note in octave n is half the frequency of the corresponding
#note in octave n+1. By using this relationship, you should be able to add support for the additional notes without adding additional cases to your if statement.
def Exercise41():
    import string
    note = input("Enter the note: ")
    frequencies = {
        "C4": "261.63",
        "D4": "293.66",
        "E4": "329.63",
        "F4": "349.23",
        "G4": "392.00",
        "A4": "440.00",
        "B4": "493.88"
        }
    noteLetter = note[:1]
    noteNumber = int(note[-1])
    if (note in frequencies.keys()):
        frequency = frequencies.get(note)
        print("Frequency:",frequency)
    elif (noteLetter in ('C','D','E','F','G','A','B')) and (noteNumber >= 1 and noteNumber <=8) :
        count = 4-noteNumber
        baseNote = str(noteLetter+"4")
        print(frequencies.get(baseNote))
        frequency = float(frequencies.get(baseNote))/(pow(2,count))
        print("Frequency:",frequency)
    else: print("Invalid note")


##Exercise 42: Frequency To Note
##In the previous question you converted from note name to frequency. In this question you will write a program that reverses that process. Begin by reading a frequency
##from the user. If the frequency is within one Hertz of a value listed in the table in the previous question then report the name of the note. Otherwise report that the
##frequency does not correspond to a known note. In this exercise you only need to consider the notes listed in the table. There is no need to consider notes from other octaves.
def Exercise42():
    import string
    frequencies = {
        "C4": "261.63",
        "D4": "293.66",
        "E4": "329.63",
        "F4": "349.23",
        "G4": "392.00",
        "A4": "440.00",
        "B4": "493.88"
        }
    flag = False
    note=""
    frequency = input("Enter the frequency (upto two decimal places): ") #read as string
    for key,value in frequencies.items():
        if value == frequency:
            note = key
            flag = True
            break;
        elif float(value)-1 <= float(frequency) <= float(value)+1:
            note = key
            flag = True
            break;
        else: flag = False
    if flag == True: print(note)
    else: print("Note not found")

##Exercise 45:What Color is that Square?
##Positions on a chess board are identified by a letter and a number. The letter identifies
##the column, while the number identifies the row, as shown below:
##1
##2
##3
##4
##5
##6
##7
##8
##abcdefgh
##Write a program that reads a position from the user. Use an if statement to deter- mine if the column begins with a black square or a white
##square. Then use modular arithmetic to report the color of the square in that row. For example, if the user enters a1 then your program should
##report that the square is black. If the user enters d5 then your program should report that the square is white. Your program may assume that a
##valid position will always be entered. It does not need to perform any error checking.
def Exercise45():
    import string
    #Board starts with black cell i.e. a1 = black
    blackCols = ('a','c','e','g') #Based on row one
    position = input("Enter cell value (format example: a1): ")
    #Assuming a valid position is entered always
    col = position[:1]
    row = int(position[-1])
    if col in blackCols:
        row1 = "black"
    else: row1 = "white"
    if row%2 == 1: #odd row
        if row1 == "black":
            color = "black"
        else: color = "white"
    else : #even row
        if row1 == "black":
            color = "white"
        else: color = "black"
    print(color)

##Exercise 51: Letter Grade to Grade Points
##At a particular university, letter grades are mapped to grade points in the following manner:
##Letter Grade//points
##A+ greater than 4.0
##A 4.0
##A− 3.7
##B+ 3.3
##B 3.0
##B− 2.7
##C+ 2.3
##C 2.0
##C− 1.7
##D+ 1.3
##D 1.0
##F 0
##Write a program that begins by reading a letter grade from the user. Then your program should compute and display the equivalent number of grade points. Ensure that your program
##generates an appropriate error message if the user enters an invalid letter grade.
def Exercise51():
    grades = {
    "A+": "4.0",
    "A" : "4.0",
    "A-" : "3.7",
    "B+" : "3.3",
    "B" : "3.0",
    "B-" : "2.7",
    "C+" :  "2.3",
    "C" : "2.0",
    "C-" : "1.7",
    "D+" :  "1.3",
    "D" : "1.0",
    "F" : "0"
    }
    grade = input("Enter grade: ")
    if (grade in grades.keys()):
        points = grades.get(grade)
        print(points)
    else: print("Invalid grade")


##Exercise 52: Grade Points to Letter Grade
##In the previous exercise you created a program that converts a letter grade into the equivalent number of grade points. In this exercise you will create a program that
##reverses the process and converts from a grade point value entered by the user to a letter grade. Ensure that your program handles grade point values that fall between
##letter grades. These should be rounded to the closest letter grade. Your program should report A+ for a 4.0 (or greater) grade point average.
def Exercise52():
    import string
    grades = {
        "A" : 4.0,
        "A-" : 3.7,
        "B+" : 3.3,
        "B" : 3.0,
        "B-" : 2.7,
        "C+" :  2.3,
        "C" : 2.0,
        "C-" : 1.7,
        "D+" :  1.3,
        "D" : 1.0,
        "F" : 0
        } # removed A+ as A+ is considered as >4.0 for this program
    gradesKeys = list(grades.keys())
    gradesValues = list(grades.values())
    points = input("Enter points: ")
    pointsF = round(float(points),2)
    #Method1: using multiple if-else statements
    ##if pointsF > 4.0 :
    ##    grade = "A+"
    ##elif pointsF == 4.0:
    ##    grade = "A"
    ##elif pointsF >= 3.7 and pointsF < 4.0:
    ##    grade = "A-"
    ##elif pointsF >= 3.3 and pointsF < 3.7:
    ##    grade = "B+"
    ##elif pointsF >=3.0 and pointsF < 3.3:
    ##    grade = "B"
    ##elif pointsF >= 2.7 and pointsF < 3.0:
    ##    grade = "B-"
    ##elif pointsF >= 2.3 and pointsF < 2.7:
    ##    grade = "C+"
    ##elif pointsF >= 2.0 and pointsF < 2.3:
    ##    grade = "C"
    ##elif pointsF >= 1.7 and pointsF < 2.0:
    ##    grade = "C-"
    ##elif pointsF >= 1.3 and pointsF < 1.7:
    ##    grade = "D+"
    ##elif pointsF >= 1.0 and pointsF < 1.3:
    ##    grade = "D"
    ##elif pointsF >= 0 and pointsF < 1.0:
    ##    grade = "F"
    ##print(grade)
    #Method2: This method works even if grades are modified or more grades are added
    flag = False
    for key,val in grades.items():
        index = gradesKeys.index(key)
        if float(pointsF) > 4.0:
            print("if 4.0")
            grade = "A+"
            print(grade)
            flag = True
            break;
        elif pointsF == float(val):
            print("if equal")
            grade = key
            print(grade)
            flag = True
            break;
    if flag == False:
        for key,val in grades.items():
            index = gradesKeys.index(key)
            if index+1 < len(grades):
                if (float(gradesValues[index]) > pointsF > float(gradesValues[index+1])):
                    grade = gradesKeys[index]
                    print("GRADE",grade)
                    flag = True
                    break;
    if flag == False: print("Invalid ")

