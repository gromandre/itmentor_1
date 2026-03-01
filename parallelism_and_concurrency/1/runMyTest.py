from main import *
from multiprocessing_start import calculate_parallel_execution_time
from sequential_start import calculate_sequential_execution_time

class Mytest:
    def __init__(self, num_fibo, simple_num, factorial_num):
        self.num_fibo = num_fibo
        self.simple_num = simple_num
        self.factorial_num = factorial_num

    def run_search_num_fibo(self):
        search_num_fibo(self.num_fibo)
        print('search_num_fibo: Ok')

    def run_search_simple_num(self):
        search_simple_num(self.simple_num)
        print('search_simple_num: Ok')

    def run_search_factorial(self):
        search_factorial(self.factorial_num)
        print('search_factorial: Ok')


if __name__ == '__main__':
    mytest = Mytest(num_fibo=37, simple_num=100_000_007, factorial_num=100000)

    function_test = [calculate_parallel_execution_time, calculate_sequential_execution_time]

    for fn in function_test:
            fn(
                mytest.run_search_num_fibo,
                mytest.run_search_simple_num,
                mytest.run_search_factorial
            )
