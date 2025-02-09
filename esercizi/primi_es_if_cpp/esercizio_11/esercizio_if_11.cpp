#include<iostream>
using namespace std;
int main ()
{
    int num;
    cout<<"inserire un numero"<<endl;
    cin>>num;
    if (num%3==0 && num%5==0)
        cout<<"divisibile";
    return 0;
}
