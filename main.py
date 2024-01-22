import csv
import sys
import os
def read_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File not'{file_path}' found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def write_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def apply_changes(csv_data, changes):
    for change in changes:
        try:
            x, y, value = map(int, change.split(','))
            if 0 <= x < len(csv_data[0]) and 0 <= y < len(csv_data):
                csv_data[y][x] = value
            else:
                print(f"Error: Invalid change '{change}'. Row or column index out of range. Skipping.")
        except (ValueError, IndexError):
            print(f"Error: Invalid change format '{change}'. Skipping.")
    return csv_data
