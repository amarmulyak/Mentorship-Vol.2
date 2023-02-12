'''
Builder Coding Exercise

You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
The expected output of the above code is:

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
Please observe the same placement of spaces and indentation.
'''

class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = {}

    def add_field(self, type, name):
        self.fields[type] = name
        return self

    def __str__(self):
        indent_2 = ' ' * 2
        indent_4 = indent_2 * 2
        return \
        'class {class_name}:\n' \
        '{indent_2}def __init__(self):\n' \
        '{indent_4}self.name = {name_field}\n' \
        '{indent_4}self.age = {age_field}'.format(
            class_name=self.root_name,
            indent_2=indent_2,
            indent_4=indent_4,
            name_field=self.fields['name'],
            age_field=self.fields['age']
        )

cb = CodeBuilder('Person')
cb \
    .add_field('name', 'Bob') \
    .add_field('age', 25)

print(cb)
