# I am trying to change the format of dates from 30-Jan-02 to 30.Jan.2002
# occurring in second position in a csv file using python. I tried several
# things but I am confused with strings and bytes comptability.
#
# http://stackoverflow.com/questions/44045643/in-python-how-to-change-date-format-in-a-csv
import datetime

with open("filename.csv", 'r') as csv_file, open('temp.csv', 'w') as temp_file:
    for line in csv_file.readlines():
        # Fetch all dates in the csv
        dates = line.split(',')

        # Extract date, month and year
        dt, mon, yr = dates[1].split('-')

        # Convert the second date and replace
        dates[1] = datetime.datetime.strptime(dates[1], '%d-%b-%y').strftime('%d.%b.%Y')

        # Write date to temp file
        temp_file.write(','.join(dates))

print("Process complete!")