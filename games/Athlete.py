class Athlete:
    """Athlete class"""
    def _init_(self, name):
        self.name = name

    def _str_(self):
        return f"Athlete: {self.name}"
    
    def _repr_(self):
        return f"Athlete('{self.name}')"
    
    def display(self):
        print(f"{self.name}")

if _name_ == "_main_":
    a = Athlete("Ana G.")
    a.display()
    print(a)
    print(repr(a))
    print(f"a: {id(a)}")
    
    b = eval(repr(a))
    print(b)
    print(f"b: {id(b)}")