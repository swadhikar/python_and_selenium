import csv


with open('file1.csv') as f1, open('file2.csv') as f2:
    f1_reader_obj = csv.reader(f1)
    f2_reader_obj = csv.reader(f2)

    next(f1_reader_obj)
    next(f2_reader_obj)

    for file1_line, file2_line in zip(f1_reader_obj, f2_reader_obj):
        line1_as_str = ' '.join(file1_line)
        line2_as_str = ' '.join(file2_line)
        print(line1_as_str)
        print(line2_as_str)
