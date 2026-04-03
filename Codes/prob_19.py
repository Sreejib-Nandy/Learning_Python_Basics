def celciustofahrenheit(num):
    fahrenheit = ((num * 9)/5) + 32
    return str(fahrenheit) + " F"

temperature = int(input("Enter the temperature in celcius : "))
print(f"The temperature in fahrenheit is : {celciustofahrenheit(temperature)}")