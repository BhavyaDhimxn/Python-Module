def siCal(p, r, t):
    
    si = (p * r * t) / 100
    
    return si

def inputPRT():

    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time in years: "))

    return p, r, t

while True:
    p, r, t = inputPRT()

    simple_interest = siCal(p, r, t)
    
    print(f"The Simple Interest is: {simple_interest}")

    calculate_again = input("Do you want to calculate again? (yes/no): ")

    if calculate_again != 'yes':
        break

