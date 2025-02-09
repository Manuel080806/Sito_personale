#include <iostream>
using namespace std;
main()
{

	int n1,n2;
	cout<<"Iniziamo a stampare"<<endl;
	cout<<"Inserisci il primo numero"<<endl;
	cin>>n1;
	cout<<"Inserisci il secondo numero"<<endl;
	cin>>n2;
	int i=n1;
	cout<<"I numeri all' interno dell' intervallo sono:"<<endl;
	while (i<=n2)
	{
		cout<<i<<endl;
		i=i+1;
	}
	system("PAUSE");
}
