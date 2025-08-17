## 🎯 Objective

Implement higher-order functions using lambda functions.

---

## 📋 Requirements

Define the function `apply_operation` with the following signature:

```python
def apply_operation(numbers, operation):
    """
    Apply the given operation to each element in the list of numbers.

    :param numbers: List of numbers to be processed.
    :param operation: A function that defines the operation to apply to each element.
    :return: A new list with the operation applied to each element.
    """
    return [operation(number) for number in numbers]
````

---

## 🚀 How it works

The function takes a list of numbers and a function (operation), then applies this operation to each number in the list, returning a new list with the results.

---

## 🖥️ Example input and output

Input list:

```
[1, 2, 3, 4, 5]
```

Operations and their outputs:

* Doubled: `[2, 4, 6, 8, 10]`
* Squared: `[1, 4, 9, 16, 25]`
* Filtered (odd numbers): `[1, 3, 5]`

---

## 🛠️ Concepts used

* Higher-order functions
* Lambda functions
* List comprehensions

```

