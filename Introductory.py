#Exercise 1: Mailing Address
#Create a program that displays your name and complete mailing address formatted in the manner that you would usually see it on the outside of an envelope. Your program
#does not need to read any input from the user
def Exercise1():
    name = 'Sai'
    address = {'unit' : 44,
     'street': '138 Cherry Road',
     'city': 'Toronto',
     'province': 'Ontario',
     'Zip code': 'n9z2x3'
               }
    print(name, '\n', address['unit'],',', address['street'],'\n',address['city'],',',address['province'],',',address['Zip code'])

#Exercise 2: Hello
#Write a program that asks the user to enter his or her name. The program should respond with a message that says hello to the user, using his or her name
def Exercise2():
    name = input("Enter your name:")
    print("Hello,"+name+"!")

#Exercise 3: Area of a Room
#Write a program that asks the user to enter the width and length of a room. Once the values have been read, your program should compute and display the area of the
#room. The length and the width will be entered as floating point numbers. Include units in your prompt and output message; either feet or meters, depending on which
#unit you are more comfortable working with
def Exercise3():
    width = float(input("Enter width of the room in meters:"))
    length = float(input("Enter length of the room in meters:"))
    print("Area of the room is",length*width,"square meters")


#Exercise 4: Area of a Field
#Create a program that reads the length and width of a farmer’s field from the user in
#feet. Display the area of the field in acres.
#Hint: There are 43,560 square feet in an acre.
def Exercise4():
    length = float(input("Enter length of the field in feet:"))
    width = float(input("Enter width of the field in feet:"))
    print("Area of the field is",(length*width)/43560,"acres")


#Exercise 5: Bottle Deposits
#In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or
#less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit. Write a program that reads the number of containers of each size from the user.
#Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar
#sign and always displays exactly two decimal places.
def Exercise5():
    lessliter_deposit = 0.10
    moreliter_deposit = 0.25
    lessliter = 0
    moreliter = 0
    bool_flag = input("Do you have bottles of capacity 1 liter or less (yes/no):")
    if bool_flag == 'yes':
        lessliter = int(input("Enter number of bottles of 1 liter or less:"))
    bool_flag = input("Do you have bottles of capacity of more than 1 liter (yes/no):")
    if bool_flag == 'yes':
        moreliter = int(input("Enter number of bottles of more than 1 liter:"))
    refund = (lessliter * lessliter_deposit) + (moreliter * moreliter_deposit)
    print("You have a refund of "+"$"+format(refund,'.2f'))


#Exercise 6: Tax and Tip
#The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and
#tip for the meal. Use your local tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from
#your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values
#are displayed using two decimal places.
def Exercise6() :
    tax_rate = 0.12 #12%
    tip_rate = 0.18 #18%
    cost_meal = float(input("Enter the cost of the meal:"))
    tax = cost_meal * tax_rate
    tip = cost_meal * tip_rate
    grand_total = cost_meal + tax + tip
    print("Tax:"+"$"+format(tax,'.2f'),'\n'+"Tip:"+"$"+format(tip,'.2f'),'\n'+"Grand Total:"+"$"+format(grand_total,'.2f'))


#Exercise 7: Sum of the First n Positive Integers
#Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers can be
#computed using the formula: sum = ((n)(n + 1))/2
def Exercise7():
    num = int(input("Enter a positive integer:"))
    while num <= 0 :
        num = int(input("Only positive integers accepted. Please enter a positive integer:"))
    sum = int((num * (num+1))/2)
    print("Sum of integers from 1 to",num,"is",sum)

#Exercise 8: Widgets and Gizmos
#An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number of
#widgets and the number of gizmos in an order from the user. Then your program should compute and display the total weight of the order.
def Exercise8():
    weight_widget = 75 #grams
    weight_gizmo = 112 #grams
    num_widget = int(input("Enter the number of widgets:"))
    while num_widget < 0 :
        num_widget = int(input("Only positive integers accepted. Please enter a positive integer:"))
    num_gizmo = int(input("Enter the number of gizmos:"))
    while num_gizmo < 0 :
        num_gizmo = int(input("Only positive integers accepted. Please enter a positive integer:"))
    Total_weight = (num_gizmo * weight_gizmo) + (num_widget * weight_widget)
    print("Total weight of the order is",Total_weight,"grams")

