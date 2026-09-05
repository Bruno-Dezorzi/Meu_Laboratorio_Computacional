#include <stdio.h>
#include <stdlib.h>

int main(){

    int var = 15;

    int* ptr;

    ptr = &var;

    printf("Conteudo de var = %d\n", var);
    printf("Endereco de memoria de var = %p\n", &var);


    printf("Conteudo de apontado por ptr = %d (no caso esse valor pertence a var) \n", *ptr);
    printf("Endereco de memoria que o ptr aponta = %p\n", ptr);
    printf("Endereco de memoria de ptr = %p\n", &ptr);

    // Atualizando o valor da minha variavel var através do ponteiro

    *ptr = 75;
    printf("Conteudo de var = %d\n", var);

    while(1);
    return 0;

}