"""
home_work_1
"""
import re
def extract_domains(emails):
    domain_pattern = re.compile(r'@([a-zA-Z0-9.-]+)')
    domains = set()
    for email in emails:
        match = domain_pattern.search(email)
        if match:
            domains.add(match.group(1))
    return list(domains)
if __name__ == "__main__":
    while True:
        try:
            input_emails = input("Введите список e-mail адресов: ").split()
            result = extract_domains(input_emails)
            if result:
                print("Извлеченные домены:", result)
            else:
                print("Нет доменов для извлечения.")
                break
        except Exception as e:
            print(f"Произошла ошибка: {e}")