#Exercise 9: Compound Interest
#Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and
#is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your
#program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places.
def Exercise9():
    deposit = float(input('Enter the amount deposited:'))
    counter = 0
    while (counter < 3):
        interest = 0.04 * deposit
        deposit = deposit + interest
        print("Amount at the end of year",counter+1,"is",format(deposit,'.2f'))
        counter = counter+1


#Exercise 10: Arithmetic
#Create a program that reads two integers, a and b, from the user. Your program should compute and display:
#• The sum of a and b
#• The difference when b is subtracted from a
#• The product of a and b
#• The quotient when a is divided by b
#• The remainder when a is divided by b
#• The result of log a base 10
#• The result of a power b
def Exercise10():
    import math as m
    a = int(input("Enter first integer a:"))
    b = int(input("Enter second integer b:"))
    sum = a+b
    print("Sum of a and b is",sum)
    diff = a-b
    print("Difference of a and b is",diff)
    prod = a*b
    print("Product of a and b is",prod)
    quot = a/b
    print("Quotient when a is divided by b is",quot)
    rema = a%b
    print("Remainder when a is divided by b is",rema)
    log_val = m.log(a,10)
    print("The result of log a base 10 is",log_val)
    exp = a**b
    print("The result of a power b is",exp)


#Exercise 11: Fuel Efficiency
#In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
#kilometers (L/100 km). Use your research skills to determine how to convert from MPG to L/100 km. Then create a program that reads a value from the user in American
#units and displays the equivalent fuel efficiency in Canadian units.
    def Exercise11():
        american_fueleff = float(input("Enter fuel efficiency in MPG:"))
        canadian_fueleff = 235.21/american_fueleff
        print("Fuel efficiency in Canadian units is",canadian_fueleff,"L/100km")
    

#Exercise 12: Distance Between Two Points on Earth
#The surface of the Earth is curved, and the distance between degrees of longitude varies with latitude. As a result, finding the distance between two points on the surface
#of the Earth is more complicated than simply using the Pythagorean theorem. Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
#surface. The distance between these points, following the surface of the Earth, in kilometers is: distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
#The value 6371.01 in the previous equation wasn’t selected at random. It is the average radius of the Earth in kilometers. Create a program that allows the user to enter the latitude
#and longitude of two points on the Earth in degrees. Your program should display the distance between the points, following the surface of the earth, in kilometers.
#Hint: Python’s trigonometric functions operate in radians. As a result, you will need to convert the user’s input from degrees to radians before computing the
#distance with the formula discussed previously. The math module contains a function named radians which converts from degrees to radians.
def Exercise12():
    import math as m
    lat1 = float(input("Enter latitude of point1 in degrees:"))
    lat1 = m.radians(lat1)
    log1 = float(input("Enter longitude of point1 in degrees:"))
    log1 = m.radians(log1)
    lat2 = float(input("Enter latitude of point2 in degrees:"))
    lat2 = m.radians(lat2)
    log2 = float(input("Enter longitude of point2 in degrees:"))
    log2 = m.radians(log2)
    # distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
    sin_val = m.sin(lat1)*m.sin(lat2)
    cos_val = m.cos(lat1)*m.acos(lat2)*m.cos(log1-log2)
    distance = 6371.01 * m.acos(sin_val + cos_val)
    print("The distance between the points, following the surface of the earth, in kilometers is",distance)


#Exercise 13: Making Change
#Consider the software that runs on a self-checkout machine. One task that it must be able to perform is to determine how much change to provide when the
#shopper pays for a purchase with cash. Write a program that begins by reading a number of cents from the user as an
#integer. Then your program should compute and display the denominations of the coins that should be used to give that amount of change to the shopper. The change
#should be given using as few coins as possible. Assume that the machine is loaded with pennies, nickels, dimes, quarters, loonies and toonies.
#A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie because one side of the coin has a loon (a type of bird) on it. The two
#dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is derived from the combination of the number two and the name of the loonie.
def Exercise13():
    cents = int(input("Enter change you need in cents:"))
    #all values below in cents
    penny = 1
    nickel = 5
    dime = 10
    quarter = 25
    loonie = 100
    toonie = 200
    num_toonie = cents//toonie #Using integer division as number of coins can be only an integer
    cents = cents%toonie
    print("Number of Toonies:",num_toonie)
    num_loonie = cents//loonie
    cents = cents%loonie
    print("Number of Loonies:",num_loonie)
    num_quarter = cents//quarter
    cents = cents%quarter
    print("Number of Quarters:",num_quarter)
    num_dime = cents//dime
    cents = cents%dime
    print("Number of Dimes:",num_dime)
    num_nickel = cents//nickel
    cents = cents%nickel
    print("Number of Nickels:",num_nickel)
    num_penny = cents//penny
    cents = cents%penny
    print("Number of pennies:",num_penny)


