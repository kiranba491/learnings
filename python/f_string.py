from datetime import datetime


if __name__ == "__main__":
    print(f"{1234.5647:.2f}")   #Round the float number to lowerbound
    print(f"{1234.5656:.2f}")   #Round the float number to upperbound
    print(f"{1000000.0:,.0f}")  #Add separates for big number representation
    print(f"{1000000.0:e}")     #Exponential number representation

    a, b = 10, 20
    print(f"{a + b = }")    #Debugger statement

    name: str = "Kiran"
    print(name)
    print(f"{name}")        #Simple string print
    print(f"{name:20}|")    #String Padding(left)
    print(f"{name:<20}|")   #Same as above default case.
    print(f"{name:*<20}")   #String padding with fill
    print(f"{name:>20}")    #String Padding(right)
    print(f"{name:*>20}")   #String padding with fill.
    print(f"{name:^20}")    #String padding(center)
    print(f"{name:*^20}")   #String padding with fill
    print(f"{name = }")     #Debugger statement for string
    print(f"{name = !s}")   #Debugger statement with string
    print(f"{name = !a}")   #Debugger statement with ASCII
    print(f"{name = !r}")   #Debugger statement with pyhton object representation

    current_datetime: datetime = datetime.now()
    print(current_datetime)
    print(f"{current_datetime}")            #Simple date and time print
    print(f"{current_datetime = }")         #Datetime with debugger statement
    print(f"{current_datetime = !s}")       #Datetime debugger statement with string
    print(f"{current_datetime = !a}")       #Datetime debugger statement with ASCII
    print(f"{current_datetime = !r}")       #Datetime debugger statement with python object representation
    print(f"{current_datetime:%Y-%m-%d}")   #Datetime with format
