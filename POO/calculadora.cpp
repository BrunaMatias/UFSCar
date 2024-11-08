#include <iostream>
#include <iomanip>
#include <bitset>

// Classe para representar a calculadora
class Calculadora {
private:
    float num1, num2, resultado;

public:
    // Método para definir os números a serem usados nas operações
    void setNumeros(float n1, float n2) {
        num1 = n1;
        num2 = n2;
    }

    // Métodos para realizar operações aritméticas
    float adicao() const {
        return num1 + num2;
    }

    float subtracao() const {
        return num1 - num2;
    }

    float multiplicacao() const {
        return num1 * num2;
    }

    float divisao() const {
        if (num2 != 0) {
            return num1 / num2;
        } else {
            std::cout << "Erro: divisao por zero!\n";
            return 0;
        }
    }

    // Métodos para converter números para binário e hexadecimal
    void converterParaBinario(int numero) const {
        std::cout << "Binario: " << std::bitset<32>(numero) << std::endl;
    }

    void converterParaHexadecimal(int numero) const {
        std::cout << "Hexadecimal: " << std::hex << std::uppercase << numero << std::dec << std::nouppercase << std::endl;
    }
};

int main() {
    // Criando uma instância da classe Calculadora
    Calculadora calculadora;

    float num1, num2;
    int escolha;

    do {
        // Exibindo as opções de operações
        std::cout << "\nEscolha uma operacao:\n";
        std::cout << "1. Adicao\n";
        std::cout << "2. Subtracao\n";
        std::cout << "3. Multiplicacao\n";
        std::cout << "4. Divisao\n";
        std::cout << "5. Converter para Binario\n";
        std::cout << "6. Converter para Hexadecimal\n";
        std::cout << "0. Sair\n";
        std::cout << "Opcao: ";
        std::cin >> escolha;

        // Executando a operação escolhida pelo usuário
        switch (escolha) {
            case 1:
            case 2:
            case 3:
            case 4:
                // Operações que exigem dois números
                std::cout << "Digite os dois numeros (separados por espaco): ";
                std::cin >> num1 >> num2;
                calculadora.setNumeros(num1, num2);

                switch (escolha) {
                    case 1:
                        std::cout << "Resultado: " << calculadora.adicao() << std::endl;
                        break;
                    case 2:
                        std::cout << "Resultado: " << calculadora.subtracao() << std::endl;
                        break;
                    case 3:
                        std::cout << "Resultado: " << calculadora.multiplicacao() << std::endl;
                        break;
                    case 4:
                        std::cout << "Resultado: " << calculadora.divisao() << std::endl;
                        break;
                }
                break;

            case 5:
                // Conversão para binário
                std::cout << "Digite o numero para converter para binario: ";
                std::cin >> num1;
                calculadora.converterParaBinario(static_cast<int>(num1));
                break;

            case 6:
                // Conversão para hexadecimal
                std::cout << "Digite o numero para converter para hexadecimal: ";
                std::cin >> num1;
                calculadora.converterParaHexadecimal(static_cast<int>(num1));
                break;

            case 0:
                std::cout << "Saindo da calculadora. Adeus!\n";
                break;

            default:
                std::cout << "Opcao invalida. Tente novamente.\n";
        }
    } while (escolha != 0);

    return 0;
}
