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
            x, y, value = map(str, change.split(','))
            x, y = int(x), int(y)
            if 0 <= x < len(csv_data[0]) and 0 <= y < len(csv_data):
                csv_data[y][x] = value
            else:
                print(f"Error: Invalid change '{change}'. Row or column index out of range. Skipping.")
        except (ValueError, IndexError):
            print(f"Error: Invalid change format '{change}'. Skipping.")
    return csv_data

def display_csv(csv_data):
    for row in csv_data:
        print(', '.join(str(cell) for cell in row))

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 4:
        print("Usage: reader.py <src> <dst> <change1> <change2> ...")
        sys.exit(1)

    # Parse command-line arguments
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    changes = sys.argv[3:]

    # Read the CSV file
    csv_data = read_csv(src_file)

    # Apply changes to the CSV data
    csv_data = apply_changes(csv_data, changes)

    # Display modified CSV content
    print("\nModified CSV Content:")
    display_csv(csv_data)

    # Save modified CSV to the destination file
    write_csv(dst_file, csv_data)

if __name__ == "__main__":
    main()