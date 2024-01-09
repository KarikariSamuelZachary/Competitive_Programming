from unicodedata import name


class Person:
    def __init__(self, name: str, house):
        self.name= name
        self.house= house

    def __str__(self):
        return f"{self.name} from {self.house}"


samuel= Person("Samuel", "Gryffindor")
print(samuel)