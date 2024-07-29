#include <iostream>
#include <vector>
#include <algorithm>

// Função de busca binária para encontrar o índice da faixa correta
int buscaBinaria(const std::vector<int>& limites, int forca) {
    int inicio = 0;
    int fim = limites.size() - 1;

    while (inicio <= fim) {
        int meio = (inicio + fim) / 2;
        if (forca < limites[meio]) {
            fim = meio - 1;
        } else {
            inicio = meio + 1;
        }
    }
    
    return fim;  // Retorna o índice da faixa correta
}

int main() {
    // Leitura da entrada
    int N, M;
    std::cin >> N >> M;

    // Vetor para armazenar os limites das faixas (com tamanho M+1)
    std::vector<int> limitesFaixas(M + 1);
    limitesFaixas[0] = 0;  // O primeiro limite é sempre 0
    for (int i = 1; i <= M; ++i) {
        std::cin >> limitesFaixas[i];
    }

    // Vetor para armazenar os prêmios
    std::vector<int> premios(M);
    for (int i = 0; i < M; ++i) {
        std::cin >> premios[i];
    }

    // Vetor para armazenar as forças dos ogros
    std::vector<int> forcasOgros(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> forcasOgros[i];
    }

    // Processamento das premiações (com busca binária)
    std::vector<int> premiosOgros(N);
    for (int i = 0; i < N; ++i) {
        int indiceFaixa = buscaBinaria(limitesFaixas, forcasOgros[i]);
        premiosOgros[i] = premios[indiceFaixa];
    }

    // Impressão dos resultados
    for (int i = 0; i < N; ++i) {
        std::cout << premiosOgros[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
