"""
task 3
"""
def calculate_min_cost(N, costs):

    costs.sort(reverse=True)
    total_cost = 0
    for i in range(N):
        if i % 3 != 2:  
            total_cost += costs[i]
    return total_cost

if __name__ == "__main__":
    while True:
        try:
            N = int(input("Введите количество товаров: "))
            if N < 1 or N > 1000:
                raise ValueError("Некорректное значение")
            costs = list(map(int, input("Введите стоимости товаров: ").split()))
            if len(costs) != N or any(cost > 10000 for cost in costs):
                raise ValueError("Некорректные стоимости товаров")
            result = calculate_min_cost(N, costs)

            print("Минимальная сумма: {}".format(result))
        except ValueError as e:

            print(f"Ошибка ввода: {e}")
            break
        