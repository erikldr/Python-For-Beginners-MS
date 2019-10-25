#Be careful when comparing strings
country = input('Enter the name of your home country: ')

if country.lower()=='brazil':
    print('So you most like football!')
else:
    print('You are not from Brazil')

#Another compare
price = input('how much did you pay? ')

price = float(price)
if price >= 1.00:
    tax = .07
else:
    tax = 0

print('Tax rate is: ' + str(tax))

