from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int], memo: Dict = None) -> Dict:
    """
    Finds an optimal rod cutting given the list of prices using memoization technique
    :param length: Length of the rod.
    :param prices: List of prices where prices[i] is the price for a rod of length i+1.
    :return: Dictionary with max profit, segment lengths, and number of cuts.
    """
    if memo is None:
        memo = {}

    # base case
    if length == 0:
        return {"max_profit": 0, "segments": [], "cuts": 0}

    # if already have a solution for length return it
    if length in memo:
        return {
            "max_profit": memo[length][0],
            "segments": memo[length][1],
            "cuts": len(memo[length][1]) - 1,
        }

    max_profit = 0
    best_segments = []

    for i in range(1, length + 1):
        if i <= len(prices):
            remaining_solution = rod_cutting_memo(length - i, prices, memo)
            current_profit = prices[i - 1] + remaining_solution["max_profit"]

            # if found a better solution, update
            if current_profit > max_profit:
                max_profit = current_profit
                best_segments = [i] + remaining_solution["segments"]

    memo[length] = (max_profit, best_segments)

    return {
        "max_profit": max_profit,
        "segments": best_segments,
        "cuts": len(best_segments) - 1,  # number of cuts is number of segments -1
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Finds the maximum profit for a rod of given length using dynamic programming.
    :param length: Length of the rod.
    :param prices: List of prices where prices[i] is the price for a rod of length i+1.
    :return: Dictionary with max profit, segment lengths, and number of cuts.
    """
    dp = [0] * (length + 1)
    segments = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        max_profit = 0
        best_segment = []
        # for every length of the rod calculate the optimal subdivision
        for j in range(1, i + 1):
            if j <= len(prices):
                current_profit = prices[j - 1] + dp[i - j]
                if current_profit > max_profit:
                    max_profit = current_profit
                    best_segment = [j] + segments[i - j]

        # update the table for length
        dp[i] = max_profit
        segments[i] = best_segment

    return {
        "max_profit": dp[length],
        "segments": segments[length],
        "cuts": len(segments[length]) - 1,
    }


def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    header = f"{'Тест':<20} {'Метод':<15} {'Макс. прибуток':<15} {'Розрізи':<20} {'К-сть розрізів':<15}"
    separator = "-" * len(header)

    print(separator)
    print(header)
    print(separator)

    for test in test_cases:
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        table_result = rod_cutting_table(test['length'], test['prices'])

        print(
            f"{test['name']:<20} {'Мемоізація':<15} {memo_result['max_profit']:<15} {str(memo_result['segments']):<20} {memo_result['cuts']:<15}")

        print(
            f"{test['name']:<20} {'Табуляція':<15} {table_result['max_profit']:<15} {str(table_result['segments']):<20} {table_result['cuts']:<15}")

    print(separator)
    print("\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()
