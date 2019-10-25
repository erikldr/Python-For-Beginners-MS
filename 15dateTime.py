#To get current date and time
#We need to use the datetime library
from datetime import datetime, timedelta #da biblioteca datetime me dê o datetime
#timedelta faz operações com datas

today = datetime.now()
#the now function returns a datetime object
print('Today is : ' + str(today))

#timedelta is used to define a period of time
one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))


one_day = timedelta(days=1)
yesterday = today - one_day
#print('Yesterday was: ' + str(yesterday))
print()

#print('Hour: ' + str(today.hour))
#print('Minutes: ' + str(today.minute))
#print('Day: ' + str(today.day))
#print('Month: ' + str(today.month))
#print('Year: ' + str(today.year))

birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: ' + str(birthday))

one_day = timedelta(days=1)
birthday_eve = birthday - one_day

print('Day before birthday: ' + str(birthday_eve))