#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main() {
    int N;
    cout << "Digite o número de pregos: ";
    cin >> N;

    cin.ignore(); // Limpar o buffer do newline após a entrada do número

    vector<int> pregos_num;
    cout << "Digite a ordem dos pregos na linha horizontal separados por espaço: ";
    string input;
    getline(cin, input);
    istringstream iss(input);
    int num_p;
    while (iss >> num_p) {
        pregos_num.push_back(num_p);
    }

    int cruzamentos = 0;

    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (pregos_num[j] < pregos_num[i]) {
                cruzamentos++;
            }
        }
    }

    cout << "O número de cruzamentos é: " << cruzamentos << endl;

    return 0;
}