#Exercise 14: Height Units
#Many people think about their height in feet and inches, even in some countries that primarily use the metric system. Write a program that reads a number of feet from
#the user, followed by a number of inches. Once these values are read, your program should compute and display the equivalent number of centimeters.
#Hint: One foot is 12 inches. One inch is 2.54 centimeters.
def Exercise14():
    num_feet = int(input("Enter the feet:"))
    num_inch = int(input("Enter the inches:"))
    #One foot is 12 inches. One inch is 2.54 centimeters.
    height_cm = ((num_feet*12)+ num_inch)*2.54
    print("Height in cm:",height_cm)

#Exercise 15: Distance Units
#In this exercise, you will create a program that begins by reading a measurement in feet from the user. Then your program should display the equivalent distance in
#inches, yards and miles. Use the Internet to look up the necessary conversion factors if you don’t have them memorized.
def Exercise15():
    num_feet = int(input("Enter the feet:"))
    #One foot is 12 inches
    num_inch = num_feet*12
    print("Inches:",num_inch)
    #One foot is 1/3 yard
    num_yard = num_feet/3
    print("Yards:",num_yard)
    num_mile = num_feet/5280
    print("Miles:",num_mile)

#Exercise 16: Area and Volume
#Write a program that begins by reading a radius, r, from the user. The program will continue by computing and displaying the area of a circle with radius r and the
#volume of a sphere with radius r. Use the pi constant in the math module in your calculations.
#Hint: The area of a circle is computed using the formula area = πrpower2. The volume of a sphere is computed using the formula volume = (4/3)πrpower3.
def Exercise16():
    import math as m
    radius = float(input("Enter the radius:"))
    areaCircle = m.pi*pow(radius,2)
    volSphere = (4/3)*m.pi*m.pow(radius,3)
    print("Area of circle",areaCircle)
    print("Volume of Sphere",volSphere)
    

#Exercise 17: Heat Capacity
#The amount of energy required to increase the temperature of one gram of a material by one degree Celsius is the material’s specific heat capacity, C. The total amount
#of energy required to raise m grams of a material by ΔT degrees Celsius can be computed using the formula: q = mCΔT. Write a program that reads the mass of some water
#and the temperature change from the user. Your program should display the total amount of energy that must be added or removed to achieve the desired temperature change.
#Hint: The specific heat capacity of water is 4.186 J/g◦C. Because water has a density of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
#in this exercise. Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
#exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use your program to compute the cost of boiling water for a cup of coffee.
def Exercise17():
    SH_Water = 4.186 #Joules/gram degrees Celcius
    unitElectricity = 8.9 #cents per KW-hour
    energyJ = 0 #Joules
    def computeEnergy(mass,temp):
        energyJ = mass * SH_Water * temp
        return energyJ
    def computeCost(energyJ):
        energyKW = energyJ * 2.777
        cost = energyKW * unitElectricity #cents
        return cost
    mass = float(input("Enter mass of water in grams: "))
    temp = float(input("Enter temperature you want to change in celcius degrees: "))
    energyJ = computeEnergy(mass,temp)
    print("Energy required to achieve mentioned temperature change: ",energyJ,"Joules")
    cost = computeCost(energyJ)
    print("Cost of heating/cooling the water to achieve mentioned temperature change: ",format(cost,'.2f'),"cents")
    #Cost of boiling water for a cup of coffee
    energyJ = computeEnergy(237,100) # considering 1 cup of water = 237 grams and boiling point of water = 100 degrees celcius
    cost = computeCost(energyJ)
    print("Cost of boiling water for a cup of coffee:",format(cost,'.2f'),"cents")


#Exercise 18:Volume of a Cylinder
#The volume of a cylinder can be computed by multiplying the area of its circular base by its height. Write a program that reads the radius of the cylinder, along with
#its height, from the user and computes its volume. Display the result rounded to one decimal place.
def Exercise18():
    import math as m
    radius = float(input("Enter radius of the cylinder:"))
    height = float(input("Enter height of the cylinder:"))
    volume = 2 * m.pi * radius * height
    print("Volume of the cylinder:",format(volume,'.1f'))
               

