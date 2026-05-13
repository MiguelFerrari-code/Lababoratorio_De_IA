# Resultados da Atividade - PMC2

## Desempenho no Treinamento

| Método | Épocas | EQM Final | Tempo de Processamento (s) |
|---|---|---|---|
| Padrão | 30377 | 0.028742 | 4.92 |
| Momentum | 5870 | 0.019559 | 1.00 |

Os gráficos de EQM versus épocas foram gerados no arquivo `grafico_eqm.png`.

## Validação no Conjunto de Teste

| Amostra | $d_1$ | $d_2$ | $d_3$ | $y_1$ (Padrão) | $y_2$ (Padrão) | $y_3$ (Padrão) | $y_1$ (Momentum) | $y_2$ (Momentum) | $y_3$ (Momentum) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 3 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 4 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 5 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 6 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 7 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 8 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 9 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 10 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 11 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 12 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 13 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 14 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 15 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 16 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 17 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 18 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |

**Taxa de Acerto (Backpropagation Padrão):** 100.00%
**Taxa de Acerto (Backpropagation com Momentum):** 100.00%
