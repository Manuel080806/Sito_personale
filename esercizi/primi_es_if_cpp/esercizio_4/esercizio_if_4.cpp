#include<iostream>
#include<cmath>
using namespace std;

int main ()
{
    float a;
    float b;
    float c;
    float d;
    float a_b;
    float c_d;
    cout<<"inserisci quattro numeri:"<<endl;
    cin>>a;
    cin>>b;
    cin>>c;
    cin>>d;
    a_b= a + b;
    c_d= c + d;
    if(a_b<= c_d)
        cout<<" e' minore o uguale";
}

