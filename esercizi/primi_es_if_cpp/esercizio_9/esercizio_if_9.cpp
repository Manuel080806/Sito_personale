#include<iostream>
using namespace std;
int main ()
{
    //iserire dati di input
    int uno;
    int due;
    cout<<"inserire due numeri:" <<endl;
    cin>>uno;
    cin>>due;
    //logica del programma
    if (( uno%2== 0)&&(due%2==0))
        cout<<"vittoria";
    else
        if(( uno%2==1)&&(due%2==1))
            cout<< "vittora";
        else
            cout<<"sconfitta";
    /* uno=uno%2;
    due=due%2;
    if(uno==due)
        cout<<"vittoria";
    else
        cout<<"sconfitta";*/
}
