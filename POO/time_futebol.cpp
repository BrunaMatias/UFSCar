#include <iostream>
#include <string>

using namespace std;

// Classe base
class funcionario{
    protected:
        double salario;
        string nome;
        string cargo;
    public:
        funcionario(string n, double s, string p){
            nome = n;
            salario = s;
            cargo = p;
        }
        virtual double depositar_bonus(double valor){
            salario += valor;
        }
        virtual void imprimir()const{
            cout<< "Nome: " << nome << " Salario: " << salario << " cargo: " << cargo << endl;
        }
};

// Classe secundária jogador
class jogador : public funcionario{
    private:
        int qtd_gols;
        float valor_bonus;
    public:
        jogador(string tnome, double tsalario, int tqtd_gols, float tvalor_bonus, string tcargo): funcionario(tnome, tsalario, tcargo){
            qtd_gols = tqtd_gols;
            valor_bonus = tvalor_bonus;
        }
        double depositar_bonus(){
            salario = salario + (qtd_gols * valor_bonus);
            return salario;
        }
};

// Classe secundária tecnico
class tecnico : public funcionario{
    private:
        int qtd_titulos;
        float valor_bonus;
    public:
        tecnico(string tnome, double tsalario, int tqtd_titulos, float tvalor_bonus, string tcargo) : funcionario (tnome, tsalario, tcargo){
            qtd_titulos = tqtd_titulos;
            valor_bonus = tvalor_bonus;
        }
        double depositar_bonus(){
            salario = salario + (qtd_titulos * valor_bonus);
            return salario;
        }
};

int main(){
    int qtd_jogadores;
    int qtd_tecnicos;
    int qtd_funcionarios;

    cout<< "Informe a quantidade de jogadores a serem cadastrados: ";
    cin >> qtd_jogadores;

    if(qtd_jogadores > 0){
        float bonus_jogador;
        cout<< "Informe o valor em dinheiro do bonus: "<< endl;
        cin >> bonus_jogador;

        while(qtd_jogadores > 0){
            string jnome;
            double jsalario;
            int jgols;
            string jcargo;

            cout<< "Informe o nome: " << endl;
            cin >> jnome;
            cout<< "Informe o salario: " << endl;
            cin >> jsalario;
            cout<< "Informe a quantidade de gols marcados: " << endl;
            cin >> jgols;
            cout<< "Informe a cargo: " << endl;
            cin >> jcargo;

            // Cria objeto de jogador
            jogador jog(jnome, jsalario, jgols, bonus_jogador, jcargo);

            jog.depositar_bonus();
            jog.imprimir();

            qtd_jogadores -= 1;
        }
    }

    cout<< "Informe a quantidade de tecnicos a serem cadastrados: ";
    cin >> qtd_tecnicos;

    if(qtd_tecnicos > 0){
        float bonus_tecnico;
        cout<< "Informe o valor em dinheiro do bonus: "<< endl;
        cin >> bonus_tecnico;

        while(qtd_tecnicos > 0){
            string tnome;
            double tsalario;
            int ttitulos;
            string tcargo;

            cout<< "Informe o nome: " << endl;
            cin >> tnome;
            cout<< "Informe o salario: " << endl;
            cin >> tsalario;
            cout<< "Informe a quantidade de titulos ganhos: " << endl;
            cin >> ttitulos;
            tcargo = "tecnico ";

            // Cria objeto de tecnico
            tecnico tec(tnome, tsalario, ttitulos, bonus_tecnico, tcargo);

            tec.depositar_bonus();
            tec.imprimir();

            qtd_tecnicos -= 1;
        }
    }

    cout<< "Informe a quantidade de outros funcionarios para cadastro: ";
    cin >> qtd_funcionarios;

    if(qtd_funcionarios > 0){
        while(qtd_funcionarios > 0){
            string fnome;
            double fsalario;
            string fcargo;

            cout<< "Informe o nome: " << endl;
            cin >> fnome;
            cout<< "Informe o salario: " << endl;
            cin >> fsalario;
            cout<< "Informe o cargo: " << endl;
            cin >> fcargo;

            // Cria objeto de funcionario
            funcionario fun(fnome, fsalario, fcargo);

            fun.imprimir();

            qtd_funcionarios -= 1;
        }
    }
}