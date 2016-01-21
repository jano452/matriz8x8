//Biblioteca que controla o chip MAX7288
#include "LedControl.h"

/*
 pino 12 se conecta a DataIn 
 pino 11 se conecta a CLK 
 pino 10 se conecta a CS 
 Estamos usando uma única matriz.
 */
LedControl lc=LedControl(12,11,10,1);

/* Delay entre os leds = 9,375 segundos 
 *   ou 9375 milissegundos
 *   para inteirar 10 minutos 
 *   (são 64 leds) 
 *  600/64 * 1000 = 9375 */ 
unsigned long delaytime=9375;

void setup() {
  /* O chip inicia em modo de 
   * economia de energia e deve
   * ser inicializado */
  lc.shutdown(0,false);
  /* Brilho médio */
  lc.setIntensity(0,8);
  /* Limpa o display */
  lc.clearDisplay(0);
}

void conta_tempo() {
  //acende todos os leds inicialmente
  for(int row=0;row<8;row++) {
    for(int col=0;col<8;col++) {
      lc.setLed(0,row,col,true);
    }
  }

  //vai apagando os leds aos poucos
  for(int row=0;row<8;row++) {
    for(int col=0;col<8;col++) {
      delay(delaytime);
      lc.setLed(0,row,col,false);
      delay(delaytime);
    }
  }
}

void detona() {
  //desenha quadrados cada vez maiores
  for(int t=0; t<4; t++) {
      //apaga todos os leds inicialmente
      lc.clearDisplay(0);
      quadrado(t);
      delay(300);
  }
}

void quadrado(int lado) {
  int TAMANHO = 8;
  float MEIO = 3.5;
  for(int row=0;row<8;row++) {
    for(int col=0;col<8;col++) {
      if (lado == int(abs(MEIO - row)) and lado >= int(abs(MEIO - col))
      or lado == int(abs(MEIO - col)) and lado >= int(abs(MEIO - row))){
        lc.setLed(0,row,col,true);
      }
    }
  }
}

void loop() { 
  conta_tempo();
  while(true) {
    detona();
  }
}
