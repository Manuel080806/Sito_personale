#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> numeri = {15, 23, 36, 42, 58, 77, 91, 14, 35, 29};
    int somma = 0;
    
    for(const auto& num : numeri) {
        somma += num;
    }
    
    double media = static_cast<double>(somma) / numeri.size();
    
    cout << "La media dei valori nel vettore e': " << media << endl << endl;
    system("pause");
}