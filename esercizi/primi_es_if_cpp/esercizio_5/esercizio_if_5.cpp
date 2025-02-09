#include <iostream>
using namespace std;
int main()
{
  //lettura dati di imput
  int uno,due,tre;
  int maggiore;
  cout << "inserisci tre numeri"<<endl;
  cin>>uno;
  cin>>due;
  cin>>tre;
  //logica del programma
 if(uno>due)
   if(uno>tre)
     maggiore=uno;
   else
     maggiore=tre;
 else
   if(due>tre)
     maggiore=due;
   else
     maggiore=tre;

  //scrittura dei dati di otput
   cout<<"il numero maggiore e':"<<maggiore;

}
