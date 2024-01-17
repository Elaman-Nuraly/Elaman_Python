"""
home_work_2
"""
import re
def extract_vowel_words(text):
    word_pattern = re.compile(r'\b[aeiouAEIOU][a-zA-Z]*\b')
    words = re.findall(word_pattern, text)
    return words
if __name__ == "__main__":
    while True:
        try:
            input_text = input("Введите текст: ")
            result = extract_vowel_words(input_text)
            if result:
                print("Извлеченные слова:", result)
            else:
                print("Нет слов, начинающихся на гласную букву.")
                break
        except Exception as e:
            print(f"Произошла ошибка: {e}")