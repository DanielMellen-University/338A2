import sys
import json
import matplotlib.pyplot as plt
import time
import threading
threading.stack_size(33554432)


sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    filename = "338A2Q2.json"
    try:
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                print(f"Error: {filename} does not contain valid JSON data.")
                return

            times = []
            sizes = []
            for arr in data:
                start_time = time.time()
                func1(arr, 0, len(arr) - 1)
                end_time = time.time()
                times.append(end_time - start_time)
                sizes.append(len(arr))

            plt.plot(sizes, times)
            plt.xlabel("Size of input array")
            plt.ylabel("Time taken (in seconds)")
            plt.title("QuickSort performance")
            plt.show()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

if __name__ == "__main__":
    main()

