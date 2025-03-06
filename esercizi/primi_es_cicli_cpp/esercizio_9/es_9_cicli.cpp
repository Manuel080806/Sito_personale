#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> numeri = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    
    cout << "Elementi dell'array: ";
    for(const auto& num : numeri) {
        cout << num << " ";
    }
    cout << endl << endl;
    system("pause");
}