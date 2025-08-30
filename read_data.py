import serial
import csv
from datetime import datetime
import os
import time

MAX_FILE_SIZE = 50 * 1024 * 1024 

# Connect to arduino
ser = serial.Serial('/dev/cu.XXXXXXXX', 9600)

# Open data csv and append data to csv
file = 'data/temp_humid_data.csv'
with open(file, 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    while True:
        csvfile.flush() 
        if os.path.getsize(file) > MAX_FILE_SIZE:
            break

        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()

        # Split the line
        values = line.split(',')

        now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        row = [now_str] + values

        # Write the data to the CSV file
        csvwriter.writerow(row)

        # Flush the file to ensure data is written immediately
        csvfile.flush()

        time.sleep(900)

# Close the serial port
ser.close()
