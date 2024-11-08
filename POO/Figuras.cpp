#include <iostream>
#include <cmath>
using namespace std;

const double PI = 3.14159265358979323846;

// Classe abstrata base para figuras:
class Figura {
public:
    // Métodos virtuais puros a serem implementados ans classes derivadas
    virtual double calculaArea() const = 0;
};

// Classe derivada Quadrado, implementa a interface Figura
class Quadrado : public Figura {
private:
    double lado;

public:
    Quadrado(double tamLado) : lado(tamLado) {}

    // Implementação do método para calcular a área
    double calculaArea() const override {
        double area = lado * lado;
        return area;   
    }
};

// Classe derivada Triangulo, implementa a interface Figura
class Triangulo : public Figura {
private:
    double base, altura;
    
public:
    Triangulo(double tamBase, double tamAltura) : base(tamBase), altura(tamAltura) {}

    // Implementação do método para calcular a área
    double calculaArea() const override {
        double area = 0.5 * base * altura;
        return area;
    }
};

// Classe derivada Circulo, implementa a interface Figura
class Circulo : public Figura {
private:
    double raio;

public:
    Circulo(double tamRaio) : raio(tamRaio) {}

    // Implementação do método para calcular a área
    double calculaArea() const override {
        double area = PI * raio * raio;
        return area;
    }
};

int main() {
    // Array de ponteiros para Figura
    Figura* ptr_figura[100];
    int escolha = true;
    int num_figuras = 0;

    // Loop para criar figuras
    while(escolha != 0){
        cout << "Seleciona uma opcao:" << endl;
        cout << "1 - Quadrado" << endl;
        cout << "2 - Triangulo" << endl;
        cout << "3 - Circulo" << endl;
        cout << "0 - Sair" << endl;
        cin >> escolha;
    
        switch(escolha){
            // Criar quadrado:
            case 1: {
                double tamLado;
                cout << "Informe o tamanho do lado do quadrado: " << endl;
                cin >> tamLado;
                ptr_figura[num_figuras++] = new Quadrado(tamLado);
                break;
            }

            // Criar triângulo:
            case 2: {
                double tamBase, tamAltura;
                cout << "Informe o tamanho da base do triangulo: " << endl;
                cin >> tamBase;
                cout << "Informe o tamanho da altura do triangulo: " << endl;
                cin >> tamAltura;
                ptr_figura[num_figuras++] = new Triangulo(tamBase, tamAltura);
                break;
            }

            // Criar círculo:
            case 3: {
                double tamRaio;
                cout << "Informe o tamanho do raio do circulo: " << endl;
                cin >> tamRaio;
                ptr_figura[num_figuras++] = new Circulo(tamRaio);
                break;
            }
        }
    }

    // Loop para calcular e imprimir áreas das figuras
    for(int i=0; i < num_figuras; i++){
        double area = ptr_figura[i] -> calculaArea();
        cout << "Area da figura " << i+1 << ": " << area << endl;
    }

    // Loop para liberar a memória 
    for(int i = 0; i < num_figuras; i++){
        delete ptr_figura[i];
    }

    return 0;
}