rural_radiation_list = []
urban_radiation_list = []
rural_radiation_counter = 0
urban_radiation_counter = 0

print('Hello, I will calculate the average amount of radiation for you chosen area.')

location = input('''
Enter Rural or Urban: 
Enter Done when you wish to stop. ''').capitalize()

if location == 'rural'.capitalize():
    try:
        while True:
            radiation_level = int(input("Enter radiation level or done to finish: "))
            rural_radiation_list.append(int(radiation_level))
            rural_radiation_counter += int(radiation_level)
            rural_average = rural_radiation_counter / len(rural_radiation_list)


    except ValueError:
        print("you have input done")
        print(rural_average)


elif location == 'urban'.capitalize():
    try:
        while True:
            radiation_level = int(input("Enter radiation level or done to finish: "))
            urban_radiation_list.append(int(radiation_level))
            urban_radiation_counter += int(radiation_level)
            urban_average = urban_radiation_counter / len(urban_radiation_list)

    except ValueError:
        print("you have input done")
        print(urban_average)

elif location == 'done'.capitalize():
    print('You did not input any values')

else:
    print("Invalid input please try again")


