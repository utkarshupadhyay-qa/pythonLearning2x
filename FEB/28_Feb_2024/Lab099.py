# Hierarchical Inheritance

class Father:
    def home(self):
        return "This is a Father"


class Utkarsh(Father):
    pass
    # def home(self):
    #     return "This is a Utkarsh  Home"

class SisUtkarsh(Father):
    def home(self):
        return "This is a bicycle."


utkarsh = Utkarsh()
print(utkarsh.home())