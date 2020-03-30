class Garden:
    _PLANTS = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets',
    }

    _diagram = ''

    _students = [
        'Alice',
        'Bob',
        'Charlie',
        'David',
        'Eve',
        'Fred',
        'Ginny',
        'Harriet',
        'Ileana',
        'Joseph',
        'Kincaid',
        'Larry',
    ]

    def __init__(self, diagram, /, students=None):
        self._diagram = diagram.split()

        if students is not None:
            self._students = sorted(students)

    def plants(self, name: str) -> [str]:
        """Returns the names of all the plants owned by a given student"""
        plants_index = self._get_plants_index(name)
        plants = self._get_diagram_values(plants_index)

        return [self._PLANTS[plant] for plant in plants]

    def _get_diagram_values(self, row_indexes: ()):
        """Returns an list containing the values of all the rows in the diagram at indexes passed by argument"""
        return [row[i] for row in self._diagram for i in row_indexes]

    def _get_plants_index(self, name: str) -> ():
        """Returns a tuple containing the index of each row of the diagram containing the plants of the give name"""
        student_index = self._students.index(name)
        diagram_index = student_index * 2

        return diagram_index, diagram_index + 1
