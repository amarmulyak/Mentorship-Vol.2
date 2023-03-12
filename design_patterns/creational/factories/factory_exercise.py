'''
Factory Coding Exercise

You are given a class called Person. The person has two attributes: id, and name.

Please implement a PersonFactory that has a non-static create_person() method that takes a person's name
and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created. So, the first person the factory makes
should have id=0, second id=1 and so on.
'''

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
