import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

def read_weather(filename):
    """Read dates, highs, and lows from the CSV file."""
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except Exception:
                continue  # Skip rows with missing data
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

def plot_temps(dates, temps, label, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(f"Daily {label} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather(filename)
    print("Welcome to the Sitka Weather Viewer!")
    print("Menu:")
    print("  highs - View high temperatures")
    print("  lows  - View low temperatures")
    print("  exit  - Exit the program")
    while True:
        choice = input("choice: ").strip().lower()
        if choice in ('highs', 'high', 'High', 'Highs'):
            plot_temps(dates, highs, "high", "red")
        elif choice in ('low', 'lows', 'Low', 'Lows'):
            plot_temps(dates, lows, "low", "blue")
        elif choice == 'exit':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'highs', 'lows', or 'exit'. Try again or exit")

if __name__ == "__main__":
    main()