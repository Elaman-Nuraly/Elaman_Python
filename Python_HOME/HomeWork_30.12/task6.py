"""
task 6
"""
def balance_array(arr):

    positive_sum = sum(x for x in arr if x > 0)
    negative_sum = sum(x for x in arr if x < 0)
    new_element = abs(negative_sum) - positive_sum

    print(arr)

    print("Positive Sum:", positive_sum)

    print("Negative Sum:", negative_sum)

    print("Need:", new_element)

    result_array = arr + [new_element]

    print(result_array)

if __name__ == "__main__":

    input_array = [-3, -2, 1, 2, 3, 4]
    balance_array(input_array)
    