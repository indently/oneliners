from secrets import choice
from string import ascii_letters, digits, punctuation
from typing import Callable

pass_gen: Callable[[int], str] = lambda x: ''.join(choice(ascii_letters + digits + punctuation) for _ in range(x))


def main() -> None:
    print(pass_gen(4))
    print(pass_gen(6))
    print(pass_gen(20))


if __name__ == '__main__':
    main()
