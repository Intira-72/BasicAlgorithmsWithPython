# Bubble Sort 

def bubble_optimized(vals):
    iterations = 0
    for i in range(len(vals)):
        for j in range(len(vals) - i - 1):
            iterations += 1
            if vals[j] > vals[j + 1]:
                vals[j], vals[j + 1] = vals[j + 1], vals[j]
    return vals, iterations


if __name__ == "__main__":
    vals = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_optimized(vals))