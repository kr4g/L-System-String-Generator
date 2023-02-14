from lsystem_axioms import AxiomDict
from lsystem_generator import LSystemGenerator
from typing import List, Tuple

class SuperLSystemGenerator:
    def __init__(self, lsystems: List[Tuple[LSystemGenerator, int]]):
        self.lsystems = lsystems

    def generate(self, iterations: int) -> str:
        result = ""
        for generator, iters in self.lsystems:
            result += generator.generate(n=iters)
        return result

if __name__ == "__main__":
    koch_curve = LSystemGenerator(AxiomDict.Koch_Curve)
    sierpinski_triangle = LSystemGenerator(AxiomDict.Sierpinski_Triangle)

    super_system = SuperLSystemGenerator([(koch_curve, 2), (sierpinski_triangle, 3)])
    print(super_system.generate(iterations=1))

