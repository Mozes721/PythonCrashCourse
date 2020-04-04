import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates and rainfall data from data file.
#  Rainfall data is in column 19.
filename = '/Users/richard/Desktop/PythonCrashCourse/chapter_16/sitka_weather_07-2014.csv'
with open(filename) as f:
    #read the csv file
    reader = csv.reader(f)
    #get the header row
    header_row = next(reader)

    #store dates, rainfalls, totals in an array
    dates, rainfalls, totals = [], [], []
    #make a for loop through the file
    for row in reader:
        try:
            #get the date of time from the vaules
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            #rainfall from apropriate row
            rainfall = float(row[19])
        except ValueError:
            #except the data is missing
            print(current_date, 'missing data')
        else:
            #append to dates the current date
            dates.append(current_date)
            #then rainfall
            rainfalls.append(rainfall)
            if totals:
                #if totals then append them as well plus rainfualls
                totals.append(totals[-1] + rainfall)
            else:
                totals.append(rainfall)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfalls, c='blue', alpha=0.5)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)

plt.plot(dates, totals, c='blue', alpha=0.75)
plt.fill_between(dates, totals, facecolor='blue', alpha=0.05)

# Format plot.
title = "Daily rainfall amounts and cumulative rainfall - 2015\nSitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
