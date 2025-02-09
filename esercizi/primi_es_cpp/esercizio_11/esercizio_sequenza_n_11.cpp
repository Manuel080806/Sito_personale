#include<iostream>
#include<cmath>
using namespace std;

int main ()
{
    float numero_enciclopedie;
    float guadagno_mensile;
    float stipendio_lordo;
    float trattenute;
    cout<<"numero enciclopedie vendute:"<<endl;
    cin>>numero_enciclopedie;
    stipendio_lordo=1000+(numero_enciclopedie*200);
    trattenute= stipendio_lordo*0.18;
    guadagno_mensile= stipendio_lordo-trattenute;
    cout<<"quadagna:"<<guadagno_mensile;
}
