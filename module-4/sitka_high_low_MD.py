import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
        # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
#creating a menu that let the user decide what he wants to see: high temps, low temps, or exit
while True:
    print("\nSITKA WEATHER MENU")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")
    # Get the user's choice.
    choice = input("Enter your choice: ")
    # Process the user's choice by displaying high temperatures.
    if choice == "1":
        print("Displaying high temperatures")
        # Plot the high temperatures.
        # plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    # Process the user's choice by displaying low temperatures.
    elif choice == "2":
        print("Displaying low temperatures")
        # Plot the low temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    # Process the user's choice by exiting the menu.
    elif choice == "3":
        print("Thanks for using Sitka Weather Menu")
        break
    # Process the user's choice by displaying an error message for invalid choices.
    else:
        print("Invalid choice. Please try again.")
