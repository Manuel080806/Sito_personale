#include <iostream>
using namespace std;
int main() {
    int n, somma = 0;
    cout << "Inserisci un numero intero positivo: ";
    cin >> n;
    for(int i = 1; i <= n; i++) {
        somma += i;
    }
    cout << "La somma dei numeri da 1 a " << n << " e': " << somma << endl << endl;
    system("PAUSE");
}