def list_multiples(num, length):
    new_arr = []
    for i in range(1, length + 1):
        new_arr.append(i*num)
    return new_arr

print(list_multiples(12,10))

def majority(arr, needed = None):
    if not needed:
        needed = len(arr)/2
    x = arr[0]
    if arr.count(x) > needed:
        return x
    elif len(arr)<needed:
        return None
    else:
        new_arr = [i for i in arr if i != x]
        return majority(new_arr, needed)

test1 = ["A", "A", "B"]
test2 = ["A", "B", "B", "A", "C", "C"]
print(majority(test1))
print(majority(test2))