#include<iostream>
using namespace std;
int main ()
{
    float perimetro;
    float altezza;
    float area;
    float base;
    cout<<"inserire perimetro:";
    cin>>perimetro;
    cout<<"inserire altezza:";
    cin>>altezza;
    base= (perimetro/2.0)- altezza;
    area = base*altezza;
    cout<< "l'area e':"<<area;
}
