import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	highs, lows, dates = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		high = int(row[5])
		low = int(row[6])
		highs.append(high)
		lows.append(low)
		dates.append(current_date)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax = plt.plot(dates, highs, c='red', alpha=0.5, label='highs')
ax = plt.plot(dates, lows, c='blue', alpha=0.5, label='lows')
plt.axis(ymin=20, ymax=140)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high and low temperatures - 2018\nSitka, AK', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend()

plt.savefig('sitka_highs_lows.png', bbox_inches='tight')