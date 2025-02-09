#include<iostream>
using namespace std;

int main()
{
    float spesa;
    float costolitro;
    cout<<"inserire costo di un litro di benzina:" << endl;
    cin>> costolitro;
    spesa = 100/20 * costolitro;
    cout << "il costo per fare 100km e' :" << spesa;
    return 0;
}
