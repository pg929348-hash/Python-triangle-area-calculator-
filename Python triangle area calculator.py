while True:
    import math
    print(" *** calculating area of triangle usingheron's formula ***")
    a=int( input(" enter the first side measure:-"))
    b=int( input(" enter the second side measure:-"))
    c=int( input(" enter the third  side measure:-"))
    if (a+b>c)and (a+c>b)and(b+c>a):
        s= (a+b+c)/2
        A=s*(s-a)*(s-b)*(s-c)
        area=  math.sqrt (A)
        print(f" { area:.2f}")
    else:
        print (" triangle cannot form")
