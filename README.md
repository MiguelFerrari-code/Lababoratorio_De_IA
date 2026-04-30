# Resolução da Atividade: Classificação com Perceptron

## 1. Treinamento da Rede Perceptron

Foram executados 5 treinamentos para a rede, cada um com pesos inicialmente aleatórios (entre 0 e 1). A taxa de aprendizado foi de 0.01.

| Treinamento | $w_0$ Inicial | $w_1$ Inicial | $w_2$ Inicial | $w_3$ Inicial | $w_0$ Final | $w_1$ Final | $w_2$ Final | $w_3$ Final | Número de Épocas |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1º (T1)** | 0.6394 | 0.0250 | 0.2750 | 0.2232 | -3.0606 | 1.5213 | 2.4551 | -0.7267 | 403 |
| **2º (T2)** | 0.5826 | 0.6802 | 0.4871 | 0.4860 | -3.1574 | 1.5953 | 2.5352 | -0.7500 | 445 |
| **3º (T3)** | 0.3354 | 0.4961 | 0.9619 | 0.6244 | -3.0646 | 1.5573 | 2.4581 | -0.7298 | 402 |
| **4º (T4)** | 0.1208 | 0.5836 | 0.0701 | 0.4826 | -3.0792 | 1.5603 | 2.4826 | -0.7351 | 407 |
| **5º (T5)** | 0.3664 | 0.4451 | 0.4506 | 0.4230 | -2.8936 | 1.4207 | 2.3831 | -0.6744 | 339 |

*Nota: Os pesos foram arredondados para 4 casas decimais para melhor visualização.*



## 2. Classificação Automática de Amostras de Óleo

Após os 5 treinamentos, o perceptron foi aplicado na classificação automática das amostras de teste fornecidas, resultando na seguinte tabela de classes. (Lembrando que -1 refere-se à classe C1 e 1 refere-se à classe C2).

| Amostra | $x_1$ | $x_2$ | $x_3$ | y(T1) | y(T2) | y(T3) | y(T4) | y(T5) | Classe Final |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | -0.3565 | 0.0620 | 5.9891 | -1 | -1 | -1 | -1 | -1 | **C1** |
| **2** | -0.7842 | 1.1267 | 5.5912 | 1 | 1 | 1 | 1 | 1 | **C2** |
| **3** | 0.3012 | 0.5611 | 5.8234 | 1 | 1 | 1 | 1 | 1 | **C2** |
| **4** | 0.7757 | 1.0648 | 8.0677 | 1 | 1 | 1 | 1 | 1 | **C2** |
| **5** | 0.1570 | 0.8028 | 6.3040 | 1 | 1 | 1 | 1 | 1 | **C2** |
| **6** | -0.7014 | 1.0316 | 3.6005 | 1 | 1 | 1 | 1 | 1 | **C2** |
| **7** | 0.3748 | 0.1536 | 6.1537 | -1 | -1 | -1 | -1 | -1 | **C1** |
| **8** | -0.6920 | 0.9404 | 4.4058 | 1 | 1 | 1 | 1 | 1 | **C2** |
| **9** | -1.3970 | 0.7141 | 4.9263 | -1 | -1 | -1 | -1 | -1 | **C1** |
| **10** | -1.8842 | -0.2805 | 1.2548 | -1 | -1 | -1 | -1 | -1 | **C1** |

---

## 3. Respostas das Questões Teóricas

> **Explique por que o número de épocas de treinamento varia a cada vez que executamos o treinamento do perceptron.**

O número de épocas varia porque os pesos iniciais da rede são configurados com valores aleatórios diferentes a cada execução do treinamento. Esses pesos iniciais definem a posição e a orientação iniciais da fronteira de decisão (o hiperplano) que separa as classes no espaço de características. Como o perceptron de Hebb ajusta iterativamente esse hiperplano baseando-se nos erros de classificação, começar a busca a partir de posições iniciais distintas faz com que o algoritmo siga caminhos diferentes e precise de quantidades diferentes de ajustes (iterações/épocas) até que convirja para uma fronteira que separe as classes perfeitamente.

> **Qual a principal limitação do perceptron quando aplicado em problemas de classificação de padrões.**

A principal limitação do Perceptron clássico (de uma única camada) é que ele consegue classificar corretamente e convergir **apenas em problemas que são linearmente separáveis**. Isso significa que deve ser possível traçar uma reta (ou um hiperplano único, em múltiplas dimensões) que separe completamente as duas classes. Caso os dados não sejam linearmente separáveis (como no caso clássico do problema lógico XOR – Ou Exclusivo), o algoritmo do perceptron não conseguirá convergir, entrando em um loop de repetição sem nunca zerar o erro. Para problemas não linearmente separáveis, deve-se usar redes mais complexas, como os Perceptrons de Múltiplas Camadas (Multilayer Perceptrons - MLP).

