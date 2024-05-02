// Função para verificar se é triângulo
function isTriangulo(a, b, c) {
    if (a < (b + c) && b < (a + c) && c < (b + a)) {
        return true;
    }
    return false;
}

// Obtendo os 4 comprimentos que são solicitados na questão
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Digite os 4 comprimentos separados por espaço: ", function (input) {
    const [n1, n2, n3, n4] = input.split(' ').map(Number);

    // Testando para todos os comprimentos
    if (isTriangulo(n1, n2, n3) || isTriangulo(n1, n2, n4) || isTriangulo(n1, n3, n4) || isTriangulo(n2, n3, n4)) {
        console.log('S');
    } else {
        console.log('N');
    }

    rl.close();
});
