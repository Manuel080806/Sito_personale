#include<iostream>
using namespace std;
int main ()
{
    int base;
    int area;
    int altezza;
    int perimetro;
    cout<<"scrivere l'area del rettangolo"<<endl;
    cin>>area;
    cout<<"scrivere la base del rettangolo"<<endl;
    cin>>base;
    altezza= area/base,
    perimetro= 2*(altezza+base);
    cout<<"il perimetro e' "<<perimetro;
     system("pause");

}
