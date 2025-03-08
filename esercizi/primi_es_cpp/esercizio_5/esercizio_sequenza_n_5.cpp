#include<iostream>
using namespace std;
int main ()
{
    float prezzo_con_iva;
    float iva;
    float prezzo_netto;
    iva=0.22;
    cout<<"inserire il prezzo comprensivo dell'iva:";
    cin>>prezzo_con_iva;
    prezzo_netto=prezzo_con_iva/1.22;
    cout<<"il prezzo netto e':"<<prezzo_netto;
    system ("pause");
}
