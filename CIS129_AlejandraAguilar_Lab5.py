#Alejandra Aguilar
#March 4, 2025
#CIS129 Module 5 Lab

#This program allows the user to track the number of bottles returned over a seven day period

#Lab 5 The Bottle Return Program

payout_per_bottle = .10
keep_going = 'y' #set to 'y' so while-loop will start initial run


while keep_going == 'y': #This loop controls whether data will be collected
    total_bottles = 0   #These variables should start out at or reset to 0 or initial number for each week
    today_bottles = 0
    total_payout = 0
    counter = 1
    number_of_days = 7
    while counter <= number_of_days:  #This loop requests data from user for each day
        today_bottles = int(input(f'Enter number of bottles for day #{counter}:'))
        total_bottles = total_bottles + today_bottles
        counter += 1 #increase counter by 1 in each iteration so input is asking for different day each time
    total_payout = total_bottles * payout_per_bottle
    print("The total number of bottles collected is", total_bottles)
    print(f'The total paid out is ${total_payout:.2f}') #formatted string since printing dollar amounts
    print("Do you want to enter another week's worth of data?")
    keep_going = input("(Enter y or n):")
