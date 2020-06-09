
'''
4)The Temperature Converter
'''

def celsiusToFahrenheit(c):
    return (c * 9/5) + 32
c = int(input("enter celsius value : "))
f = celsiusToFahrenheit(c)
print(c,'°C', "is" ,f,'°F')

def fahrenheitToCelsius(f):
    return 5*(f - 32)/9
f = int(input("enter fahrenheite value : "))
c = fahrenheitToCelsius(f)
print(f,'°F', "is" ,round(c,2),'°C')
