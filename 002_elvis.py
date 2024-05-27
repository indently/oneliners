# Example 1
def valid_length(user_input: str) -> str:
    if len(user_input) > 10:
        return 'Yes case'
    else:
        return 'No case'


# Example 2
def valid_length_elvis(user_input: str) -> str:
    return 'Yes case' if len(user_input) > 10 else 'No case'


# Example 3
def valid_length_elvis_2(user_input: str) -> bool:
    return len(user_input) > 10


def main() -> None:
    print(f'{valid_length('Bob loves grapefruit.')=}')
    print(f'{valid_length_elvis('Hi, Bob!')=}')
    print(f'{valid_length_elvis_2('Hi, Bob!')=}')


if __name__ == '__main__':
    main()


