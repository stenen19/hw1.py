def greeting():
    capture = input("What's your name? ");
    print("Hello %s"%capture );


def greeting1() :
    capture = input ( "name:" );
    print( "Hello ", capture );


def number():
    number = input("enter any real number ");
    numberint = int(number);
    print("Your number is " + number )


def average():
    first = input("enter your first number ");
    firstint= float(first);
    second = input("enter your second number ");
    secondint= float(second);
    third = input("enter your third number ");
    thirdint= float(third);
    average = ((first+second+third)/3);
    print("the average is ", average)
    

def graduate():
    gradyear = input("What's your class year? ");
    gradyearint = int(gradyear);
    yearstogo = gradyearint - 2019;
    print("You will graduate from USNA in", yearstogo, "years" );


def sphere( radius ):
    A = (4*3.14)*(radius**2);
    V = (4/3)*(3.14)*(radius**3);
    print ( "Surface area is", A," and volume is", V);
    

def feet( inches ):
    feet = inches // 12;
    rem = inches %12 ;
    print( feet, " feet ", rem, " inches" );

    

def packet ( bits_in_file, bits_in_packet ):
    num_full_packets = bits_in_file // bits_in_packet
    rem_bits = bits_in_file % bits_in_packet
    print( num_full_packets, " packets and ", rem_bits, " bits" );

def rect_base( length, width ):
    area = length * width
    return area

def pyramid ( length, width, height ):
    volume = rect_base ( length, width ) * ( height );
    return volume







