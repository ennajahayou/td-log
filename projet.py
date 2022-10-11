class armes:
    def __init__(self,ammunitions:int,range:int) -> None:
        self.ammunitions=ammunitions
        self.range=range
    def fire_at(self,x:int,y:int,z:int):
        if self.ammunitions== 0:
            print('NoAmmunitionError')
        else:
            if self.range< z :
                self.ammunitions= self.ammunitions-1  

#        print(f'fire enemy{x,y,z}')    


Lance_missilesantisurface=armes(40,30)
Lance_missiles_anti_air=armes(50,40)
lance_torpilles=armes(15,20)

