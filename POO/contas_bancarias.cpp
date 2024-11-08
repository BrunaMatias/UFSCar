#include <iostream>
#include <vector>
using namespace std;

// Classe base que representa uma conta genérica
class Conta {
protected:
    string TipoConta;
    string nome;
    int DataAbertura;
    double TaxaManutencao;
    double saldo;

public:
    // Construtor da classe base
    Conta(string vTipoConta, string vNome, int vDataAbertura) {
        TipoConta = vTipoConta;
        nome = vNome;
        DataAbertura = vDataAbertura;
        saldo = 0;
        TaxaManutencao = 0; // Inicializar TaxaManutencao para evitar problemas
    }

    // Função para consultar o saldo da conta
    void consultarSaldo() {
        cout << "Saldo atual: R$" << saldo - TaxaManutencao << endl;
    }

    // Função virtual para sacar dinheiro da conta
    virtual double Sacar(double valor) {
        if (valor <= saldo) {
            cout << "Saque de R$" << valor << " realizado com sucesso" << endl;
            return saldo -= valor;
        }
        else {
            cout << "Saldo insuficiente" << endl;
            return 0;
        }
    }

    // Função virtual para depositar dinheiro na conta
    virtual void depositar(double valor) {
        saldo += valor - TaxaManutencao;
    }
};

// Classe derivada que representa uma conta poupança
class Poupanca : public Conta {
private:
    double TaxaManutencao = 15; // Taxa específica para a poupança

public:
    // Construtor da classe poupança que chama o construtor da classe base
    Poupanca(string pNome, int pDataAbertura) : Conta("Poupanca", pNome, pDataAbertura) {};

    // Implementação da função depositar específica para a poupança
    void depositar(double valor) override {
        saldo += valor - TaxaManutencao;
        cout << "Deposito de R$" << valor << " realizado com sucesso" << endl;
    }
};

// Classe derivada que representa uma conta de investimento
class ContaInvestimento : public Conta {
private:
    double TaxaManutencao = 30; // Taxa específica para conta de investimento

public:
    // Construtor da classe de investimento que chama o construtor da classe base
    ContaInvestimento(string iNome, int iDataAbertura) : Conta("Investimento", iNome, iDataAbertura) {};

    // Implementação da função depositar específica para conta de investimento
    void depositar(double valor) override {
        saldo += valor - TaxaManutencao;
        cout << "Deposito de R$" << valor << " realizado com sucesso" << endl;
    }
};

// Função principal do programa
int main() {
    int numContas;

    // Solicita ao usuário o número de contas a serem criadas
    cout << "Quantas contas deseja criar? ";
    cin >> numContas;

    vector<Conta*> contas;

    // Loop para criar as contas com base na escolha do usuário
    for (int i = 0; i < numContas; ++i) {
        int opcao;
        string nome;

        // Solicita ao usuário o tipo de conta a ser criada
        cout << "Informe o tipo de conta a ser criada para a conta " << i + 1 << ":" << endl;
        cout << "[1] Comum [2] Poupanca ou [3] Investimento" << endl;
        cin >> opcao;

        Conta* conta;

        // Cria a conta com base na escolha do usuário
        if (opcao == 1) {
            cout << "Informe o nome: ";
            cin >> nome;
            conta = new Conta("Comum", nome, 0); 
        }
        else if (opcao == 2) {
            cout << "Informe o nome: ";
            cin >> nome;
            conta = new Poupanca(nome, 0); 
        }
        else if (opcao == 3) {
            cout << "Informe o nome: ";
            cin >> nome;
            conta = new ContaInvestimento(nome, 0); 
        }
        else {
            cout << "Opção inválida!" << endl;
            return 1;
        }

        contas.push_back(conta);
    }

    int escolhaConta;

    // Loop principal do programa
    do {
        // Solicita ao usuário escolher uma conta ou sair
        cout << "\nEscolha uma conta (1 a " << numContas << ") ou 0 para sair: ";
        cin >> escolhaConta;

        // Verifica se a escolha está dentro dos limites
        if (escolhaConta >= 1 && escolhaConta <= numContas) {
            int opcaoOperacao;

            // Loop para realizar operações na conta escolhida
            do {
                cout << "\nOperações disponíveis:\n"
                        "[1] Depositar\n"
                        "[2] Sacar\n"
                        "[3] Consultar Saldo\n"
                        "[0] Voltar para o menu anterior\n"
                        "Escolha uma operação: ";
                cin >> opcaoOperacao;

                // Executa a operação com base na escolha do usuário
                switch (opcaoOperacao) {
                    case 1: {
                        double valor;
                        cout << "Informe o valor para depositar: R$";
                        cin >> valor;
                        contas[escolhaConta - 1]->depositar(valor);
                        break;
                    }
                    case 2: {
                        double valor;
                        cout << "Informe o valor para sacar: R$";
                        cin >> valor;
                        contas[escolhaConta - 1]->Sacar(valor);
                        break;
                    }
                    case 3:
                        contas[escolhaConta - 1]->consultarSaldo();
                        break;
                    case 0:
                        break;
                    default:
                        cout << "Opção inválida!" << endl;
                        break;
                }

            } while (opcaoOperacao != 0);
        }

    } while (escolhaConta != 0);

    // Libera a memória alocada para as contas
    for (int i = 0; i < numContas; ++i) {
        delete contas[i];
    }

    return 0;
}