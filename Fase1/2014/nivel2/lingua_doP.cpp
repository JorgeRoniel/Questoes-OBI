#include <iostream>
#include <string>

using namespace std;

int main() {
    string frase1;
    cout << "Digite uma frase: ";
    getline(cin, frase1);

    size_t pos;
    while ((pos = frase1.find('p')) != string::npos) {
        frase1.erase(pos, 1);
    }

    cout << frase1 << endl;

    return 0;
}
