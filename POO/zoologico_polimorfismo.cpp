#include <iostream>
using namespace std;

class Animal{
    private:
        string nome;
        int idade;
        bool banho;
        bool saude;

    public: 
        Animal(string Anome, int Aidade, bool Abanho, bool Asaude){
            nome = Anome;
            idade = Aidade;
            banho = Abanho;
            saude = Asaude;
        }

        virtual void MostrarEspecie()const{
            cout << "Especie do animal aqui " << endl;
        }

        void MostrarNome()const{
            cout << "Meu nome: " << nome << endl;
        }

        void MostrarIdade()const{
            cout << "Tenho: " << idade << " anos" << endl;
        }

        void MostrarBanho()const{
            cout << "Banho: " << banho << endl;
        }

        void MostrarSaude()const{
            cout << "Saudavel: " << saude << endl;
        }

        bool DarBanho(){
            banho = true;
            return banho;
        }

        bool DarRemedio(){
            saude = true;
            return saude;
        }
};

class Girafa : public Animal{
    public:
        Girafa(string Anome, int Aidade, bool Abanho, bool Asaude) : Animal(Anome, Aidade, Abanho, Asaude) {}

        void MostrarEspecie()const{
            cout << "Sou uma girafa " << endl;
        }
};

class Elefante : public Animal{
    public:
        Elefante(string Anome, int Aidade, bool Abanho, bool Asaude) : Animal(Anome, Aidade, Abanho, Asaude) {}

        void MostrarEspecie()const{
            cout << "Sou uma girafa " << endl;
        }
};

class Leao : public Animal{
    public:
        Leao(string Anome, int Aidade, bool Abanho, bool Asaude) : Animal(Anome, Aidade, Abanho, Asaude) {}

        void MostrarEspecie()const{
            cout << "Sou uma girafa " << endl;
        }
};

int main(){
    int cuidador = 0;
    Animal *VetorAnimais[5];
    
    VetorAnimais[0] = new Girafa("Mica", 8, false, true);
    VetorAnimais[1] = new Girafa("Caio", 2, true, true);
    VetorAnimais[2] = new Leao("Rafa", 9, false, true);
    VetorAnimais[3] = new Leao("Alex", 7, false, false);
    VetorAnimais[4] = new Elefante("Nelson", 15, false, false);

    cout << "Status dos animais: " << endl;

    for(int i=0; i<5; i++){
        VetorAnimais[i] -> MostrarEspecie();
        VetorAnimais[i] -> MostrarNome();
        VetorAnimais[i] -> MostrarIdade();
        VetorAnimais[i] -> MostrarBanho();
        VetorAnimais[i] -> MostrarSaude();
        cout << endl;
    }
    
    do{
        cout << "Deseja contratar um cuidador para o zoologico: "<< endl;
        cout << "[1] Sim [2]Nao" << endl;
        cin >> cuidador; 

        if(cuidador == 1){
            VetorAnimais[0] -> DarBanho();
            VetorAnimais[2] -> DarBanho();
            VetorAnimais[3] -> DarBanho();
            VetorAnimais[3] -> DarRemedio();
            VetorAnimais[4] -> DarBanho();
            VetorAnimais[4] -> DarRemedio();

            cout << "Status dos animais: " << endl;

            for(int i=0; i<5; i++){
                VetorAnimais[i] -> MostrarEspecie();
                VetorAnimais[i] -> MostrarNome();
                VetorAnimais[i] -> MostrarIdade();
                VetorAnimais[i] -> MostrarBanho();
                VetorAnimais[i] -> MostrarSaude();
                cout << endl;
            }

            cout << "Programa encerrado! " << endl;
        }

        else if(cuidador == 2){
            cout << "Programa encerrado! " << endl;
        }

        else{
            cout << "Opcao invalida" << endl;
            cout << endl;
        }
    } while (cuidador != 1 && cuidador != 2);

    return 0;
}