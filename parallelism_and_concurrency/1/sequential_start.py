from main import *
import time


def run_search_num_fibo(self):
    search_num_fibo(37)
    print('search_num_fibo: Ok')


def run_search_simple_num(self):
    search_simple_num(100_000_007)
    print('search_simple_num: Ok')


def search_factorial():
    search_factorial(100000)
    print('search_factorial: Ok')

def calculate_sequential_execution_time(fn1, fn2, fn3):
    start = time.time()
    fn1()
    fn2()
    fn3()
    print("time sequential:", time.time() - start)