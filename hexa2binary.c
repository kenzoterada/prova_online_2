#include <stdio.h>
#include <stdlib.h>
#include <string.h>

union float_bytes {
    float f; 
    char b[sizeof(float)];
};

void hexa2binary(float f) {
    union float_bytes fb = { f };
    char verifica;
    
    for (int i = 0; i < sizeof(float); i++) {
        verifica = fb.b[i];

        // Cada iteracao a variavel verifica recebe os valores os valores em bytes de fb.b[i]

        printf("%hhx\n", fb.b[i]);
        
        // Conversão do byte para binário
        char binario[9]; // Armazena o valor binário

        memset(binario, 0, sizeof(binario)); // Inicializa com zeros
        
        for (int j = 7; j >= 0; j--) {
            //A variavel verifica que possui os valores dos bytes é ultilizada para seus caracteres serem
            //modificados de hexadecimal para binário
            int bit = (verifica >> j) & 1;
            /*Essa linha ultiliza a operacao de deslocamento movendo o bit para uma posicao menos significativa
              sendo assim o resultado da operacao é 1 se o bit for 1 e 0 caso o bit seja 0.
            */
            
            binario[7 - j] = bit + '0';
            /* Adiciona o dígito binário na variável binario, essa parte garante também que os números sejam alocados
            de maneira correta na string, sendo assim facil de ser interpretado porteriormente, já que o número 
            binário será ultilizado na função em python para calcular o valor em decimal
            */
        }
        
        printf("%s\n", binario);
        //os valores da variável binário serão ultilizados no código em python para gerar os valores em decimais.

    }
}

float f1 = 1.2347e+39;
float f2 = 1.2347e+38;
float f11 = 1.2347e-38;
float f12 = 1.2347e-39;
float f13 = 1.2347e-42;
float f14 = 1.2347e-45;
float f15;

float teste_quest_6_1 = 1.401298e-45;
float teste_quest_6_2 = 1.985345e-45;
float teste_quest_6_3 = 2.123456e-45;
float teste_quest_6_4 = 2.537821e-45;
float teste_quest_6_5 = 2.802597e-45;

int main(void) {

    /*Quando a funcao hexa2binary for chamada será impressos os seguintes intens na tela:
    a representação hexadecimal do byte em questão que está sendo tratado na iteração do primeiro for 
    da função, e o seu valor correspondente em binário de 8 bits, os bytes juntos analizados compõem o valor que
    será ultilizado no código em python.
    Vale ressaltar que os números que são printados na tela da função hexa2binary estão em ordem contrária a qual
    irei ultilizar no próximo programa. Ou seja, a saída a saída da função para número da variável f11 são:
    0x6a/0x72/0x86/0x00 devem ser ultilizado ao contrário, do 00 para o 6a. Não fiz nenhuma função ou arquivo txt
    o qual importe dessde programa para o outro, fiz apenas 4 vetores do tipo inteiro que armazenam o valor dos 4
    numeros decimais em ordem contrária da qual é printada os valores em hexadecimal neste programa aqui.
    */
    puts("f11\n");
    hexa2binary(f11);

    puts("f12\n");
    hexa2binary(f12);

    puts("f13\n");
    hexa2binary(f13);

    puts("f14\n");
    hexa2binary(f14);
    
    printf("#######################\n");
    printf("Testes para questao 6: \n");
    
    puts("teste_quest_6_1\n");
    hexa2binary(teste_quest_6_1);

    puts("teste_quest_6_2\n");
    hexa2binary(teste_quest_6_2);

    puts("teste_quest_6_3\n");
    hexa2binary(teste_quest_6_3);

    puts("teste_quest_6_4\n");
    hexa2binary(teste_quest_6_4);
    
    puts("teste_quest_6_5\n");
    hexa2binary(teste_quest_6_5);
    

    return 0;
}
