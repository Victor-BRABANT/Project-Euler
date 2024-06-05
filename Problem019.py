nb_sundays = 0

week_day_n = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
month_n = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juiller", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]

week_day = 2
day = 1
month = 1
year = 1901

def is_bissex(y):
	return (y%4 == 0) and (y%400 == 0 or y%100 != 0)

while (year != 2001):

	print(week_day_n[week_day-1],day,month_n[month-1], year)

	if (week_day == 7 and day == 1):
		nb_sundays += 1
	week_day += 1
	if (week_day == 8):
		week_day = 1
	day += 1
	if (month in (1,3,5,7,8,10,12)):
		if (day == 32):
			day = 1
			month += 1
			if (month == 13):
				month = 1
				year += 1
	elif (month != 2):
		if (day == 31):
			day = 1
			month += 1
	else:
		if (is_bissex(year)):
			if (day == 30):
				day = 1
				month += 1
		elif (day == 29):
			day = 1
			month += 1

print(nb_sundays)