from chair import Chair
class Salon_bir_seans_bir(Chair):
    all_chair=[]
    remove_chair=[]
    for i in range(100):
        all_chair.append(i+1)
    def __init__(self, name, surname, age, chair,sinema,seans):
        super().__init__(name, surname, age, chair,sinema,seans)
    
            
    