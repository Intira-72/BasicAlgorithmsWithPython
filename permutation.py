# factorials การหาความเป็นไปได้ว่ามีความเป็นไปได้กี่รูปแบบ
# !5 = 5 x 4 x 3 x 2 x 1

def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


if __name__ == "__main__":
    print(iterative_factorial(5))