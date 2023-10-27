#Área de criação de métodos
import this
this.num1 = 0 #Declarando e Instanciando uma Variavél
this.num2 = 0 #Declarando e Instanciando uma Variavél



#retornar a soma dos parâmetros num1 e num2
def somar(num1,num2):
    return num1 + num2

#retornar a subtração dos parâmetros num1 e num2
def subtrair(num1,num2):
    return num1 - num2

#retornar a multiplicação dos parâmentros num1 e num2
def multiplicar(num1,num2):
    return num1 * num2

#retornar a divisão dos parâmentros num1 e num2
def dividir(num1,num2):
    if num2 <= 0:
        return "Impossivel Dividir!"
    else:
        return num1 / num2

def coletar():
    this.num1 = int(input('Informe um número: '))  # leia - coleta os dados
    this.num2 = int(input('Informe um número: '))

def imprimir():
    return('\n A soma de {} e {} é {}'.format(this.num1,this.num2, somar(this.num1,this.num2))
          + "\n A subtração de {} e {} é {}".format(this.num1,this.num2, subtrair(this.num1,this.num2))
          + "\n A Multiplicação de {} e {} é {}".format(this.num1,this.num2, multiplicar(this.num1,this.num2))
          + '\n A divisão de {} e {} é {}'.format(this.num1,this.num2, dividir(this.num1,this.num2))
          + ' \n O maior número é {}'.format(comparar()))  # Print é o escreval = mostra no console o resultado do método

def comparar():
        if this.num1 > this.num2:
            return this.num1
        else:
            return this.num2



if __name__ == '__main__':
#Área de Execução de métodos
    coletar()#chamando o método que coleta 2 números
    print(imprimir())






