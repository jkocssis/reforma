class Ambiente:
  def __init__(self,nome,altura,largura,comprimento):
    """Realiza o calculo de Metragem
    em ambientes, para uma reforma, já com 10% de acréscimo""" 
    self.nome = nome
    self.altura = altura
    self.largura = largura
    self.comprimento = comprimento

  def piso(self):
    """ calcula a metragem para o piso"""
    return round(self.largura * self.comprimento * 1.10,2)

  def parede1(self):
    """calcula a metragem para parede """
    return round(self.altura * self.largura *  1.10,2)
  
  def parede2(self):
    """calcula a metragem para parede """
    return round(self.altura * self.comprimento * 1.10,2)
  
  def somaParede(self):
    """calcula a metragem total para parede """
    return round(2*(self.parede1() + self.parede2()),2)
  
  def total(self):
    """calcula a metragem total """
    return round(self.somaParede() + self.piso(),2)
  

  def relatorio(self):
    print(str(self.nome) + " (com + 10%) :")
    print("Piso : " + str(self.piso()) + "m2")
    print("Parede 1 : " + str(self.parede1()) + "m2")
    print("Parede 2 : " + str(self.parede2()) + "m2")
    print("Metragem paredes : " + str(self.somaParede()) + "m2")
    print("Metragem Total : " + str(self.total()) + "m2")
    print()



  



if __name__ == "__main__":
  quarto = Ambiente("Quarto", 2.87, 2.87, 2)
  quarto.relatorio()
  cozinha = Ambiente("Cozinha",2.87, 3.63, 3.79 )
  cozinha.relatorio()
  