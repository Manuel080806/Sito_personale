#include<iostream>
using namespace std;
int main ()
{
    //lettura dati di imput
    float cateto_a;
    float cateto_b;
    float ipotenusa;
    cout<<"inserire il primo cateto di un triangolo:";
    cin>>cateto_a;
    cout<<"inserire il secondo cateto di un triangolo:";
    cin>>cateto_b;
    cout<<"inserire l'ipotenusa di un triangolo:";
    cin>>ipotenusa;
    //logica del programma
    if(cateto_a==cateto_b)
        if(cateto_b==ipotenusa)
           cout<<"equilatero";
        else
           cout<<"isoscele";
    else
        if(cateto_a==ipotenusa)
           cout<<"isoscele";
        else
           cout<<"scaleno";

}
