time = int(input("Enter the amount of minutes: "))

hours1 = float(time/60)
hours2 = int(time/60)
minutes = (hours1 - hours2)*60

print("The amount of hours is: ",hours2)
print("The amount of minutes is: ",minutes)