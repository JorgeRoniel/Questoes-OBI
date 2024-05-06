const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
}); //interface de leitura

rl.question('', (codigo) => {
  let mensagem = '';

  let i = 0;
  while (i < codigo.length) {
    if (codigo[i] === ' ') {
      mensagem = mensagem + ' ';
    } else {
      i = i + 1;
      mensagem = mensagem + codigo[i];
    }
    i = i + 1;
  }

  console.log(mensagem);

  rl.close();
});
