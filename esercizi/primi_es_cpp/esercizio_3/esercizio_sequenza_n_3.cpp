#include<iostream>
using namespace std;
int main ()
{
    float cateto_minore;
    float cateto_maggiore;
    float area;
    cout<<"inserire cateto minore";
    cin>>cateto_minore;
    cateto_maggiore = (cateto_minore/3.0)*5.0;
    area= (cateto_minore*cateto_maggiore)/2.0;
    cout<<"l'area e':"<<area;
}
