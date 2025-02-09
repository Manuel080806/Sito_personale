#include <iostream>
using namespace std;
int main()
{

  //input dei dati
  int consumo_mensile;
  float importo;
  cout<< "inserire consumo mensile "<<endl;
  cin>> consumo_mensile;
  importo= 0;
  //logica del programma
  if (consumo_mensile<= 500)
    cout<<" l'importo e' 20 euro"<<endl;
  else
    if(consumo_mensile<=1000)
      {
      importo = 20 + 0.08*(consumo_mensile-500);
      cout<< "l'importo e':"<<importo<<endl;
      }
    else
      {
      importo= 0;
      importo= 60 + 0.05*(consumo_mensile-1000);
      cout<< "l'importo e':"<<importo<<endl;
      }
}
