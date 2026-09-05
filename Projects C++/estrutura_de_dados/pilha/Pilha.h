typedef int TipoItem;
const int max_itens = 100;


class Pilha{
    private:
    int tamanho;
    int* estrutura;

    public:
    Pilha(); //construtora
    ~Pilha(); //destrutora

    bool esta_cheia(); // verifica se a pilha esta cheia
    bool esta_vazia(); // verifica se a pilha esta vazia

    void inserir(TipoItem item); // Inserir elementos; PUSH
    TipoItem remover(); //pop
    void imprimir(); //print
    int qualtamanho(); //lenght
};