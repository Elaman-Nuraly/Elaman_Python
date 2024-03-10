"""
task 5
"""
def align_strings(strings):

    max_length = max(len(s) for s in strings)

    print(max_length)

    for s in strings:
        stars_count = max_length - len(s)
        aligned_string = '*' * stars_count + s

        print(aligned_string)

if __name__ == "__main__":

    input_strings = ["da", "net", "poka"]
    align_strings(input_strings)
    