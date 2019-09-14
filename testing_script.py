# press cmd + I to run script

num1 = 100_000_000
num2 = 19_318_431

total = num1 + num2

# print(f'{total:,}')


condition = False

x = 1 if condition else False

# print(x)

# queues

def dequeue(sample):
    return sample.pop(0)

sample = [1,2,3,4]

# return doesn't actually 'return' anything that we can use. We need to make some use of it like store it in a variable or call it within another function
sample.pop(0)

# now, sample = [2,3,4]

# instead of sample.pop(0), we can do either val = sample.pop(0), which will store the 1st element, or run return sample.pop(0) within another function like we do in dequeue(sample)

val = sample.pop(0)
# print(val)
# print(dequeue(sample))

def binary_search(input_array, value):
    """Your code goes here."""
    low = 0
    high = len(input_array)-1
    while low <= high:
        mid = int((low + high)/2)
        if value == input_array[mid]:
            return mid
        elif value > input_array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
# print(binary_search(test_list, test_val1))
# print(binary_search(test_list, test_val2))
