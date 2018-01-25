# Teste Pratico

Primeiramente gostaria de pedir desculpas porque tenho maior proeficiencia em **JavaScript** e **Node.js**.

## Índice Remissivo


> ATENÇÃO: O algoritmo não é eficiente para grandes casos, precisa-se melhorar o tempo de busca( `O(n^2)` mas poderia ser `O(log(n)^2)` ) e o tempo de impressao ( `O(n)` mas poreria ser `O(1)`), poreém fiz isso correndo e cansado durante a madrugada.
### Como o algoritmo funciona?

1. O algoritmo percorre todas as linhas do arquivo montando uma lista de palavras

2. Na segunda etapa, percorremos essa lista gerada para poder criar uma nova lista

    2.1 Se a palavra nāo estiver nova lista incluimos ela com a linha em qual aparece

    2.2 Se a palavra já existe na lista, apenas colocamos a linha na lista de aparições

3. Por fim ordenamos a lista gerada no passo `2` baseando-se na palavra

4. Formatamos e imprimimos a saída

### Como executar?

**Pre-requisito:** `python` e `make` instalado no sistema.

Para executar o projeto:

1. Clone o projeto: `git clone https://github.com/marco-souza/remissive_index.git`

2. Entre na pasta do projeto: `cd remissive_index`

3. Execute `make`



Cheers :)