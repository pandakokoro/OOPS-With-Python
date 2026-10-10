
class Student:
    """
    Demonstrates validated property setters
    and exception handling.
    """

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self._marks = value


s1 = Student("JOYBOY", 90)

try:
    s1.marks = 95
    print(f"Updated marks: {s1.marks}")

    s1.marks = 150
    print(f"Current marks: {s1.marks}")

except ValueError as error:
    print(f"Update rejected: {error}")

print(f"Final marks: {s1.marks}")
