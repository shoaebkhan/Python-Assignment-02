temp_fah=input("Enter temperature in fahrenheit: ")
temp=int(temp_fah)
temp_cel=(temp-32)*5.0/9.0
print(f"Temperature: {temp_cel.__round__(2)}")