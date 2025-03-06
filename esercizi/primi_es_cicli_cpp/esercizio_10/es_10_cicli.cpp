#include <iostream>
#include <vector>
using namespace std;
int main() {   
    vector<int> numeri = {12, 45, 7, 23, 56, 89, 34, 67, 5, 19};
    int massimo = numeri[0];
    
    for(const auto& num : numeri) {
        if(num > massimo) {
            massimo = num;
        }
    }
    
    cout << "Il valore massimo nel vettore e': " << massimo << endl << endl;
    system("pause");
}