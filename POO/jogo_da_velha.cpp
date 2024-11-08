#include <iostream>
#include <vector>

using namespace std;

class Tabuleiro {
private:
    vector<vector<char>> matriz;

public:
    Tabuleiro() : matriz(3, vector<char>(3, ' ')) {}

    void imprimir() const {
        for (const auto& linha : matriz) {
            for (char celula : linha) {
                cout << celula << " ";
            }
            cout << endl;
        }
        cout << endl;
    }

    bool fazerJogada(int linha, int coluna, char jogador) {
        if (linha < 0 || linha >= 3 || coluna < 0 || coluna >= 3 || matriz[linha][coluna] != ' ') {
            return false; // Jogada inválida
        }

        matriz[linha][coluna] = jogador;
        return true;
    }

    char verificarVencedor() const {
        for (int i = 0; i < 3; i++) {
            if (matriz[i][0] == matriz[i][1] && matriz[i][1] == matriz[i][2] && matriz[i][0] != ' ') {
                return matriz[i][0]; // Linha vencedora
            }
            if (matriz[0][i] == matriz[1][i] && matriz[1][i] == matriz[2][i] && matriz[0][i] != ' ') {
                return matriz[0][i]; // Coluna vencedora
            }
        }

        if (matriz[0][0] == matriz[1][1] && matriz[1][1] == matriz[2][2] && matriz[0][0] != ' ') {
            return matriz[0][0]; // Diagonal principal
        }
        if (matriz[0][2] == matriz[1][1] && matriz[1][1] == matriz[2][0] && matriz[0][2] != ' ') {
            return matriz[0][2]; // Diagonal secundária
        }

        return ' '; // Nenhum vencedor ainda
    }

    bool tabuleiroCheio() const {
        for (const auto& linha : matriz) {
            for (char celula : linha) {
                if (celula == ' ') {
                    return false; // Ainda há espaço vazio
                }
            }
        }
        return true; // Tabuleiro está cheio
    }
};

class JogoDaVelha {
private:
    Tabuleiro tabuleiro;
    char jogadorAtual;

public:
    JogoDaVelha() : jogadorAtual('X') {}

    void jogar() {
        while (true) {
            tabuleiro.imprimir();

            int linha, coluna;
            cout << "Jogador " << jogadorAtual << ", digite a linha (0-2) e a coluna (0-2) separadas por espaço: ";
            cin >> linha >> coluna;

            if (tabuleiro.fazerJogada(linha, coluna, jogadorAtual)) {
                char vencedor = tabuleiro.verificarVencedor();
                if (vencedor != ' ') {
                    tabuleiro.imprimir();
                    cout << "Jogador " << vencedor << " venceu!" << endl;
                    break;
                }

                if (tabuleiro.tabuleiroCheio()) {
                    tabuleiro.imprimir();
                    cout << "Empate!" << endl;
                    break;
                }

                jogadorAtual = (jogadorAtual == 'X') ? 'O' : 'X';
            } else {
                cout << "Essa célula já está ocupada ou a jogada é inválida. Tente novamente." << endl;
            }
        }
    }
};

int main() {
    JogoDaVelha jogo;
    jogo.jogar();

    return 0;
}