#Exercise 19: Free Fall
#Create a program that determines how quickly an object is traveling when it hits the ground. The user will enter the height from which the object is dropped in meters (m).
#Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration due to gravity is 9.8 m/s2. You can use the formula vf = sqrt(vi pow 2 + 2ad) to compute the
#final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
def Exercise19():
    import math as m
    height = float(input("Enter the height from which the object is dropped in meters:"))
    gravity = 9.8 #m/sq sec
    initialSpeed = 0 #m/s
    finalSpeed = m.sqrt(pow(initialSpeed,2) + (2 * gravity * height))
    print("Final speed is:",finalSpeed,"metres per second")

#Exercise 20: Ideal Gas Law
#The ideal gas law is a mathematical approximation of the behavior of gasses as pressure, volume and temperature change. It is usually stated as: PV = nRT
#where P is the pressure in Pascals, V is the volume in liters, n is the amount of substance in moles, R is the ideal gas constant, equal to 8.314 J mol K , and
#T is the temperature in degrees Kelvin. Write a program that computes the amount of gas in moles when the user supplies the pressure, volume and temperature.
#Test your program by determining the number of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at a pressure of 20,000,000 Pascals (approximately 3,000 PSI).
#Room temperature is approximately 20 degrees Celsius or 68 degrees Fahrenheit. Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
#to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it, multiply it by 5/9 and then add 273.15 to it.
def Exercise20():
    RConst = 8.314 #Joules per mole per kelvin
    press = float(input("Enter pressure in pascals:"))
    vol = float(input("Enter volume in liters:"))
    temp = float(input("Enter temperature in Kelvin:"))
    amountGas = (press * vol)/(RConst * temp)
    print("Amount of Gas:",amountGas,"moles")
    ScubaVol = 12 #litres
    ScubaPress = 20000000 #pascals
    RoomTemp = ((68 - 32)*(5/9))+273.15 #Room temp is 68 Fahrenheit. Converted to Kelvin
    ScubaGas ==(ScubaPress * ScubaVol)/(RConst * RoomTemp)
    print("Amount of Gas in Scuba tank:",ScubaGas)

#Exercise 31: Sum of the Digits in an Integer
#Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number. For example, if the user enters 3141 then your program
#should display 3+1+4+1=9.
def Exercise31() :
    num = input("Enter a positive integer:")
    num = int(num)
    sum = 0
    while num>=1 :
        rem = num%10
        sum=sum+rem
        num = num//10
        print("Sum of digits:",sum)

#Exercise 32: Sort 3 Integers
#Create a program that reads three integers from the user and displays them in sorted order (from smallest to largest). Use the min and max functions to find the smallest
#and largest values. The middle value can be found by computing the sum of all three values, and then subtracting the minimum value and the maximum value.
def Exercise32():
    num1 = int(input("Enter first integer:"))
    num2 = int(input("Enter second integer:"))
    num3 = int(input("Enter third integer:"))
    min_num = min(num1,num2,num3)
    max_num = max(num1,num2,num3)
    other_num = 0
    if num1 == min_num or num1 == max_num:
        if num2 == min_num or num2 == max_num:
            other_num = num3
        elif num3 == min_num or num3 == max_num:
            other_num = num2
    else:
        other_num = num1
    print("Smallest to largest are:",min_num,other_num,max_num)

#Exercise 33: Day Old Bread
#A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60 percent. Write a program that begins by reading the number of loaves of day old
#bread being purchased from the user. Then your program should display the regular price for the bread, the discount because it is a day old, and the total price. All of the
#values should be displayed using two decimal places, and the decimal points in all of the numbers should be aligned when reasonable values are entered by the user.
def Exercise22 ():
    discount = 0.60
    regPrice = 3.49
    numLoaves = int(input("Enter the number of loaves of one day old:"))
    discPrice = discount * regPrice
    TotalPrice = numLoaves * discPrice
    print("Regular Price for the bread:",format(regPrice,'.2f'))
    print("Discounted Price for the bread:",format(discPrice,'.2f'))
    print("Total Price:",format(TotalPrice,'.2f'))
   

    
