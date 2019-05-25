""" Python script that shares memory with multiprocessing """
import multiprocessing

proc_lock = multiprocessing.Lock()


def square_list(in_list, result_array_index, sum_squares):
    proc_lock.acquire()
    result_array, index = result_array_index
    for num in in_list:
        result_array[index.value] = num ** 2
        index.value += 1
    sum_squares.value = sum(result_array)
    proc_lock.release()


if __name__ == '__main__':
    # Define data
    test_list_1 = [1, 2, 3, 4]
    test_list_2 = [5, 6, 7, 8]
    test_list_3 = [9, 10, 11, 12]
    list_input = (test_list_1, test_list_2, test_list_3)

    result_as_array = multiprocessing.Array('i', 4 * len(list_input))
    result_index_num = multiprocessing.Value('i')
    squares_as_sum = multiprocessing.Value('i')
    result_index_num.value = 0
    process_list = list()

    for test_list in list_input:
        result_array_and_index = result_as_array, result_index_num
        p = multiprocessing.Process(target=square_list, args=(test_list, result_array_and_index, squares_as_sum))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    print('Squares list:')
    for i in range(len(result_as_array)):
        print(result_as_array[i], end=' ')

    print('\nSum of all squares:', squares_as_sum.value)
