import random
import time

random.seed(42)

mode_params = {
    # mode: [min, max, size]
    "tiny": [0, 10, 6],
    "small": [0, 30, 12],
    "medium": [0, 3000, 2000],
    "large": [0, 50_000, 35_000],
    "huge": [0, 1_500_000, 1_000_000]
}


# Test sort method, returns time taken to sort per element.
def test_sort(sort_method, mode="tiny", verbose=False):
    """
    Test sort method, returns time taken to sort per element.
    If sort is un successful, returns -1.

    :param sort_method: function to test
    :param mode: (str) size of array to sort, one of "tiny", "small", "medium", "large", "huge"
    :return:
    """
    arr = [random.randint(*(mode_params[mode][:2])) for _ in range(mode_params[mode][2])]
    arr_copy = arr.copy()
    if verbose:
        print(f"Testing {sort_method.__name__} with {mode} array over {len(arr)} elements")
    start_time = time.time()
    sort_method(arr)
    end_time = time.time()
    avg_time = (end_time - start_time) * 100 / len(arr)
    success = arr == sorted(arr_copy)
    if verbose:
        if success:
            print(f"Success!Avg time per 100 elems: {avg_time}s")
        else:
            print("Failed! Array not sorted correctly.")
    if success:
        return avg_time
    else:
        return -1
