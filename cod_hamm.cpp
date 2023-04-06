#include "cod_hamm.h"
cod_hamm::cod_hamm()
{
  pin_interrupt=3;
  pin_fin=5;
  pin_datos=4;
  pinMode(pin_interrupt,OUTPUT);
  pinMode(pin_datos,OUTPUT);
  pinMode(pin_fin,OUTPUT);
}
/*funciones de la clase*/
void cod_hamm::carc_bin(char c)
{
    int x=c;
	for (int i=0;i<7;i++)
	{	
		b[7-i]=x%2;
		x=x/2;
	}
}
void cod_hamm::par()
{
	int aux=b[0]+b[1]+b[3]+b[4]+b[6];
	p[0]=aux%2;
	aux=b[0]+b[2]+b[3]+b[5]+b[6];
	p[1]=aux%2;
	aux=b[1]+b[2]+b[3]+b[7];
	p[2]=aux%2;
	aux=b[4]+b[5]+b[6]+b[7];
	p[3]=aux%2;
}
void cod_hamm::men()
{
	int sinc[]={0,0,0,0,0,0,0,1};
	cod[8]=p[0];
	cod[9]=p[1];
	cod[11]=p[2];
	cod[15]=p[3];
	for (int i=0;i<8;i++)//tiene un problema, modifica el vector de paridades.
	{
		cod[i]=sinc[i];
	}
	for (int i=10,j=1,k=0;i<20;i++)//llena el mensaje codificado y con el byte de paridad.
	{
		if (i!=11 && i!=15)
		{	
			cod[i]=b[k];
			k++;
		}
	}
}
void cod_hamm::transm()
{   
      int aux=0;
      int lector=0;
    for(int i=0;i<20;i++)
    {  
        
        digitalWrite(pin_interrupt,HIGH);
        digitalWrite(pin_fin,HIGH);
        if(cod[i]==0 && lector == 0)
        {
            aux++;
            //Serial.print("0");
        }
        else if(cod[i]==1 && aux==7)
        {
            aux=0;
            lector=1;
            digitalWrite(pin_fin,LOW);
            //Serial.print("1");
        }
        else
        { 
            if(cod[i]==0)
            {
                digitalWrite(pin_interrupt,LOW);
                digitalWrite(pin_datos,LOW);
                //Serial.print("0");
            }
            else
            {
                digitalWrite(pin_interrupt,LOW);
                digitalWrite(pin_datos,HIGH);
                //Serial.print("1");
            }
        }
        delay(50);
    }
    //Serial.println("");
}

/*finaliza el código*/

