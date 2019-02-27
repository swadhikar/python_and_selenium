# Python script to list most memory consuming processes in windows machine
from time import sleep
import subprocess
import csv

task_list = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result, error = task_list.communicate()
title = 'Image Name;PID;Session Name;Session#;Mem Usage'
csv_lines = [';'.join(l.split()) for l in result.split('\n')[1: -1]]
csv_lines = [title] + csv_lines

csv_reader = csv.DictReader(csv_lines, delimiter=';')

for _ in range(3):
    csv_reader.next()

process_details = []
for process in csv_reader:
    try:
        process_name = process['Image Name']
        memory_usage = process['Mem Usage']
        memory_usage = memory_usage.replace(',', '')
        memory_usage = int(memory_usage)
        process_details.append('{},{}'.format(process_name, memory_usage))
    except Exception:
        pass


def sort_helper(line):
    return int(line.split(',')[1])

process_details = sorted(process_details, key=sort_helper, reverse=True)

display_format = '{:>25s} {:>25s}'
print("Most memory consuming process: ")
print("========================================================")
print(display_format.format("Process", "Memory"))
print("========================================================")

for process_detail in process_details:
    process_name, memory = str(process_detail).split(',')
    print(display_format.format(process_name, memory))

time_to_sleep = 30
print("Waiting for {} seconds...".format(time_to_sleep))
sleep(time_to_sleep)
