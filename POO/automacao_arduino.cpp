#include <Arduino.h>

// Definindo a classe Lampada
class Lampada {
private:
  int pinAnodo;
  int pinCatodo;

public:
  Lampada(int anodo, int catodo) : pinAnodo(anodo), pinCatodo(catodo) {
    pinMode(pinAnodo, OUTPUT);
    pinMode(pinCatodo, OUTPUT);
    desligar();
  }

  void ligar() {
    digitalWrite(pinAnodo, HIGH);
    digitalWrite(pinCatodo, LOW);
  }

  void desligar() {
    digitalWrite(pinAnodo, LOW);
    digitalWrite(pinCatodo, HIGH);
  }
};

// Definindo a classe AutomacaoResidencial
class AutomacaoResidencial {
private:
  int pinPir;
  int pinRelay;
  Lampada lampada;

public:
  AutomacaoResidencial(int pirPin, int relayPin, int ledAnodo, int ledCatodo)
      : pinPir(pirPin), pinRelay(relayPin), lampada(ledAnodo, ledCatodo) {
    pinMode(pinPir, INPUT);
    pinMode(pinRelay, OUTPUT);
    desligarDispositivos();
  }

  void iniciar() {
    Serial.begin(9600);
  }

  void verificarMovimento() {
    int estadoMovimento = digitalRead(pinPir);

    if (estadoMovimento == HIGH) {
      Serial.println("Movimento detectado!");
      ligarDispositivos();
      delay(5000);  // Espera 5 segundos para evitar acionamentos constantes
    } else {
      desligarDispositivos();
    }
  }

private:
  void ligarDispositivos() {
    digitalWrite(pinRelay, HIGH);
    lampada.ligar();
  }

  void desligarDispositivos() {
    digitalWrite(pinRelay, LOW);
    lampada.desligar();
  }
};

// Criando uma instância da classe AutomacaoResidencial
AutomacaoResidencial automacao(2, 7, 8, 9);  // Substitua os pinos conforme necessário

void setup() {
  automacao.iniciar();
}

void loop() {
  automacao.verificarMovimento();
}
