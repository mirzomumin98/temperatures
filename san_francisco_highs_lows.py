import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = '../data/san_francisco_2018.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)


	# Чтение дат, температурных максимумов из файла
	highs, lows, dates = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
		try:
			high = int(row[header_row.index('TMAX')])
			low = int(row[header_row.index('TMIN')])
		except ValueError:
			f'Missing data at {current_date}'
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)


# Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(dates, highs, c='red', alpha=0.5, label='highs')
plt.plot(dates, lows, c='blue', alpha=0.5, label='lows')
plt.axis(ymin=20, ymax=140)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Оформление диаграммы
plt.title('Daily high and low temperatures - 2018\nSan-Francisco CA', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend()

plt.savefig('san_francisco_highs_lows.png', bbox_inches='tight')