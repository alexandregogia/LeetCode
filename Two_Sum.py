
lst = input("Enter a list of numbers separated by spaces: ")
target = int(input("Enter the target number: "))

numbers = lst.split()
n = len(numbers)

for i in range(n):
    numbers[i] = int(numbers[i])
    if not -10**9 <= numbers[i] <= 10**9:
            raise ValueError("Invalid input")

if not 2 <= n <= 10**4:
    raise ValueError("Invalid input")

if not -10**9 <= target <= 10**9:
    raise ValueError("Invalid input")

def two_sum(n, numbers, target):
    
    for i in range(n):
        for j in range(n):
            if numbers[i] + numbers[j] == target and i != j:
                print("numbers: ", numbers)
                return [i, j]

func = two_sum(n, numbers, target)
print(func)