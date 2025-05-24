import random
import timeit
import matplotlib.pyplot as plt

############## Randomized_quick_sort ##################
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

############## Deterministic_quick_sort ##################
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

############## Test ##################
if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    rand_times = []
    det_times = []

    results_text = f"{'Розмір масиву':<15}{'RandQuickSort (сек)':<25}{'DetQuickSort (сек)'}\n"
    results_text += "-" * 60 + "\n"

    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        arr1 = arr.copy()
        arr2 = arr.copy()

        rand_time = timeit.timeit(lambda: randomized_quick_sort(arr1), number=5) / 5
        det_time = timeit.timeit(lambda: deterministic_quick_sort(arr2), number=5) / 5

        rand_times.append(rand_time)
        det_times.append(det_time)

        results_text += f"{size:<15}{rand_time:<25.6f}{det_time:.6f}\n"

    print(results_text)

    # Plot graph
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, rand_times, marker='o', label='Randomized QuickSort')
    plt.plot(sizes, det_times, marker='o', label='Deterministic QuickSort')
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("QuickSort Performance Comparison")
    plt.legend()
    plt.grid(True)
    plt.savefig("quick_sort_comparison.png")
    plt.show()

    # Write to README.md
    with open("README.md", "w") as f:
        f.write("# QuickSort Performance Analysis\n\n")
        f.write("This report compares the execution time of **Randomized QuickSort** and **Deterministic QuickSort** on arrays of different sizes.\n\n")
        f.write("## Results\n\n")
        f.write("```\n")
        f.write(results_text)
        f.write("```\n")
        f.write("## Performance Chart\n\n")
        f.write("![QuickSort Performance](quick_sort_comparison.png)\n")
