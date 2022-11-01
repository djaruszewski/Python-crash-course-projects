import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Printing headers and their index positions:
    # for index, column_header in enumerate(header_row):
          # print(index, column_header)

    # Get dates and high temperatures from this file.
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(current_date)
        rainfall.append(rain)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rainfall, c='red')

    # Format plot.
    ax.set_title("Daily rainfall - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Rainfall (in)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()