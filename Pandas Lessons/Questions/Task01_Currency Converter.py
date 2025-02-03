from ast import Try
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("Data/currency.csv")

print(df)

#write a program that:
#   lets the user enter a date
#   validates the date input
#   lets the user enter a currency conversion
#   validates the currency input
#   shows the user their chosen conversion rate
#       on their chosen day
#   repeats
 
 
earliest = "18/12/2020"
latest = "16/03/2021"
conversions = ["GBP - EUR","EUR - GBP","GBP - AUD",
               "AUD - GBP","GBP - JPY","JPY - GBP"]
def validate_date(date_text):
    try:
        date_obj = datetime.strptime(date_text, "%d/%m/%Y")
        earliest_date = datetime.strptime(earliest, "%d/%m/%Y")
        latest_date = datetime.strptime(latest, "%d/%m/%Y")
        return earliest_date <= date_obj <= latest_date
    except ValueError:
        return False

while True:
    dateInput = input(f"enter a date between {earliest} and {latest}/ must be in the format 'DD/MM/YYYY' ")
    if not validate_date(dateInput):
        print("Invalid date or date out of range. Please try again.")
        continue
    
    print("here are the options")
    for index in range (len(conversions)):
        print(f"{index}:{conversions[index]}")
    
    try:
        choice = int(input("enter your choice"))
        if choice < 0 or choice >= len(conversions):
            raise ValueError()
    except ValueError:
        print("Invalid choice. Please enter a valid number.")
        continue
    conversion = conversions[choice]
    dfSelectDate = df[df["Date"]==dateInput]
    if dfSelectDate.empty:
        print("No data available for the selected date.")
    else:
        dfSelectCurrency = dfSelectDate[conversion]
        print(dfSelectCurrency)
    repeat = input("Do you want to check another date and currency conversion? (yes/no): ").strip().lower()
    if repeat != 'yes':
            break

x = df["Date"]
y=df[conversion]
plt.title(conversion )
plt.xlabel("Dates")
plt.ylabel("conversion rate ")
plt.margins(x=-0.2) 
plt.xticks(rotation=70)
plt.xticks(fontsize=6)  
plt.plot(x,y)




plt.show()
#write a program that
#   lets the user enter a currency conversion
#   validates the currency input
#   plots a graph of dates against conversion rates