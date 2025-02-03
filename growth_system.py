# growth_system.py
from .lsystem import LSystemParser
from .parameters import GrowthParameters

class GrowthSystem:
    def __init__(self):
        self.parser = LSystemParser()
        self.params = GrowthParameters()
        
    def initialize(self):
        self.parser.setup_default_rules()
        self.params.setup_parameters()
        
    def generate_growth(self, iterations=3):
        current = 'X'
        
        for _ in range(iterations):
            new = ''
            for char in current:
                new += self.parser.rules.get(char, char)
            current = new
            
        self.parser.interpret_string(
            current,
            angle=self.params.node.parm('angle').eval(),
            length=self.params.node.parm('length').eval()
        )

# __init__.py
from .lsystem import LSystemParser
from .parameters import GrowthParameters
from .growth_system import GrowthSystem

__all__ = ['LSystemParser', 'GrowthParameters', 'GrowthSystem']
