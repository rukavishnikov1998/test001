def most_frequent(list):
    return max(set(list), key = list.count)  

numbers = [10,14,14,14,15,11,11]
most_frequent(numbers)
