"""
home work 2
"""
from itertools import permutations

def generate_words(input_sequence):
    unique_chars = set(input_sequence)
    words = set()
    for length in range(1, len(unique_chars) + 1):
        perms = permutations(unique_chars, length)
        for perm in perms:
            word = ''.join(perm)
            words.add(word)
    return sorted(words, key=lambda x: (len(x), x))
if __name__ == "__main__":
    while True:
        try:
            input_sequence = input("Введите последовательность символов: ")
            if input_sequence.lower() == 'exit':
                break
            result = generate_words(input_sequence)
            print("Количество слов:", len(result))
            print("Слова:")
            for word in result:
                print(word)
        except Exception as e:
            print(f"Произошла ошибка: {e}")