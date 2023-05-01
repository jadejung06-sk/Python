import time
from random import Random
from multiprocessing import Barrier
import multiprocessing
from multiprocessing.context import Process

'''
Each Process will have a separate memory space.
'''

##### Simple example
# matrix_size = 3
# matrix_a = [[3,1,-4],
#             [2,-3,1],
#             [5,-2,0]]

# matrix_b = [[1,-2,-1],
#             [0,5,4],
#             [-1,-2,3]]

# result = [[0] * matrix_size for r in range(matrix_size)]
# # print(result)

# for row in range(matrix_size):
#     for col in range(matrix_size):
#         for i in range(matrix_size):
#             result[row][col] += matrix_a[row][i] * matrix_b[i][col]
            
# for row in range(matrix_size):
#     print(matrix_a[row], matrix_b[row], result[row])
# print()

##### Only one time
# matrix_size = 200 # 5
# matrix_a = [[0] * matrix_size for a in range(matrix_size)]
# matrix_b = [[0] * matrix_size for b in range(matrix_size)]
# result = [[0] * matrix_size for r in range(matrix_size)]
# random = Random()

# def generate_random_matrix(matrix):
#     for row in range(matrix_size):
#         for col in range(matrix_size):
#             matrix[row][col] = random.randint(-5,5)
    
# generate_random_matrix(matrix_a)
# generate_random_matrix(matrix_b)
# for row in range(matrix_size):
#     for col in range(matrix_size):
#         for i in range(matrix_size):
#             result[row][col] += matrix_a[row][i] * matrix_b[i][col]
            
# for row in range(matrix_size):
#     print(matrix_a[row], matrix_b[row], result[row])
# print()


##### ten times
# matrix_size = 200 # 5
# matrix_a = [[0] * matrix_size for a in range(matrix_size)]
# matrix_b = [[0] * matrix_size for b in range(matrix_size)]
# result = [[0] * matrix_size for r in range(matrix_size)]
# random = Random()

# def generate_random_matrix(matrix):
#     for row in range(matrix_size):
#         for col in range(matrix_size):
#             matrix[row][col] = random.randint(-5,5)

# start = time.time()
# for t in range(10):
#     generate_random_matrix(matrix_a)
#     generate_random_matrix(matrix_b)
#     result = [[0] * matrix_size for r in range(matrix_size)]
#     for row in range(matrix_size):
#         for col in range(matrix_size):
#             for i in range(matrix_size):
#                 result[row][col] += matrix_a[row][i] * matrix_b[i][col]
            
# end = time.time()
# print("Done, time taken", end - start) # Done, time taken 11.651249647140503

##### Barrier
# matrix_size = 200 # 5
# matrix_a = [[0] * matrix_size for a in range(matrix_size)]
# matrix_b = [[0] * matrix_size for b in range(matrix_size)]
# result = [[0] * matrix_size for r in range(matrix_size)]
# random = Random()
# work_start = Barrier(matrix_size + 1)
# work_complete = Barrier(matrix_size + 1)

# def generate_random_matrix(matrix):
#     for row in range(matrix_size):
#         for col in range(matrix_size):
#             matrix[row][col] = random.randint(-5,5)

# def work_out_row(row):
#     while True:
#         work_start.wait()
#         for col in range(matrix_size):
#             for i in range(matrix_size):
#                 result[row][col] += matrix_a[row][i] * matrix_b[i][col]
#         work_complete.wait()

# for row in range(matrix_size):
#     Thread(target = work_out_row, args = ([row])).start()
# start = time.time()
# for t in range(10):
#     generate_random_matrix(matrix_a)
#     generate_random_matrix(matrix_b)
#     result = [[0] * matrix_size for r in range(matrix_size)]
#     work_start.wait()
#     work_complete.wait()
# end = time.time()
# print("Done, time taken", end - start) # Done, time taken 8.695238828659058


###### Multi process
process_count = 8
matrix_size = 200 # 5
random = Random()

def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row * matrix_size + col] = random.randint(-5,5)

def work_out_row(id, matrix_a, matrix_b, result, work_start, work_complete):
    while True:
        work_start.wait()
        for row in range(id, matrix_size, process_count):
            for col in range(matrix_size):
                for i in range(matrix_size):
                    result[row * matrix_size + col] += matrix_a[row * i + col] * matrix_b[row * i +col]
        work_complete.wait()

if __name__ == "__main__":
    # print([0] * (3 * 3)) # [0, 0, 0, 0, 0, 0, 0, 0, 0]
    multiprocessing.set_start_method('spawn')
    work_start = Barrier(process_count + 1)
    work_complete = Barrier(process_count + 1)
    matrix_a = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock  = False)     # Each Process will have a separate memory space
    matrix_b = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock = False)
    result = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock = False)
    for p in range(process_count):
        Process(target = work_out_row, args = (p, matrix_a, matrix_b, result, work_start, work_complete)).start()
    start = time.time()
    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)
        for i in range(matrix_size * matrix_size):
            result[i] = 0 
        work_start.wait()
        work_complete.wait()
    end = time.time()
    print("Done, time taken", end - start) # Done, time taken 3.8701984882354736 not linear due to syncronize and communicate with processors each other

