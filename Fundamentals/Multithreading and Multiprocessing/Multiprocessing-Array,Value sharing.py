import multiprocessing
# creating a new pocess always creates a new address space. Array/Value


def calc_square(numbers, result, val):
    val.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n * n


if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', 3)
    val = multiprocessing.Value('d', 0.0)

    p = multiprocessing.Process(target=calc_square, args=(numbers, result, val))

    p.start()
    p.join()

    print(result[:])
    print(val.value)
