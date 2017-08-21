#!/usr/bin/python

import fasteners
import time

rw_lock = fasteners.ReaderWriterLock()
file_path = "test"
i = 5
while i > 1:

    i -= 1
    with rw_lock.read_lock():
        print(" %d is reading something" % i)
        with open(file_path, 'r') as f_output:
            time.sleep(6)
            for line in f_output:
                list_line = line.split()
                print(list_line[0])
            print("EOF")

        # f_output.seek(0)

