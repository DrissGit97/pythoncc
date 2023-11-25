from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#for index, column_header in enumerate(header_row):
#    print(index, column_header)

#Extract date, and high and low temperatures
PRCPs, dates = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        PRCP = float (row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        PRCPs.append(PRCP)


# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, PRCPs, color='red', alpha=0.5)


# Format plot
ax.set_title("Amount of Rainfall, Sitka, 2021", fontsize = 20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("PRCP (Rainfall)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

#print(highs)