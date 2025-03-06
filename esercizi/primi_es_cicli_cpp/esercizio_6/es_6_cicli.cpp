#include <iostream>
using namespace std;
int main() {
    int n;
    cout << "Inserisci un numero intero positivo: ";
    cin >> n;
    cout << "I divisori di " << n << " sono: ";
    for(int i = 1; i <= n; i++) {
        if(n % i == 0) {
            cout << i << " ";
        }
    }
    cout << endl << endl;
    system("pause");
}