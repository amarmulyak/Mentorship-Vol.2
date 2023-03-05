class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    index = 0
    person_initialized = []

    def create_person(self, name):
        person = Person(self.index, name)
        self.index += 1
        self.person_initialized.append(person)

        return person

    def __str__(self):
        output = ''
        for person in self.person_initialized:
            output += f'Person(id={person.id}, name={person.name})\n'
        return output

if __name__ == '__main__':
    person_factory = PersonFactory()
    person_factory.create_person('Anna')
    person_factory.create_person('Ira')

    print(person_factory)
