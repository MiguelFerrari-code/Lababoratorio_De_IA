# Resultados da Atividade

## 2. Tabela de Treinamentos

| Treinamento | Erro Quadrático Médio | Número de Épocas |
|---|---|---|
| T1 | 0.003968 | 10133 |
| T2 | 0.004211 | 12219 |
| T3 | 0.004100 | 12793 |
| T4 | 0.004340 | 11658 |
| T5 | 0.004499 | 13291 |

## 3. Gráficos
Os gráficos foram gerados no arquivo `grafico_eqm.png`.

## 4. Explicação da variação de EQM e épocas
A rede Perceptron Multicamadas (MLP) é treinada utilizando o algoritmo de retropropagação do erro (backpropagation). Esse algoritmo utiliza o método de descida do gradiente para encontrar o mínimo da função de custo (o Erro Quadrático Médio). Como a superfície de erro em redes com múltiplas camadas possui diversos mínimos locais e não é convexa, o ponto de partida na superfície de erro determina o caminho que o gradiente tomará. Como os pesos iniciais de cada treinamento foram inicializados com valores aleatórios entre 0 e 1, cada treinamento parte de um ponto diferente do espaço de pesos. Isso resulta em:
- **Variação no número de épocas**: Dependendo de quão perto o ponto inicial está de um mínimo e da inclinação da superfície nesse ponto, a rede levará mais ou menos iterações para atingir a precisão desejada ($\epsilon = 10^{-6}$).
- **Variação no EQM**: A rede pode convergir para diferentes mínimos locais do erro quadrático médio em cada execução. Algumas configurações iniciais de pesos permitem que a rede encontre um mínimo mais profundo (menor EQM) do que outras.

## 5. Validação da rede no conjunto de teste

| Amostra | $x_1$ | $x_2$ | $x_3$ | $d$ | $y_{rede}$ (T1) | $y_{rede}$ (T2) | $y_{rede}$ (T3) | $y_{rede}$ (T4) | $y_{rede}$ (T5) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.0611 | 0.2860 | 0.7464 | 0.4831 | 0.5288 | 0.5106 | 0.5171 | 0.5221 | 0.5106 |
| 2 | 0.5102 | 0.7464 | 0.0860 | 0.5965 | 0.6047 | 0.6180 | 0.6146 | 0.6122 | 0.6165 |
| 3 | 0.0004 | 0.6916 | 0.5006 | 0.5318 | 0.5613 | 0.5544 | 0.5563 | 0.5595 | 0.5478 |
| 4 | 0.9430 | 0.4476 | 0.2648 | 0.6843 | 0.6802 | 0.6906 | 0.6880 | 0.6864 | 0.6940 |
| 5 | 0.1399 | 0.1610 | 0.2477 | 0.2872 | 0.3678 | 0.3679 | 0.3662 | 0.3696 | 0.3723 |
| 6 | 0.6423 | 0.3229 | 0.8567 | 0.7663 | 0.7149 | 0.7079 | 0.7092 | 0.7089 | 0.7087 |
| 7 | 0.6492 | 0.0007 | 0.6422 | 0.5666 | 0.5822 | 0.5775 | 0.5798 | 0.5835 | 0.5866 |
| 8 | 0.1818 | 0.5078 | 0.9046 | 0.6601 | 0.6668 | 0.6502 | 0.6549 | 0.6573 | 0.6464 |
| 9 | 0.7382 | 0.2647 | 0.1916 | 0.5427 | 0.5571 | 0.5695 | 0.5666 | 0.5681 | 0.5772 |
| 10 | 0.3879 | 0.1307 | 0.8656 | 0.5836 | 0.6095 | 0.5939 | 0.5996 | 0.6027 | 0.5980 |
| 11 | 0.1903 | 0.6523 | 0.7820 | 0.6950 | 0.6755 | 0.6632 | 0.6665 | 0.6684 | 0.6580 |
| 12 | 0.8401 | 0.4490 | 0.2719 | 0.6790 | 0.6580 | 0.6677 | 0.6653 | 0.6645 | 0.6712 |
| 13 | 0.0029 | 0.3264 | 0.2476 | 0.2956 | 0.3758 | 0.3768 | 0.3742 | 0.3788 | 0.3782 |
| 14 | 0.7088 | 0.9342 | 0.2763 | 0.7742 | 0.7411 | 0.7454 | 0.7454 | 0.7401 | 0.7423 |
| 15 | 0.1283 | 0.1882 | 0.7253 | 0.4662 | 0.5125 | 0.4954 | 0.5017 | 0.5068 | 0.4978 |
| 16 | 0.8882 | 0.3077 | 0.8931 | 0.8093 | 0.7626 | 0.7598 | 0.7592 | 0.7560 | 0.7591 |
| 17 | 0.2225 | 0.9182 | 0.7820 | 0.7581 | 0.7397 | 0.7309 | 0.7323 | 0.7329 | 0.7230 |
| 18 | 0.1957 | 0.8423 | 0.3085 | 0.5826 | 0.6067 | 0.6093 | 0.6085 | 0.6084 | 0.6029 |
| 19 | 0.9991 | 0.5914 | 0.3933 | 0.7938 | 0.7489 | 0.7539 | 0.7530 | 0.7486 | 0.7540 |
| 20 | 0.2299 | 0.1524 | 0.7353 | 0.5012 | 0.5346 | 0.5188 | 0.5249 | 0.5295 | 0.5226 |
| Erro Relativo Médio (%) | | | | | 6.7236% | 6.3417% | 6.4194% | 6.8326% | 6.6971% |
| Variância (%) | | | | | 54.4724% | 54.0509% | 50.9889% | 56.5853% | 57.1947% |

## 6. Melhor configuração de treinamento
A configuração final mais adequada para o sistema de ressonância magnética é a **T2**. Esta escolha é baseada na avaliação do conjunto de teste (validação cruzada holdout), que afere a capacidade de generalização da rede. A melhor generalização é obtida pelo modelo que produz o menor Erro Relativo Médio e menor Variância nos dados nunca vistos (conjunto de teste).