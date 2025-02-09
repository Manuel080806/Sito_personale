#include<iostream>
#include<cmath>
using namespace std;

int main ()
{
    float numero_a;
    float numero_b;
    float numero_maggiore;
    cout<<"inserisci due numeri:";
    cin>>numero_a;
    cin>>numero_b;
    if(numero_a>numero_b)
        numero_maggiore=numero_a;
    else numero_maggiore=numero_b;
    cout<<"il numero maggiore e'" <<numero_maggiore;
}
