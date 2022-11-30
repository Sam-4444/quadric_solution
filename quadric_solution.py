import math
def main():
    print("This programme finds the real solutions to a quadratic\n")
    try:
        a=float(input("Please enter the coefficient a : "))
        b = float(input("Please enter the coefficient b : "))
        c = float(input("Please enter the coefficient c : "))
        discRoot=math.sqrt(b*b-4*a*c)
        root1=(-b+discRoot)/(2*a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except OverflowError:
        print("\nNo real roots")
    except NameError:
        print("\nYou didn’t enter three numbers.")
    except TypeError:
        print("\nYour inputs were not all numbers.")
    except:
        print("\nSomething went wrong, sorry!")
main()