# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    length = len(numbers) - 1
    max_value = 0
    max_second_value = 0
    for i in range(length, -1, -1):
        if numbers[i] > max_value:
            max_second_value = max_value
            max_value = numbers[i]
        elif numbers[i] > max_second_value:
            max_second_value = numbers[i]

    return max_value * max_second_value



if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
