#include<iostream>
using namespace std;

int main ()
{
    float base_maggiore;
    float altezza;
    float base_minore;
    float area;
    cout<<"inserisci base maggiore:"<<endl;
    cin>> base_maggiore;
    base_minore= base_maggiore/3;
    altezza = base_minore*2;
    base_maggiore = altezza+base_minore;
    area=(base_maggiore+base_minore)*altezza/2;
    cout<<"l'area e':"<<area;
}
