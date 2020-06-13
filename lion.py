"""A lineo."""
import animal
class Lion(animal.Animal):
    def __init__(self):
        self.kind='linon'
    def get_kind(self):
        return self.kind
    def tukekuwae(self):
        return 'tukekuwae desu'
