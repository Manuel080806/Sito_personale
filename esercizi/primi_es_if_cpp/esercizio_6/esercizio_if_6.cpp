#include<iostream>
#include<cmath>
using namespace std;

int main ()
{
    int voto_a;
    int voto_b;
    int voto_c;
    int voto_d;
    int insufficienze;
    cout<<"inserisci 4 voti"<<endl;
    cin>>voto_a;
    cin>>voto_b;
    cin>>voto_c;
    cin>>voto_d;
    if(voto_a>=6)
        insufficienze=1;
    if(voto_b>=6)
        insufficienze=insufficienze+1;
    if(voto_c>=6)
        insufficienze=insufficienze+1;
    if(voto_d>=6)
        insufficienze=insufficienze+1;
    cout<<"numero insufficienze ="<<insufficienze;
}
