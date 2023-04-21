import csv
import datetime

def read_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            current_date = datetime.datetime.now().strftime('%Y%m%d')
            print(f"Current gh-actions server date: {current_date}")
            if row[0] == current_date:
                return row[1], row[2]
    return None
