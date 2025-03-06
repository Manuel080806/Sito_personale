#include <iostream>
using namespace std;
int main() {
    int n;
    cout << "Inserisci un numero per vedere la sua tabellina: ";
    cin >> n;
    
    cout << "Tabellina del " << n << ":" << endl;
    for(int i = 1; i <= 10; i++) {
        cout << n << " x " << i << " = " << n * i << endl;
    }
    cout << endl;
    system("pause");
}