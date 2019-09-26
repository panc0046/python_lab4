from panc0046Library import *

# Calculayte Miles per gallon
print ("***** Calculate Miles per gallon ******")
number_of_miles = float(input("Enter number of miles you have driven"))
number_of_gallons = float(input("Enter number of gallons used"))
# call function to calculate mpg
mpg = caculateMpg(number_of_miles,number_of_gallons)
print ("Miles per Gallon of your car is : " + str(mpg) + " mpg")


# Calculate area of circle
print("***** Calculate area of circle ******")
radius = int(input("Enter the radius"))
# Call function
area_circle = calculateAreaOfCircle(radius)
print (area_circle)

# Convert Fahrenheit To Celsius
print ("***** Convert Fahrenheit To Celsius *****")
fahrenheit = float(input("Enter temperature of fahrenheit"))
# Call function
celsius = convertFahrenheitToCelsius(fahrenheit)
print ("Temperature in Celsius: " + str(celsius))


# Calculate distance between two points
print ("***** Calculate distance between two points *****")
x = int(input("Enter value of x"))
y = int(input("Enter value of y"))
x1 = int(input("Enter value of x1"))
y1 = int(input("Enter value of y1"))
d = calculateDistanceBetweenPoints(x,y,x1,y1)
print ("Distance between two points is: " + str(d))
