from collections import Counter

def determine_winner(votes, candidates):
    candidate_votes = Counter(votes)

    # Находим максимальное количество голосов
    max_votes = max(candidate_votes.values())

    # Определяем всех кандидатов с максимальным количеством голосов
    winners = [candidate for candidate, votes in candidate_votes.items() if votes == max_votes]

    if len(winners) == 1:
        winner = winners[0]
        print(f"Победитель выборов: {winner} с количеством голосов: {max_votes}")
    else:
        # В случае, если есть два победителя, сортируем их по длине имени
        winners.sort(key=lambda x: len(x))

        # Выбираем победителя с минимальным количеством букв в имени
        winner = winners[0]
        print(f"Победитель выборов (по длине имени): {winner} с количеством голосов: {max_votes}")

# Запрос данных у пользователя
candidates = []

while True:
    candidate_input = input("Введите имя кандидата или введите '1' для завершения ввода: ")
    if candidate_input == '1':
        break
    candidates.append(candidate_input)

try:
    voters_count = int(input("Введите количество голосующих: "))
except ValueError:
    print("Ошибка: Введите корректное число.")
    exit()

# Голосование
try:
    votes_input = input(f"Введите количество голосов за каждого кандидата через пробел: ")
    votes = [candidates[int(vote) - 1] for vote in votes_input.split()]
except (ValueError, IndexError):
    print("Ошибка: Введите корректные голоса за каждого кандидата.")
    exit()

if len(votes) != len(candidates) * voters_count:
    print("Ошибка: Введено некорректное количество голосов.")
    exit()

# Определение победителя 
determine_winner(votes, candidates)
