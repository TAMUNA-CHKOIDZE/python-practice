# Student Grades Management

## Objective
Create a system to manage student grades using Object-Oriented Programming (OOP) principles. This exercise will help you understand how to define classes, create objects, and implement methods that handle multiple grades and calculate averages.

## Requirements

### Student Class
- Attributes:
  - `name`: Student's name (string)
  - `grades`: List of integer grades
- Methods:
  - `__init__`: Initialize attributes
  - `add_grade`: Add a grade to the list
  - `get_average_grade`: Calculate average grade
  - `__str__`: String representation of student details

### Classroom Class
- Attributes:
  - `students`: List of Student objects
- Methods:
  - `add_student`: Add Student object to the list
  - `get_top_students`: Return top three students by average grade
  - `get_failed_students`: Return students with average grade below 51

## Implementation
- Create Student instances and add grades
- Add students to Classroom
- Use Classroom methods to retrieve top and failed students
