#include <iostream>

class No {
public:
    int chave;
    No* esquerda;
    No* direita;
    int altura;

    No(int valor) {
        chave = valor;
        esquerda = direita = nullptr;
        altura = 1;
    }
};

class ArvoreAVL {
private:
    No* raiz;

    int altura(No* no) {
        if (no == nullptr)
            return 0;
        return no->altura;
    }

    int fatorBalanceamento(No* no) {
        if (no == nullptr)
            return 0;
        return altura(no->esquerda) - altura(no->direita);
    }

    No* rotacaoDireita(No* y) {
        No* x = y->esquerda;
        No* T2 = x->direita;

        x->direita = y;
        y->esquerda = T2;

        y->altura = std::max(altura(y->esquerda), altura(y->direita)) + 1;
        x->altura = std::max(altura(x->esquerda), altura(x->direita)) + 1;

        return x;
    }

    No* rotacaoEsquerda(No* x) {
        No* y = x->direita;
        No* T2 = y->esquerda;

        y->esquerda = x;
        x->direita = T2;

        x->altura = std::max(altura(x->esquerda), altura(x->direita)) + 1;
        y->altura = std::max(altura(y->esquerda), altura(y->direita)) + 1;

        return y;
    }

    No* inserir(No* no, int chave) {
        if (no == nullptr)
            return new No(chave);

        if (chave < no->chave)
            no->esquerda = inserir(no->esquerda, chave);
        else if (chave > no->chave)
            no->direita = inserir(no->direita, chave);
        else
            return no; // Ignorar chaves duplicadas

        no->altura = 1 + std::max(altura(no->esquerda), altura(no->direita));

        int balanceamento = fatorBalanceamento(no);

        // Casos de desbalanceamento
        // Esquerda-Esquerda
        if (balanceamento > 1 && chave < no->esquerda->chave)
            return rotacaoDireita(no);

        // Direita-Direita
        if (balanceamento < -1 && chave > no->direita->chave)
            return rotacaoEsquerda(no);

        // Esquerda-Direita
        if (balanceamento > 1 && chave > no->esquerda->chave) {
            no->esquerda = rotacaoEsquerda(no->esquerda);
            return rotacaoDireita(no);
        }

        // Direita-Esquerda
        if (balanceamento < -1 && chave < no->direita->chave) {
            no->direita = rotacaoDireita(no->direita);
            return rotacaoEsquerda(no);
        }

        return no;
    }

    void percorrerEmOrdem(No* no) {
        if (no != nullptr) {
            percorrerEmOrdem(no->esquerda);
            std::cout << no->chave << " ";
            percorrerEmOrdem(no->direita);
        }
    }

public:
    ArvoreAVL() : raiz(nullptr) {}

    void inserir(int chave) {
        raiz = inserir(raiz, chave);
    }

    void percorrerEmOrdem() {
        percorrerEmOrdem(raiz);
    }
};

int main() {
    ArvoreAVL arvore;

    arvore.inserir(10);
    arvore.inserir(20);
    arvore.inserir(30);
    arvore.inserir(40);
    arvore.inserir(50);
    arvore.inserir(25);

    std::cout << "Árvore AVL percorrendo em ordem: ";
    arvore.percorrerEmOrdem();
    std::cout << std::endl;

    return 0;
}
