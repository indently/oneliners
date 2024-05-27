from typing import Callable, Any

type Flatten = Callable[[list], list]  # type: ignore
flatten: Flatten = lambda target: sum((flatten(sub) if isinstance(sub, list) else [sub] for sub in target), [])

# Example usage
nested_list: list[Any] = [1, [2, [3, 4], 5], [6, 7], 8, [[[[[[9, 10], 11]]]]]]
print(flatten(nested_list))
