date = input('Enter the desired date (e.g. 04/07/2006): ').split('/')
hemisphere = input('Enter the hemisphere (S = south / N = north): ').upper()

day = int(date[0])
month = int(date[1])

if hemisphere == 'S' or hemisphere == 'SOUTH':
    if (month == 9 and day >= 22) or (month > 9 and month < 12) or (month == 12 and day <= 21):
        print('Spring!')
    elif (month == 12 and day >= 22) or (month < 3) or (month == 3 and day <= 21): 
        print('Summer!')
    elif (month == 3 and day >= 22) or (month > 3 and month < 6) or (month == 6 and day <= 21):
        print('Autumn!')
    elif (month == 6 and day >= 22) or (month > 6 and month < 9) or (month == 9 and day <= 21):
        print('Winter!')
    else:
        print("You didn't type the date correctly.\nTry again.\n")
elif hemisphere == 'N' or hemisphere == 'NORTH':
    if (month == 9 and day >= 22) or (month > 9 and month < 12) or (month == 12 and day <= 21):
        print('Autumn!')
    elif (month == 12 and day >= 22) or (month < 3) or (month == 3 and day <= 21): 
        print('Winter!')
    elif (month == 3 and day >= 22) or (month > 3 and month < 6) or (month == 6 and day <= 21):
        print('Spring!')
    elif (month == 6 and day >= 22) or (month > 6 and month < 9) or (month == 9 and day <= 21):
        print('Summer!')
    else:
        print("You didn't type the date correctly.\nTry again.\n")
else:
    print("You didn't type the hemisphere correctly.\nTry again.\n")
