# Data validation for data that needs to fall within a range
temperature = int(input("Enter temperature in Centigrade: "))

if temperature >= -273:
    print("The temperature: " + str(temperature))
else:
    print("ERROR:  you must enter a temperature above absolute zero.")


