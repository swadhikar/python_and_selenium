""" Multiprocessing way to update shared resources using server process """

import multiprocessing

record_list = [('Sam', 10), ('Adam', 8), ('Kevin', 11)]
new_record = ('Jerry', 7)


def print_records(records):
    for record in records:
        print(f'Name: {record[0]}\nScore: {record[1]}\n')


def insert_record(records, record):
    records.append(record)
    print(f'Added new record: {record}')


def manager_way():
    with multiprocessing.Manager() as manager:
        m_records = manager.list(record_list)

        p1 = multiprocessing.Process(target=insert_record, args=(m_records, new_record))
        p2 = multiprocessing.Process(target=print_records, args=(m_records,))

        for p in (p1, p2):
            p.start()

        for p in (p1, p2):
            p.join()

    """
    Added new record: ('Jerry', 7)
    Name: Sam
    Score: 10
    
    Name: Adam
    Score: 8
    
    Name: Kevin
    Score: 11
    
    *** New record is properly inserted! ***
    Name: Jerry
    Score: 7
    """


def usual_way():
    p1 = multiprocessing.Process(target=insert_record, args=(record_list, new_record))
    p2 = multiprocessing.Process(target=print_records, args=(record_list,))

    for p in (p1, p2):
        p.start()

    for p in (p1, p2):
        p.join()

    """
    Insert operation doesn't reflect at the record list
    
    Added new record: ('Jerry', 7)
    Name: Sam
    Score: 10
    
    Name: Adam
    Score: 8
    
    Name: Kevin
    Score: 11
    """


if __name__ == '__main__':
    usual_way()
    manager_way()
