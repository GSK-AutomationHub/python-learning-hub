
# Write a python program using function to convert Celsius to Fahrenheit
# (0°C × 9/5) + 32 = 32°F

def celsius_to_fahrenheit(tempreture):
    resullt = (tempreture * 9/5) + 32
    return resullt

print("Celsius to Fahrenheit conversion: ",celsius_to_fahrenheit(100))