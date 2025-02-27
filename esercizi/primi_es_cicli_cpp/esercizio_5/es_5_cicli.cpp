#include <iostream>
using namespace std;
int main() {
    int n;
    long long fattoriale = 1;
    cout << "Inserisci un numero intero positivo: ";
    cin >> n;   
    for(int i = 1; i <= n; i++) {
        fattoriale *= i;
    }
    cout << "Il fattoriale di " << n << " e': " << fattoriale << endl << endl;
    system("PAUSE");
}