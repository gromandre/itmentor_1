from multiprocessing import Process
import time


def calculate_parallel_execution_time(f1, f2, f3):
    start = time.time()

    p1 = Process(target=f1)
    p2 = Process(target=f2)
    p3 = Process(target=f3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("time multiprocessing:", time.time() - start)


