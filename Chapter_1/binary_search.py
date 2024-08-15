def binary_search(list, item):
    low = 0
    high = len(list) - 1 # get the last item in an array

    while low <= high:
        middle = (low + high) // 2 # double slash, floor division 
        print("middle: ",middle)
        guess = list[middle]
        print("guess: ",guess)
        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
            print("high: ",high)
        else:
            low = middle + 1
            print("low: ",low)
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list,9)) # => 1
# print(binary_search(my_list,-1)) # => none 10 10 = 100