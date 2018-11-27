#Author: Ronni Kurtzhals
#Date: 12/4/18
#Class: CSIS 152
#Instructor: Dr. Brekke
#Assignment: Program 13
import string
import math

def main():
    print("Enter two fractions to find their sum, difference, product, and quotient.")
    fraction1 = input("Enter your first fraction: ")
    fraction2 = input("Enter your second fraction: ")
    str_int(fraction1)
    str_int(fraction2)
    print(add_fr(5,6,2,3))
    print(sub_fr(5,6,2,3))
    print(mult_fr(5,6,2,3))
    print(div_fr(5,6,2,3))
    
def lcm(a,b):
    if a < b:
        lcm = a
    else:
        lcm = b
    while (lcm % a != 0 or lcm % b != 0):
            lcm += 1
    return lcm

def str_int(a):
    numerator = int(a[:a.index("/")])
    denominator = int(a[a.index("/")+1:])
    return numerator,denominator

def gcd(a,b):
    gcd = math.gcd(a,b)
    return gcd

def add_fr(n1,d1,n2,d2):
    n1 = n1*lcm(d1,d2)//d1
    n2 = n2*lcm(d1,d2)//d2
    n3 = n1+n2
    d3 = lcm(d1,d2)
    result = str(n3//gcd(n3,d3))+"/"+str(d3//gcd(n3,d3))
    return result

def sub_fr(n1,d1,n2,d2):
    n1 = n1*lcm(d1,d2)//d1
    n2 = n2*lcm(d1,d2)//d2
    n3 = n1-n2
    d3 = lcm(d1,d2)
    result = str(n3//gcd(n3,d3))+"/"+str(d3//gcd(n3,d3))
    return result

def mult_fr(n1,d1,n2,d2):
    n3 = n1*n2
    d3 = d1*d2
    result = str(n3//gcd(n3,d3))+"/"+str(d3//gcd(n3,d3))
    return result

def div_fr(n1,d1,n2,d2):
    n3 = n1*d2
    d3 = n2*d1
    result = str(n3//gcd(n3,d3))+"/"+str(d3//gcd(n3,d3))
    return result

main()
