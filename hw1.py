from math import sqrt
def greeting():
    capture = input("What's your name? ")
    print("Hello %s " % capture)

def number():
    number = input("enter any real number ")
    numberint = int(number)
    print("Your number is", numberint )

def average():
    first = input("enter your first number ")
    firstint = float(first)
    second = input("enter your second number ")
    secondint = float(second)
    third = input("enter your third number ")
    thirdint = float(third)
    average = ((firstint+secondint+thirdint)/3)
    print("the average is", average)
    
def graduate():
    gradyear = input("What's your class year? ")
    gradyearint = int(gradyear)
    yearstogo = gradyearint - 2019
    print("You will graduate from USNA in", yearstogo, "years" )

def sphere( radius ):
    A = (4*3.14)*(radius**2)
    V = (4/3)*(3.14)*(radius**3)
    print( "Surface area is", A," and volume is", V)

#Professor Casey, why is the remainder not calculating correctly?
def division(divisor, dividend):
    divisor = float(divisor)
    dividend = float(dividend)
    quotient = 0
    count = 0
    while dividend >= divisor: 
        dividend -= divisor
        quotient += 1 
        count += 1
        remainder = dividend - (divisor * count) 
    print("Quotient is" ,quotient, "and remainder is" ,remainder)

# Professor Casey, same problem as with previous example
#def division_alt (): 

def triangle():
    length = input("length of one leg of an isocleles right triangle: ")
    length = float(length)
    hypotenuse = sqrt(2 * (length ** 2))
    print("The length of the hypotenuse is",hypotenuse)
"""
def feet( inches ):
    feet = inches // 12
    rem = inches % 12 
    print( feet, "feet", rem, "inches" )
    
def packets ( bits_in_file, bits_in_packet ):
    num_full_packets = bits_in_file // bits_in_packet
    rem_bits = bits_in_file % bits_in_packet
    print( num_full_packets, " packets and ", rem_bits, " bits" )

def rect_base( length, width ):
    area = length * width
    return area

def pyramid ( length, width, height ):
    volume = rect_base ( length, width ) * ( height )
    return volume

"""
#greeting()j
#number()
#average()
#graduate()
#sphere( 32 )
#feet(72)
#division (4,11)
#division_alt (4,3)
#triangle()
