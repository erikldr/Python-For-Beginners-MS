x = 5
y = 0

try:
    print(x / y)
except ZeroDivisionError as e:
    #Optionally, log e somewhere
    print('Not allowed to divide by zero')
except:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
    
