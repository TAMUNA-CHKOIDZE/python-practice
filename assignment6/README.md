# 📚 Basic Shape Hierarchy

## Task
Create a Basic Shape Hierarchy

## Objective
Implement a basic inheritance structure with polymorphism in Python.

---

## ✅ Step 1: Create a Base Class

- Define a class `Shape` with an initializer to set a `name` attribute.
- Add a method `area()` that returns `None` (this will be overridden in subclasses).

---

## ✅ Step 2: Create Subclasses

### Rectangle
- Inherits from `Shape`.
- Add attributes `width` and `height` in the initializer.
- Override the `area()` method to return the area of the rectangle.

### Circle
- Inherits from `Shape`.
- Add an attribute `radius` in the initializer.
- Override the `area()` method to return the area of the circle (use `math.pi` for the value of π).

---

## ✅ Step 3: Demonstrate Polymorphism

- Create a function `print_area(shape)` that takes a `Shape` object and prints its name and area.
- Instantiate a `Rectangle` and a `Circle`, and call `print_area()` for each.
