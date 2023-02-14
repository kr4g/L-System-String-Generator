from lsystem_axioms import AxiomDict

class LSystemGenerator:
    def __init__(self, axiom_dict: AxiomDict):
        """
        Initialize the L-system generator with the selected axiom dictionary.

        Parameters:
            - axiom_dict (AxiomDict): The axiom dictionary for the L-system to be generated.
        """
        self.axiom_dict = axiom_dict
        self.variables = set(axiom_dict.value['variables'])
        self.constants = set(axiom_dict.value['constants'])
        self.axiom = axiom_dict.value['axiom']
        self.rules = axiom_dict.value['rules']
        self.memo = {}

    def set_variable(self, variable: str, new_value: str) -> None:
        """
        Update the value of a variable in the set of variables.

        Parameters:
            - variable (str): The variable to update in the set of variables.
            - new_value (str): The new value for the variable
        """
        if variable not in self.variables:
            raise ValueError(f'{variable} is not a variable')
        self.variables.add(variable)
        self.constants.discard(variable)
        self.rules[variable] = new_value

    def set_constant(self, constant: str, value: str) -> None:
        """
        Set the value of a constant.
        
        Parameters:
            - constant (str): The constant to set the value for.
            - value (str): The value to set the constant to.
        """
        self.constants[constant] = value

    def generate(self, n: int) -> str:
        """
        Generate an L-system string of length n using the axiom and rules from the selected axiom dictionary.

        Parameters:
            - n (int): The number of iterations to apply the production rules.

        Returns:
            - str: The generated L-system string.
        """
        if n == 0:
            return self.axiom
        if n in self.memo:
            return self.memo[n]
        else:
            current_str = self.axiom
            for i in range(n):
                current_str = self._apply_rules(current_str)
                self.memo[i+1] = current_str
            return current_str

    def _apply_rules(self, string: str) -> str:
        """
        Apply the production rules to the input string.

        Parameters:
            - string (str): The input string to which the production rules are applied.

        Returns:
            - str: The resulting string after applying the production rules.
        """
        result = []
        for c in string:
            if c in self.rules:
                result.append(self.rules[c])
            else:
                result.append(c)
        return ''.join(result)
    
    def interpolate(self, i: int, n: int) -> str:
        """
        Interpolate between the initial axiom and the final L-system string at a specific iteration.
        
        Parameters:
            - i (int): The current iteration number.
            - n (int): The total number of iterations.
        
        Returns:
            - str: The interpolated L-system string.
        """
        final_string = self.generate(n)
        initial_string = self.axiom
        ratio = i / n
        current_string = ""
        for c1, c2 in zip(initial_string, final_string):
            current_string += chr(int(ord(c1) + (ord(c2) - ord(c1)) * ratio))
        return current_string


if __name__ == "__main__":
    # import sys
    # try:
    #     l_system_name, iterations = sys.argv[1], int(sys.argv[2])
    # except ValueError:
    #     print("Invalid input. Please input L-system name and number of iterations.")
    #     sys.exit()
    # except IndexError:
    #     print("Invalid input. Please input L-system name and number of iterations.")
    #     sys.exit()
        
    # l_system = None
    # for system in AxiomDict:
    #     if system.name.lower() == l_system_name.lower():
    #         l_system = system
    #         break
    # if l_system is None:
    #     l_system = AxiomDict.Algae
        
    # print(l_system)
    # generator = LSystemGenerator(l_system)
    # print(f'Iteration 0: {generator.generate(0)}')
    # for i in range(1, iterations+1):
    #     generated_string = generator.generate(i)
    #     print(f"Iteration {i}: {generated_string}")
    if __name__ == "__main__":
        axiom_dict = AxiomDict.GPT3_Variation
        # axiom_dict = AxiomDict.Fractal_Plant
        generator = LSystemGenerator(axiom_dict)

        for i in range(5):
            print(f"Iteration {i + 1}: {generator.generate(i)}")

