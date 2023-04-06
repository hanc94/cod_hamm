#include "cod_hamm.h"
cod_hamm hamming;
String men_ser = "";
int i;
char mensaje[100];
void setup()
{
  pinMode(3, OUTPUT);
  Serial.begin(9600);
  digitalWrite(3, HIGH);
}

void loop()
{
  if (Serial.available())
  {
    men_ser = Serial.readString();
    men_ser.toCharArray(mensaje, sizeof(mensaje));
    for (i = 0; i < strlen(mensaje); i++)
    {
      hamming.carc_bin(mensaje[i]);
      hamming.par();
      hamming.men();
      hamming.transm();
    }
  }
}
