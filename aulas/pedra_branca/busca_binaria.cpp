#include <iostream>
#include <vector>

int buscaBinaria(const std::vector<int>& arr, int elemento) {
    int esquerda = 0;
    int direita = arr.size() - 1;

    while (esquerda <= direita) {
        int meio = esquerda + (direita - esquerda) / 2;

        // Verifica se o elemento está presente no meio
        if (arr[meio] == elemento) {
            return meio;
        }

        // Se o elemento é maior, ignore a metade esquerda
        if (arr[meio] < elemento) {
            esquerda = meio + 1;
        } 
        // Se o elemento é menor, ignore a metade direita
        else {
            direita = meio - 1;
        }
    }

    // Se o elemento não está presente no array
    return -1;
}

int main() {
    std::vector<int> arr = {2, 3, 4, 10, 40};
    int elemento = 10;
    int resultado = buscaBinaria(arr, elemento);

    if (resultado != -1) {
        std::cout << "Elemento encontrado no índice: " << resultado << std::endl;
    } else {
        std::cout << "Elemento não encontrado no array." << std::endl;
    }

    return 0;
}
