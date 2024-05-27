import re
from typing import Callable

type Email = Callable[[str], list[str]]  # type: ignore
get_emails: Email = lambda text: re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)


def main() -> None:
    with open('text.txt') as txt:
        sample_text: str = txt.read()

    print(get_emails(sample_text))


if __name__ == '__main__':
    main()
