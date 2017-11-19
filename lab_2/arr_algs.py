def arr_min(arr):
    result = arr[0]
    for i in arr:
        if result > i:
            result = i
    return result


def average(arr):
    return sum(arr) / len(arr)


if __name__ == "__main__":
    print(arr_min([1, 6, 8, 4, 3, 7]))
    print(average([1, 6, 8, 4, 3, 7]))