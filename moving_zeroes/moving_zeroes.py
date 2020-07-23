'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeroes = 0
    i = 0
    while i < len(arr):
        if (len(arr) - 1 - i) == zeroes:
            break
        elif arr[i] == 0:
            zeroes += 1
            arr.append(arr.pop(i))
        else:
            i+=1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")