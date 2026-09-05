#include <iostream>
#include "Pilha.h"

int main(){

    Pilha pilha1;
    TipoItem item;
    int opcao;

    std::cout << "Programa gerador de pilhas\n";

    do {
        std::cout << "Digite 0 para parar o programa!\n";
        std::cout << "Digite 1 para inserir um elemento!\n";
        std::cout << "Digite 2 para remover um elemento!\n";
        std::cout << "Digite 3 para imprimir pilha!\n";
        std::cout << "Digite sua opcao: ";
        std::cin >> opcao;
        switch (opcao)
        {
        case 0:
            break;
        case 1:
            std::cout << "Digite o elemento a ser inserido: ";
            std::cin >> item;
            std::cout << "\n";
            pilha1.inserir(item);
            std::cout << "Item adicionado\n";
            break;
        case 2:
            item = pilha1.remover();
            std::cout << "Elemento Removido: " << item << std::endl;
            break;
        case 3:
            pilha1.imprimir();
            break;
        
        default:
            std::cout << "Escolha uma opcao valida!\n";
            break;
        }


    } while (opcao !=0);
    

    system("pause");
    return 0;
}