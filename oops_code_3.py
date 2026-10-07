class Student:
    """
    Demonstrates encapsulation using a property and setter.

    Marks are stored internally in _marks and accessed through
    the public marks property.

    The setter validates the new value before allowing the
    student's marks to be updated.
    """

    school = "Republic of Happiness"

    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks: value must be between 0 and 100")


s1 = Student("JOYBOY", 90)

print(f"Student: {s1.name} | Marks: {s1.marks}")

s1.marks = 95
print(f"Updated Marks: {s1.marks}")

s1.marks = -10
print(f"Final Marks: {s1.marks}")