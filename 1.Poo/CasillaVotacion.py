class CasillaVotacion:
    def __init__(self,identificador , pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
    
    @property
    def region(self):
        return self.__region
    
    @property
    def pais(self):
        return self.__pais
    
    @region.setter
    def region(self , region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.pais}')

casilla = CasillaVotacion(123,['Ciudad de Mexico','Morelos'])
