from enum import Enum

class AxiomDict(Enum):
    """ Enum containing different axiom dictionaries """
    # Example 1: Algae
    Algae = {
        'axiom': 'A',
        'rules': {
            'A': 'AB',
            'B': 'A'
        },
        'variables': ('A', 'B'),
        'constants': None
    }
    # Example 2: Fractal Plant
    Fractal_Plant = {
        'axiom': 'X',
        'rules': {
            'X': 'F-[[X]+X]+F[+FX]-X',
            'F': 'FF'
        },
        'variables': ['X', 'F'],
        'constants': ['[', ']', '+', '-']
    }
    # Example 3: Sierpinski Triangle
    Sierpinski_Triangle = {
        'axiom': 'A',
        'rules': {
            'A': 'B-A-B',
            'B': 'A+B+A'
        },
        'variables': ['A', 'B'],
        'constants': ['+', '-']
    }
    # Example 4: Dragon Curve
    Dragon_Curve = {
        'axiom': 'FX',
        'rules': {
            'X': 'X+YF+',
            'Y': '-FX-Y'
        },
        'variables': ['X', 'Y', 'F'],
        'constants': ['+', '-']
    }
    # Example 5: Koch Curve
    Koch_Curve = {
        'axiom': 'F',
        'rules': {
            'F': 'F+F-F-F+F'
        },
        'variables': ['F'],
        'constants': ['+', '-']
    }
    # Example 6: Sierpinski Arrowhead Curve
    Sierpinski_Arrowhead_Curve = {
        'axiom': 'A',
        'rules': {
            'A': 'B-A-B',
            'B': 'A+B+A'
        },
        'variables': ['A', 'B'],
        'constants': ['+', '-']
    }
    # Example 7: Hilbert Curve
    Hilbert_Curve = {
        'axiom': 'A',
        'rules': {
            'A': '-BF+AFA+FB-',
            'B': '+AF-BFB-FA+'
        },
        'variables': ['A', 'B', 'F'],
        'constants': ['+', '-']
    }
    # Example 8: Peano Curve
    Peano_Curve = {
        'axiom': 'F',
        'rules': {
            'F': 'F+F-F-F-F+F+F-F'
        },
        'variables': ['F'],
        'constants': ['+', '-']
    }
    # Example 9: Levy C Curve
    Levy_C_Curve = {
        'axiom': 'F',
        'rules': {
            'F': '+F--F+'
        },
        'variables': ['F'],
        'constants': ['+', '-']
    }
    # Example 10: GPT3 Variation
    GPT3_Variation = {
        'variables': ('A', 'B', 'F', 'G', 'X', 'Y'),
        'constants': ('+', '-', '[' ,']'),
        'axiom': 'A',
        'rules': {
            'A': 'B-[F]-G-A-B',
            'B': '[F]+G+A+B+A',
            'F': 'F-G+F+G-X',
            'G': 'Y+G+Y',
            'X': 'Y-[-X]-Y',
            'Y': '[F]+Y+X'
        }
    }

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Variables: {self.value["variables"]}\n' \
               f'Constants: {self.value["constants"]}\n' \
               f'Axiom: {self.value["axiom"]}\n' \
               f'Rules: {self.value["rules"]}'

# if __name__ == '__main__':
#     import sys
#     import random
#     # Example usage of AxiomDict enum class
#     if len(sys.argv) == 1:
#         lsystem = random.choice(list(AxiomDict))
#         print(lsystem)
#     else:
#         lsystem_name = sys.argv[1]
#         try:
#             lsystem = AxiomDict[lsystem_name]
#             print(lsystem)
#         except KeyError:
#             print(f'{lsystem_name} not found in the available L-systems.')
if __name__ == '__main__':
    import sys

    input_name = None
    if len(sys.argv) > 1:
        input_name = sys.argv[1].lower()
    if input_name:
        found = False
        for l_system in AxiomDict:
            if l_system.name.lower() == input_name:
                print(l_system)
                found = True
                break
        if not found:
            print(f"L-system with name {input_name} not found.")
    else:
        import random
        print(random.choice(list(AxiomDict)))
