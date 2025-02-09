#include<iostream>
using namespace std;

int main ()
{
    float prezzo_base;
    float sconto;
    float iva;
    float prezzo_lordo;
    float prezzo_scontato;
    cout<<"inserisci in sequanza i dati sul prezzo lo sconto e l'iva:",
    cin>>prezzo_base;
    cin>>sconto;
    cin>>iva;
    prezzo_scontato = prezzo_base-prezzo_base*sconto/100;
    prezzo_lordo = prezzo_scontato*(1+iva/100);
    cout << "il prezzo totale e':" <<prezzo_lordo;
}
