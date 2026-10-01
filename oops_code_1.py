class Student:
    """
    Demonstrates the difference between class attributes and instance attributes.

    The 'school' attribute belongs to the Student class, so it is shared
    across all Student objects.

    The 'name' and 'marks' attributes belong to individual objects through
    'self', so each object maintains its own independent state.

    Updating s1.name changes only s1's state; s2 remains unchanged because
    s1 and s2 are separate instances.
    """

    school = "Repulic of Happiness"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("JOYBOY", 90)
s2 = Student("NIKA", 85)

s1.name = "LUFFY"

print(f"\nMarks Obtained: {s1.marks} by {s1.name} and the School is {s1.school}\n")
print(f"\nMarks Obtained: {s2.marks} by {s2.name} and the School is {s2.school}\n")