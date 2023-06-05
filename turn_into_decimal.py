vetor_f11 = [0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0]

vetor_f12 = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1]

vetor_f13 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1]

vetor_f14 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

'''

Os valores dos vetores f11, f12, f13, f14 são os valores da varíavel binário do código em C posterior.
A variável binario do código em C a cada iteração do for convertia o valor de hexadecimal para binário,
assim como foi explicado nos comentários na função main do código anterior.

'''

def frac2dec(vetor):
    decimal = 0
    #variável que será ultilizada para receber o valor da conversão

    for i, digito in enumerate(vetor):
        '''
        fiz o uso do laço com o enumerato assim eu consigo pegar mais facilmente o valor dos índices do
        vetor e com a variavel i é facil tambem conseguir o índice o qual eu desejo a cada iteração 
        '''
        decimal += digito * 2**(-i-1)
        '''
        calculo para efetuar a conversão de número binário para decimal, a operação faz o calculo de conversão
        da mesma maneira a qual foi apresentada em aula.
        '''
    return decimal

def bin2dec(vetor):
    '''
    função feita para combinar concatenar e transformar os dados passados como parâmetros em uma única
    string, convertendo bits para decimal concatenando a string e fazendo um type cast para converter
    o valor para int e ser ultilizado posteriormente.
    '''
    numero_binario = ''.join(str(digito) for digito in vetor)
    return int(numero_binario, 2)


def vetor_inteiros_eh_subnormal(vetor):
    numero_binario = ''.join(str(digito) for digito in vetor)
    '''
    concatena os elementos passados como parametro com espaços vazios entre eles para serem iterados 
    depois pela funcao is_subnormal.
    '''
    return is_subnormal(numero_binario)

def is_subnormal(numero_binario):

    '''
    Para a representação de numeros de ponto flutuante em computadores no formato IEE 754
    existem as formatações normal e subnormal (ou denormal) as duas servem para representar
    números de ponto flutuante, todavia quando precisa representar um número o qual o objetivo da 
    representação é abranger um número grande de digitos do número a representação normal é mais
    indicada, todavia essa representação mais abrangente falha no quesito de precisão.

    Se o objetivo da representação é com números extremamente pequenos que beiram o 0
    com um intervalo menor entre os digitos, existe uma limitação no formato I três E, mas mesmo 
    com essas limitações os números extremamente pequenos ainda podem ser presentados pela
    representação sub-normal. 

    Na representação de 32 bits, o primeiro bit é o bit de sinal, se o primeiro bit for 1 a contade sinal
    que é execatada na fução iee754 vai resultar em -1, ou seja, número negativo, caso contrário a conta
    resultará em 1 que é um resultado positovo.
    Os 8 bits que ficam após o bit de sinal correspondem ao expoente que é o número para deslocamento
    deslocamentos da vírgula, no caso da representação de 32 bits há um viés de 127, o expoente pode
    ser positivo, negativo ou zero, dependendo do intervalo de valores representáveis.
    Na representação subnormal todos os valores dos bits que representam o expoente são 0,
    sendo assim nas operações da função ieee754 o valor do expoente é tratado como -126 (deslocamento de -127 + 1).
    Sendo assim a representação varia de -126 e 127.

    A mantissa é composta pelos números posteirores ao que representam o expoente, é basicamente uma sequencia de
    bits que seguem o bit implícito, possui 23 bits (bit 9 ao 31), a única diferença da formatação normal
    e subnormal é o bit implicito o qual na normal é 1 e na subnormal é 0.

    Pontos a se ressaltar:
    Existe arredondamento nas transformações numéricas de binário para decimal no formato IEEE754
    Em números extremamente pequenos oue extremamente grandes além da falta de precisão do formato, existe os problemas de
    overflow e underflow.
    '''

    expoente = numero_binario[1:9]
    mantissa = numero_binario[9:]

    if all(bit == '0' for bit in expoente) and any(bit == '1' for bit in mantissa):
        return True

    return False


def ieee754(v):
  sinal = (-1)**v[0]

  if vetor_inteiros_eh_subnormal(v):

    return sinal * 2**(-126) * (frac2dec(v[9:]))
    '''
    calculo para um número que necessita de precisão subnormal, consideramos o expoente como -126,
    depois calculamos o valor da mantissa usando a funçao de calculo para decimal.
    '''
  else:

    return sinal * 2**(bin2dec(v[1:9]) - 127) * (1*2**0 + frac2dec(v[9:]))
  '''
  função para calculo do número normalizado, o calculo do expoente é feito pela função bin2dec e subtraído
  127 que é o número de viés. E a mantissa é calculada com a soma de 1 que é o bit implicito.
  '''


def numero_subnormal(valor_calculado):
    # Valor mínimo normalizado
    menor_normalizado = 2 ** (-126)

    # Verificar se o valor absoluto é menor que o menor valor normalizado
    if abs(valor_calculado) < menor_normalizado:
        return True
    else:
        return False


tupla_verificacao = (ieee754(vetor_f11),
            ieee754(vetor_f12),
            ieee754(vetor_f13),
            ieee754(vetor_f14)
        )       

for tupla in tupla_verificacao:
    print(tupla)

    if numero_subnormal(tupla):
       print("representaçaõ subnormal\n")
    else:
        print("representação normal\n")


print("################################################################")




'''

def precisa_de_calculo_subnormal(vetor):
    sinal = (-1)**vetor[0]
    return sinal * 2**(bin2dec(vetor[1:9]) - 127) * (1*2**0 + frac2dec(vetor[9:]))

tupla_2 = (precisa_de_calculo_subnormal(vetor_f11),
            precisa_de_calculo_subnormal(vetor_f12),
            precisa_de_calculo_subnormal(vetor_f13),
            precisa_de_calculo_subnormal(vetor_f14)
        )

for tupla in tupla_2:
   print(tupla)

x = int(10)
for t1, t2 in zip(tupla_1, tupla_2):
    x+=1
    if t1 == t2:
        print("o numero f",x")
    else:
        print("o numero f",x)
'''
