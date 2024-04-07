class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        
class Figur:
    def __init__(self):
        self.name = "Figur1"
        
    def umfang(self):
        return 0
    
    def __str__(self):
        return self.name
        
    
class Dreieck(Figur):
    def __init__(self, name, a, b, c):
        super().__init__()
        self.name = name
        self.a = a
        self.b = b
        self.c = c
    
    def umfang(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return "Dreieck a=" + str(self.a) + " b=" + str(self.b) + " c=" + str(self.c) + " U=" + str(self.umfang())
            
class Rechteck(Figur):
    def __init__(self, name):
        super().__init__(name)
        
class Kreis(Figur):
    def __init__(self, name):
        super().__init__(name)
        
class Polygon(Figur):
    def __init__(self, name):
        super().__init__(name)
    
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

testdreieck = Dreieck("Dreieck_1", 4, 3,3)
print(testdreieck)


    