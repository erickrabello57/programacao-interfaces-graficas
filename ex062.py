# Defina uma classe ObjetoGrafico, subclasse de object, cujos atributos são:
# cor de preenchimento, inteiro
#preenchido, booleano
# cor de contorno, inteiro

# Defina outras três classes, subclasses da classe ObjetoGrafico

# Retangulo, com atributos base e altura
# Circulo, com atributo raio
# Triangulo, com atrubutos base e altura

# Todas as subclasses de objeto grafico devem possuir area e perimetro


import math

class ObjetoGrafico(object):
    def __init__(self, corPreenchimento, estaPreenchido, corContorno):
        self.corPreenchimento = corPreenchimento
        self.estaPreenchido = estaPreenchido
        self.corContorno = corContorno

class Retangulo(ObjetoGrafico):
    def __init__(self, corPreenchimento, estaPreenchido, corContorno, base, altura):
        super(Retangulo, self).__init__(
            corPreenchimento, estaPreenchido, corContorno)
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def area(self):
        return self.base * self.altura

class Circulo(ObjetoGrafico):
    def __init__(self, raio):
        super(Circulo, self).__init__(corPreenchimento=0,
                                      estaPreenchido=False, corContorno=0)
        self.raio = raio
        self.diametro = raio * 2

    def area(self):
        return 3.14 * self.raio**2

    def perimetro(self):
        return 2 * 3.14 * self.raio

class Triangulo(ObjetoGrafico):
    def __init__(self, base, altura):
        super(Triangulo, self).__init__(
            corPreenchimento=0, estaPreenchido=False, corContorno=0)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2 
        
        

    # para cálulo do perímetro supõe-se um triângulo retângulo, já que temos conhecimento apenas da base e altura do mesmo

    def perimetro(self):
        hipotenusa = math.sqrt((self.base ** 2) + (self.altura**2))
        return hipotenusa + self.base + self.altura 

baseRetangulo = float(input("Entre com a base do retângulo: "))
alturaRetangulo = float(input("Entre com a altura do retângulo: "))
baseTriangulo = float(input("Entre com a base do triângulo: "))
alturaTriangulo = float(input("Entre com a altura do triângulo: "))
raioCirculo = float(input("Entre com o raio do círculo: "))

retangulo = Retangulo(0, False, 0, baseRetangulo, alturaRetangulo)
triangulo = Triangulo(baseTriangulo, alturaTriangulo)
circulo = Circulo(raioCirculo)


print("Retângulo: ", retangulo.__dict__)
print("Área: ", retangulo.area())
print("Perímetro: ", retangulo.perimetro())
print("="*20)
print("Triângulo: ", triangulo.__dict__)
print("Área: ", triangulo.area())
print("Perímetro: ", triangulo.perimetro())
print("="*20)
print("Círculo: ", circulo.__dict__)
print("Área: ", circulo.area())
print("Perímetro: ", circulo.perimetro())
print("="*20)
