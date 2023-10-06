#covert celcius to fehrenheit using function
#Author- Parth1105
#Date-21/08/23

def farh(cel): #define fehrenheit with inside celcius
    return(cel*(9/5))+32 #formula to convert celcius to fahrenheit
c=67 #temperature in celcius
f=farh(c)
print("fahreheit temperature is "+str(f))
