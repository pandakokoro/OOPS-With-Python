
class Student:
    """
    Demonstrates encapsulation through controlled attribute access.

    The school attribute is shared at the class level.
    Each student maintains independent instance data.

    The marks property allows reading marks but prevents
    direct reassignment through the public marks attribute.
    """

    school = "Republic of Happiness"

    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):
        """Return the student's marks without a public setter."""
        return self._marks


s1 = Student("JOYBOY", 90)
s2 = Student("NIKA", 85)

s1.name = "LUFFY"


print(f"{s1.name} | {s1.marks} | {s1.school}")
print(f"{s2.name} | {s2.marks} | {s2.school}")

# Try this:
# s1.marks = 100