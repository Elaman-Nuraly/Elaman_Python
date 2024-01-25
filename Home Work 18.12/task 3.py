def get_user_data():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    education = input("Введите ваше образование: ")
    experience = input("Введите ваш опыт работы: ")
    skills = input("Введите ваши навыки: ")
    return name, age, education, experience, skills
def print_cv(name, age, education, experience, skills):
    print("\nCV:")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Образование: {education}")
    print(f"Опыт работы: {experience}")
    print(f"Навыки: {skills}")
if __name__ == "__main__":
    user_data = get_user_data()
    print_cv(*user_data)