# This function calculate Miles per gallon
# parameters:  number_of_miles,number_of_gallons
def caculateMpg(number_of_miles,number_of_gallons):
    mpg = number_of_miles / number_of_gallons
    return mpg


# This function calculate area of circle
# parameters: radius
import math
def calculateAreaOfCircle(radius):
    return math.pi * radius ** 2


# This function converts fahrenheit to celsius
# parameters: fahrenheit
def convertFahrenheitToCelsius(fahrenheit):
     return (fahrenheit-32)/1.8


# This function calculates distance between two points
# parameters: x, x1, y, y1
def calculateDistanceBetweenPoints (x,y,x1,y1):
    a = x - x1;
    b = y - y1;
    d = (a**2 + b**2)**.5
    return d
