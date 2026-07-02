"""
Amount = P(1 + R/100) ** T
ci = Amount - P
"""
principal = float(input("Enter the principal amount: "))
Rate = float(input("Enter the rate of intrest: "))
Time = float(input("Enter the time duration of intrest: "))
#Amount = principal * (1 + Rate/100) ** Time
Amount2 = principal * pow((1 + Rate/100), Time)
print(round(Amount2 , 2))
ci = Amount2 - principal
print("Compound Intrest is" , ci)
