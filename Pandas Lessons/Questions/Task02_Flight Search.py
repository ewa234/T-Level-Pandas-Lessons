import pandas as pd
import matplotlib.pyplot as plt
 
# Load the flight data from a CSV file
df = pd.read_csv("Data/flights.csv")


while True:
# Get the available dates, departure locations, and destinations
    dates = df.columns.tolist()  # List of available dates in the dataset
    starts = df["From"].unique().tolist()  # List of unique departure locations
    ends = df["To"].unique().tolist()  # List of unique destination locations
    
    while True:
            select_date = input(f"Please select a date between 01/04/22 - 29/06/22: ")
            if select_date in dates:
                break  # Exit the loop if the date is valid
            else:
                print(f"Invalid date. Please select a valid date between 01/04/22 - 29/06/22: ")
    
        # Validate starting location input
    while True:
        select_from = input(f"Please select a starting location from {starts}: ").strip()
        if select_from in starts:
            break  # Exit the loop if the starting location is valid
        else:
            print(f"Invalid starting location. Please choose from: {starts}")
    
    # Validate destination location input
    while True:
        select_to = input(f"Please select a destination from {ends}: ").strip()
        if select_to in ends:
            break  # Exit the loop if the destination location is valid
        else:
            print(f"Invalid destination location. Please choose from: {ends}")
    
    # Validate time input (AM/PM)
    while True:
        select_time = input("Please select AM/PM: ").strip().upper()
        if select_time in ["AM", "PM"]:
            break  # Exit the loop if the time is valid
        else:
            print("Invalid time selection. Please enter 'AM' or 'PM'.")
# Filter the dataframe for the selected date, departure, destination, and time
    df = df[["From", "To", "Time", select_date]]
    print(df)

    flight = df[

                (df["From"].str.contains(select_from, na=False)) &  # Case-insensitive matching for starting location
                (df["To"].str.contains(select_to, na=False)) &   # Case-insensitive matching for destination
                (df["Time"].str.contains(select_time, na=False))  # Case-insensitive matching for AM/PM time
]
   # Display results if there are matching flights
    if not flight.empty:
            print("\nAvailable Flights:")
            print(flight)
    else:
        print("\nNo flights available for the selected criteria.")
 # Ask the user if they want to search for another flight
    again = input("\nSearch for another flight? (yes/no): ").strip().lower()
    if again != "yes":
        break# Exit the loop and stop the program if the user doesn't want to search again

#program brief
#let the user select a date
#let the user select a "From" location
#let the user select a "To" location
#let the user select between AM and PM
#show the user the flights running at the time, on that path
#repeat