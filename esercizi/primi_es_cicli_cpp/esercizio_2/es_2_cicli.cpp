#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"inserire un numero"<<endl;
    cin>>n;
    if(n%2!=0)
        n =n - 1;
    do
    {
        cout << n << endl;
        n = n-2;
    }
    while (n!=0);
    return 0;
}
