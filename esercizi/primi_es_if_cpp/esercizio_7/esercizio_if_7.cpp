#include <iostream>
using namespace std;
int main()
{
  //lettura dati di imput
  int uno,due,tre;
  int minore;
  cout << "inserisci tre numeri";
  cin>>uno;
  cin>>due;
  cin>>tre;
  //logica del programma
 if(uno<due)
   if(uno<tre)
     minore=uno;
   else
     minore=tre;
 else
   if(due<tre)
     minore=due;
   else
     minore=tre;

  //scrittura dei dati di otput
   cout<<"il numero minore e':"<<minore;

}
