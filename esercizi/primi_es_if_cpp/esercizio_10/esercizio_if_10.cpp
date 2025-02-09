#include<iostream>
using namespace std;
int main ()
{
    int va,vb,vc;
    cout<<"inserire tre voti"<<endl;
    cin>>va;
    cin>>vb;
    cin>>vc;
    if (va>=6 && vb>=6 && vc>=6)
        cout<<"sufficienti";
    return 0;
}
