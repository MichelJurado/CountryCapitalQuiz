# Create a program that contains a dictionary containing 20 countries as keys and their capitals as values. ( Use the Internet if needed)
# The program is to randomly quiz the user by displaying a country's name and ask user to enter the country's capital. 
# The program is to verify user's entry , if correct , program is to congratulate user and display another countries name. Use sentinel to allow the user to exit the program if they choose to.
#  The program should keep count of  the number of correct and incorrect responses and display results when user chooses to stop playing
# 9/22/21
# CTI-110 M4Pro – Country Capitals
# Michel Jurado

#create a dictionary with 20 countries
#import random
#output the country name and wait for capital as input
#if input is correct congradulate user and display another country.
#use a sentinel to allow user to exit program if they choose
#add total of number correct and incorrect and display once user stops.

import random
totalincorrect = 0
totalcorrect = 0

#create dictionary
countries = {'cuba':'havana',
            'canada':'ottawa',
            'columbia':'bogota',
            'egypt':'cairo',
            'el salvador':'san salvador',
            'fiji':'suva',
            'france':'paris',
            'india':'new delhi',
            'indonesia':'jakarta',
            'iran': 'tehran',
            'iraq': 'baghdad',
            'ireland': 'dublin',
            'israel': 'jerusalem',
            'italy': 'rome',
            'jamaica': 'kingston',
            'japan':'tokyo',
            'united states':'washington d.c',
            'zambia':'lusaka',
            'ukraine':'kiev',
            'sweden':'stockholm'}


stop = 0
#start a loop
while stop != 1:
    
    country = list(countries.keys())
    x = random.choice(country)
    print(f'What is the capital of {x}')
    y = str(x)
    capital = str(input("Enter answer in lowercase: "))
    if countries[y] == capital:
        print("Correct!")
        correct=1
        totalcorrect += correct
    else:
        print("Incorrect!")
        incorrect=1
        totalincorrect += incorrect
    stop = int(input("Press 1 to quit or any other number to continue: "))
#terminates and prints total
print(f'Total correct: {totalcorrect}')
print(f'Total incorrect: {totalincorrect}')