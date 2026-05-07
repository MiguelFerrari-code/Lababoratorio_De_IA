# Atividade 2 - Classificação de Óleo com Perceptron

=== TABELA 1: RESULTADOS DOS TREINAMENTOS ===
| Treinamento | w0 inicial | w1 inicial | w2 inicial | w3 inicial | w0 final | w1 final | w2 final | w3 final | Épocas |
|---|---|---|---|---|---|---|---|---|---|
| 1º (T1) | 0.9975 | 0.5182 | 0.4486 | 0.0477 | -3.0425 | 1.5588 | 2.4785 | -0.7290 | 421 |
| 2º (T2) | 0.2418 | 0.2472 | 0.1605 | 0.3898 | -3.1982 | 1.6107 | 2.5564 | -0.7588 | 444 |
| 3º (T3) | 0.5199 | 0.5732 | 0.6756 | 0.5317 | -3.0801 | 1.5568 | 2.4714 | -0.7345 | 399 |
| 4º (T4) | 0.5527 | 0.8663 | 0.0793 | 0.0576 | -3.0873 | 1.5789 | 2.4778 | -0.7371 | 417 |
| 5º (T5) | 0.3101 | 0.7602 | 0.5749 | 0.7544 | -3.0299 | 1.5190 | 2.4608 | -0.7254 | 380 |


## Classificação Automática das Amostras (Teste)

=== TABELA 2: CLASSIFICAÇÃO DAS AMOSTRAS DE TESTE ===
| Amostra | x1 | x2 | x3 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |
|---|---|---|---|---|---|---|---|---|
| 1 | -0.3565 | 0.0620 | 5.9891 | -1 | -1 | -1 | -1 | -1 |
| 2 | -0.7842 | 1.1267 | 5.5912 | 1 | 1 | 1 | 1 | 1 |
| 3 | 0.3012 | 0.5611 | 5.8234 | 1 | 1 | 1 | 1 | 1 |
| 4 | 0.7757 | 1.0648 | 8.0677 | 1 | 1 | 1 | 1 | 1 |
| 5 | 0.1570 | 0.8028 | 6.3040 | 1 | 1 | 1 | 1 | 1 |
| 6 | -0.7014 | 1.0316 | 3.6005 | 1 | 1 | 1 | 1 | 1 |
| 7 | 0.3748 | 0.1536 | 6.1537 | -1 | -1 | -1 | -1 | -1 |
| 8 | -0.6920 | 0.9404 | 4.4058 | 1 | 1 | 1 | 1 | 1 |
| 9 | -1.3970 | 0.7141 | 4.9263 | -1 | -1 | -1 | -1 | -1 |
| 10 | -1.8842 | -0.2805 | 1.2548 | -1 | -1 | -1 | -1 | -1 |


**1. Explique por que o número de épocas de treinamento varia a cada vez que executamos o treinamento do perceptron.**
O número de épocas varia porque o vetor de pesos ($w_0, w_1, w_2, w_3$) é inicializado com valores totalmente aleatórios (entre 0 e 1) no começo de cada treinamento[cite: 1]. Como o ponto de partida matemático na busca pela solução é diferente a cada tentativa, a quantidade de ajustes necessários (iterações/épocas) para que o algoritmo convirja e encontre o "hiperplano separador" ideal também muda. 

**2. Qual a principal limitação do perceptron quando aplicado em problemas de classificação de padrões?**
A principal limitação do Perceptron de camada única é que ele só consegue resolver problemas que sejam **linearmente separáveis**. Ou seja, ele só será capaz de classificar perfeitamente os óleos[cite: 1] se for possível traçar uma reta (ou um plano/hiperplano bidimensional/tridimensional) reta e contínua que separe perfeitamente todas as amostras da Classe 1 das amostras da Classe 2 no espaço.