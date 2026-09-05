#include <iostream>
#include "Pilha.h"



    Pilha::Pilha(){

        tamanho = 0;
        estrutura = new TipoItem[max_itens];
    } 

    Pilha::~Pilha(){
        delete [] estrutura;
    } 

    bool Pilha::esta_cheia(){
        return( tamanho == max_itens);
    }

    bool Pilha::esta_vazia(){
        return( tamanho == 0);
    }

    void Pilha::inserir(TipoItem item){

        if (esta_cheia()){
            std::cout << "A pilha esta cheia!\n";
            std::cout << "Nao e possivel inserir nenhum elemento\n";
        }
        else{
            estrutura[tamanho] = item;
            tamanho++;
        }
    }

    TipoItem Pilha::remover(){
        if (esta_vazia()){
            std::cout << "A pilha esta vazia\n";
            std::cout << "Não tem como remover nenhum elemento\n";
            return 0;
        }
        else{
            tamanho--;
            return estrutura[tamanho];
        }
    }

    void Pilha::imprimir(){
        std::cout << "Pilha: [ ";
        for (int i=0; i<tamanho; i++){
            std::cout << estrutura[i] << " ";

        }
        std::cout << "]\n";
    }

    int Pilha::qualtamanho(){
        return tamanho;
    }