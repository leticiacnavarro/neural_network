import numpy as np
import matplotlib.pyplot as plt

# Classe para auxiliar nas chamadas
class Polinomio:
  def __init__(self, vetor):
      
    # Salvando o vetor
    self.vetor = vetor
  
  # Funcao para mostrar a expressao do polinomio
  def expressao(self):

    # Funcao para calcular o que acompanhará o polinomio de acordo com seu grau
    def exp_grau(valor):
      # se o grau for 0, não vai ter nada
      if valor == 0:
        aux = ""
      # se for 1, vai ter o X
      elif valor == 1:
        aux = "*x"
      # se não, vai ser o X elevado a potencia
      else:
        aux = "*x**" + str(valor)
      return aux
    
    exp = ""
    # Pegando o tamanho do vetor e tirando '1' para considerar o grau '0'
    graus = len(self.vetor) -1
    # Percorrendo o tamanho inteiro do vetor
    for i in range(0, len(self.vetor)):
      # Obtendo o módulo da subtração entre a posição e a quantidade de graus
      grau = abs((i) - graus)
      # Acrescentando na expressao o valor do coeficiente mais o 'X' e a potência correspondente
      exp += str(self.vetor[i]) + exp_grau(grau) + " +"
      # retira o ultimo '+' e retorna a expressão
    return exp[:-1]

  # Retorna os coeficientes da derivada da função polinomial
  def derivada(self):
    #lista de coeficientes
    coeficientes = []
    # lista de potencias
    potencia = len(self.vetor) - 1
    for i in range(0, len(self.vetor)):
      # multiplicando o coeficiente atual com a potência correspondente ('derivando')
      coeficientes.append(self.vetor[i] * potencia)
      # decrementa a potencia
      potencia -=1 
    # Se o ultimo elemento for um 0, excluir
    if coeficientes[len(coeficientes) - 1] == 0:
     coeficientes = coeficientes[:-1] 
     # retorna a lista de coeficientes
    return Polinomio(coeficientes)

# calcula o valor do Y com base na função
  def __call__(self, x):
    y = 0
    for index, coeficiente in enumerate(self.vetor[::-1]):
      y += coeficiente * x ** index
    return y

## Funcao da descida do gradiente
def descendo(funcao, x0, alpha):
  x_array = []
  # calculando o gradiente com a função derivada da classe de polinomio
  gradiente = lambda x: eval((funcao.derivada()).expressao())
  # definindo um maximo de iteracoes
  maximo_iteracoes = 70 
  for iteracao in range(0, maximo_iteracoes):
    # guarda o valor de x no x_aux 
    x_aux = x0 
    # calculando o gradiente descendente
    x0 = x0 - alpha * gradiente(x_aux)  

    x_array.append(x0)   

  return x_array, x0



## QUESTÕES

vetor = [-1, -3, 3, 5]

## QUESTAO 01

p = Polinomio(vetor)
print("Polinômio: " + p.expressao())

## QUESTA0 02

p_derivada = p.derivada()
print("Derivada do polinômio: " + p_derivada.expressao())

## QUESTAO 03

# chamando a função com x0 = 0 e taxa de aprendizagem = 0.02 e recebendo um array dos valores para poder imprimir a descida
x_array, x0 = descendo(p, 0, 0.02)
print("Local mínimo: {:.2f}".format(round(x0, 2)))

# Imprimindo os gráficos

x = np.linspace(-4, 3, 50, endpoint=True)
y = p(x)
y2 = p_derivada(x)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Colocando os eixos no meio da figura para mostrar aonde corta
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_xlim([-3.5, 3.5])
ax.set_ylim([-8, 8])

plt.plot(x,y, 'm')
plt.plot(x,y2, 'b')

# imprimindo a descida
for x_descida in x_array:
  plt.plot(x_descida,p(x_descida),'co')

# imprimindo mínimo local
plt.plot(x_array[-1], p(x_array[-1]), 'r*',  markersize= 10)

plt.show()

