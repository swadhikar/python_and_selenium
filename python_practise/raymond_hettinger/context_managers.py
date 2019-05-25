from contextlib import contextmanager
from threading import (
    Thread,
    Lock,
    current_thread
)


number = 0
thread_lock = Lock()


@contextmanager
def acquire_thread_lock():
    try:
        thread_lock.acquire()   # Intended open resource operation
        yield                   # Return control to the caller
    except Exception as exc:
        print('Failed to acquire thread lock!')    # Quit if exception arises
        raise
    finally:
        thread_lock.release()


def print_number(thread_name=None):
    print('Value of "n" post "{}" thread\'s update is: {}'.format(current_thread().name, number))


def raise_number_by(n, num_times):
    global number
    with acquire_thread_lock():
        for _ in range(num_times):
            number += n
        print_number()
    # Lock released from contextmanager

def clear_number():
    global number
    number = 0


def main(t1=1000, t2=2000, t3=3000):

    t_raise_by_1 = Thread(target=raise_number_by, args=(1, t1), name='t1')
    t_raise_by_2 = Thread(target=raise_number_by, args=(1, t2), name='t2')
    t_raise_by_3 = Thread(target=raise_number_by, args=(1, t3), name='t3') # 1000, 2000, 3000 = 6000
    
    for thread in (t_raise_by_1, t_raise_by_2, t_raise_by_3):
        thread.start()

    for thread in (t_raise_by_1, t_raise_by_2, t_raise_by_3):
        thread.join()

    clear_number()


#main()


from pprint import pprint

my_json = {
  a: {
    b: {
      c: [
        {
          d: [
            { f: 'some_string' }
          ]
        },
        {
          e: {
            g: [
              {h: 'another string'}
            ]
          }
        }
      ]
    }
  }
  z: [
    b: {
      c: [
        {
          d: [
            { f: 'some_string1' }
          ]
        },
        {
          e: {
            g: [
              h: 'another string1'
            ]
          }
        }
      ]
    },
    x: {
      c: [
        {
          d: [
            { f: 'some_string2' }
          ]
        },
        {
          e: {
            g: [
              {h: 'another string2'}
            ]
          }
        }
      ]
    }
  ]
}

pprint(word_dict)
