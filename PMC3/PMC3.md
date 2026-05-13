+---------+---+--------------+----------+-------------------+----+-------+
| ![Lo    |   | **Centro     |          |                   |    |       |
| gotipo, |   | Federal de   |          |                   |    |       |
| nome da |   | Educação     |          |                   |    |       |
| empresa |   | Tecnológica  |          |                   |    |       |
| De      |   | de Minas     |          |                   |    |       |
| scrição |   | Gerais**     |          |                   |    |       |
| gerada  |   |              |          |                   |    |       |
| a       |   | ***Campus    |          |                   |    |       |
| utomati |   | VIII --      |          |                   |    |       |
| camente |   | Varginha***  |          |                   |    |       |
| ](media |   |              |          |                   |    |       |
| /image1 |   | *            |          |                   |    |       |
| .jpeg){ |   | *Bacharelado |          |                   |    |       |
| width=" |   | em Sistemas  |          |                   |    |       |
| 0.77152 |   | de           |          |                   |    |       |
| 7777777 |   | Informação** |          |                   |    |       |
| 7778in" |   |              |          |                   |    |       |
| he      |   |              |          |                   |    |       |
| ight="0 |   |              |          |                   |    |       |
| .484722 |   |              |          |                   |    |       |
| 2222222 |   |              |          |                   |    |       |
| 222in"} |   |              |          |                   |    |       |
+---------+---+--------------+----------+-------------------+----+-------+
| **      |   |              | **TR     | ***Professor***   | *  | ***No |
| *Discip |   |              | ABALHO** |                   | ** | ta*** |
| lina*** |   |              |          | Lázaro Eduardo da | Va |       |
|         |   |              |          | Silva             | lo |       |
| Lab.    |   |              |          |                   | r* |       |
| Intel   |   |              |          |                   | ** |       |
| igência |   |              |          |                   |    |       |
| Art     |   |              |          |                   | 10 |       |
| ificial |   |              |          |                   | 0% |       |
+---------+---+--------------+----------+-------------------+----+-------+
| ***D    | * |              |          |                   |    |       |
| ata:*** | * |              |          |                   |    |       |
|         | * |              |          |                   |    |       |
| 13/     | A |              |          |                   |    |       |
| 05/2026 | l |              |          |                   |    |       |
|         | u |              |          |                   |    |       |
|         | n |              |          |                   |    |       |
|         | o |              |          |                   |    |       |
|         | ( |              |          |                   |    |       |
|         | a |              |          |                   |    |       |
|         | ) |              |          |                   |    |       |
|         | : |              |          |                   |    |       |
|         | * |              |          |                   |    |       |
|         | * |              |          |                   |    |       |
|         | * |              |          |                   |    |       |
+---------+---+--------------+----------+-------------------+----+-------+

O preço de uma determinada mercadoria disposta para ser comercializada
no mercado financeiro de ações possui um histórico de variação de valor
conforme mostrado na tabela apresentada no Apêndice.

Um pool de pesquisadores estará tentando aplicar redes neurais para
tentar prever o comportamento futuro deste processo. Assim, pretende-se
utilizar uma arquitetura perceptron multicamadas, com topologia "Time
Delay" (TDNN), conforme mostrado na figura abaixo:

As topologias candidatas para serem aplicadas no mapeamento do problema
acima são especificadas como segue:

**Rede 1** 05 entradas (*p* = 05) com N1 = 10

**Rede 2** 10 entradas (*p* = 10) com N1 = 15

**Rede 3** 15 entradas (*p* = 15) com N1 = 25

Utilizando o algoritmo de aprendizagem *backpropagation com momentum* e
os dados de treinamento apresentados no Anexo, realize as seguintes
atividades:

1.  Execute 3 treinamentos para cada rede perceptron acima inicializando
    as matrizes de pesos em cada treinamento com valores aleatórios
    entre 0 e 1. Se for o caso, reinicie o gerador de números aleatórios
    em cada treinamento de tal forma que os elementos das matrizes de
    pesos iniciais não sejam os mesmos. Utilize a função de ativação
    logística (*sigmoid*) para todos os neurônios, taxa de aprendizado η
    = 0.1, fator de momentum α= 0.8 e precisão ε = 0.5x10^-6^.

2.  Registre os resultados finais desses 3 treinamentos para cada uma
    das três topologias de rede na tabela a seguir:

  ---------------- -------- ---------- -------- ---------- -------- ----------
  Treinamento      **Rede              **Rede              **Rede   
                   1**                 2**                 3**      

                   EQM      Épocas     EQM      Épocas     EQM      Épocas

  1^o^ (T1)                                                         

  2^o^ (T2)                                                         

  3^o^ (T3)                                                         
  ---------------- -------- ---------- -------- ---------- -------- ----------

3.  Para todos os treinamentos efetuados no item 2, faça a validação da
    rede em relação aos valores desejados apresentados na tabela abaixo.
    Forneça para cada treinamento o erro relativo médio entre os valores
    desejados e os valores fornecidos pela rede em relação a todos os
    padrões de teste. Obtenha também a respectiva variância.

  ------------ ---------- -------- ------ ------ -------- ------ ------ -------- ------ ------
                          **Rede                 **Rede                 **Rede          
                          1**                    2**                    3**             

  Amostra      *f*(*t*)   (T1)     (T2)   (T3)   (T1)     (T2)   (T3)   (T1)     (T2)   (T3)

  *t* = 101    0.4173                                                                   

  *t* = 102    0.0062                                                                   

  *t* = 103    0.3387                                                                   

  *t* = 104    0.1886                                                                   

  *t* = 105    0.7418                                                                   

  *t* = 106    0.3138                                                                   

  *t* = 107    0.4466                                                                   

  *t* = 108    0.0835                                                                   

  *t* = 109    0.1930                                                                   

  *t* = 110    0.3807                                                                   

  *t* = 111    0.5438                                                                   

  *t* = 112    0.5897                                                                   

  *t* = 113    0.3536                                                                   

  *t* = 114    0.2210                                                                   

  *t* = 115    0.0631                                                                   

  *t* = 116    0.4499                                                                   

  *t* = 117    0.2564                                                                   

  *t* = 118    0.7642                                                                   

  *t* = 119    0.1411                                                                   

  *t* = 120    0.3626                                                                   

  Erro                                                                                  
  Relativo                                                                              
  Médio:                                                                                

  Variância:                                                                            
  ------------ ---------- -------- ------ ------ -------- ------ ------ -------- ------ ------

4.  Para cada uma das topologias apresentadas na tabela acima,
    considerando ainda o melhor treinamento {T1, T2 ou T3} realizado em
    cada uma delas, trace o gráfico dos valores de erro quadrático médio
    (EQM) em função de cada época de treinamento. Imprima os três
    gráficos numa mesma folha de modo não superpostos.

5.  Para cada uma das topologias apresentadas na tabela acima,
    considerando ainda o melhor treinamento {T1, T2 ou T3} realizado em
    cada uma delas, trace o gráfico dos valores desejados e dos valores
    estimados pela respectiva rede em função do domínio de estimação
    considerado (*t*=101..120). Imprima os três gráficos numa mesma
    folha de modo não superpostos.

6.  Baseado nas análises dos itens acima, indique qual das topologias
    candidatas {Rede 1, Rede 2 ou Rede 3} e com que qual configuração
    final de treinamento {T1 , T2 ou T3} seria a mais adequada para
    realização de previsões neste processo.

7.  Em relação aos algoritmos de treinamento que são variantes do
    algoritmo *backpropagation*, investigue e comente sobre as
    principais características e vantagens dos seguintes algoritmos:

    a.  Algoritmo de treinamento Resilient-Propagation (RProp).

    b.  Algoritmo de treinamento Levenberg-Marquardt (LM).

## ANEXO

+--------+--------+--------+--------+--------+--------+--------+--------+
| #### A | ***f*( | #### A | ***f*( | #### A | ***f*( | #### A | ***f*( |
| mostra | *t*)** | mostra | *t*)** | mostra | *t*)** | mostra | *t*)** |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.1701 | *t* =  | 0.2398 | *t* =  | 0.3087 | *t* =  | 0.3701 |
| 1      |        | 26     |        | 51     |        | 76     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.1023 | *t* =  | 0.0508 | *t* =  | 0.0159 | *t* =  | 0.0006 |
| 2      |        | 27     |        | 52     |        | 77     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.4405 | *t* =  | 0.4497 | *t* =  | 0.4330 | *t* =  | 0.3943 |
| 3      |        | 28     |        | 53     |        | 78     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.3609 | *t* =  | 0.2178 | *t* =  | 0.0733 | *t* =  | 0.0646 |
| 4      |        | 29     |        | 54     |        | 79     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.7192 | *t* =  | 0.7762 | *t* =  | 0.7995 | *t* =  | 0.7878 |
| 5      |        | 30     |        | 55     |        | 80     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.2258 | *t* =  | 0.1078 | *t* =  | 0.0262 | *t* =  | 0.1694 |
| 6      |        | 31     |        | 56     |        | 81     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.3175 | *t* =  | 0.3773 | *t* =  | 0.4223 | *t* =  | 0.4468 |
| 7      |        | 32     |        | 57     |        | 82     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.0127 | *t* =  | 0.0001 | *t* =  | 0.0085 | *t* =  | 0.0372 |
| 8      |        | 33     |        | 58     |        | 83     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.4290 | *t* =  | 0.3877 | *t* =  | 0.3303 | *t* =  | 0.2632 |
| 9      |        | 34     |        | 59     |        | 84     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.0544 | *t* =  | 0.0821 | *t* =  | 0.2037 | *t* =  | 0.3048 |
| 10     |        | 35     |        | 60     |        | 85     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.8000 | *t* =  | 0.7836 | *t* =  | 0.7332 | *t* =  | 0.6516 |
| 11     |        | 36     |        | 61     |        | 86     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.0450 | *t* =  | 0.1887 | *t* =  | 0.3328 | *t* =  | 0.4690 |
| 12     |        | 37     |        | 62     |        | 87     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.4268 | *t* =  | 0.4483 | *t* =  | 0.4445 | *t* =  | 0.4132 |
| 13     |        | 38     |        | 63     |        | 88     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.0112 | *t* =  | 0.0424 | *t* =  | 0.0909 | *t* =  | 0.1523 |
| 14     |        | 39     |        | 64     |        | 89     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.3218 | *t* =  | 0.2539 | *t* =  | 0.1838 | *t* =  | 0.1182 |
| 15     |        | 40     |        | 65     |        | 90     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.2185 | *t* =  | 0.3164 | *t* =  | 0.3888 | *t* =  | 0.4334 |
| 16     |        | 41     |        | 66     |        | 91     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.7240 | *t* =  | 0.6386 | *t* =  | 0.5277 | *t* =  | 0.3978 |
| 17     |        | 42     |        | 67     |        | 92     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.3516 | *t* =  | 0.4862 | *t* =  | 0.6042 | *t* =  | 0.6987 |
| 18     |        | 43     |        | 68     |        | 93     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.4420 | *t* =  | 0.4068 | *t* =  | 0.3435 | *t* =  | 0.2538 |
| 19     |        | 44     |        | 69     |        | 94     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.0984 | *t* =  | 0.1611 | *t* =  | 0.2304 | *t* =  | 0.2998 |
| 20     |        | 45     |        | 70     |        | 95     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.1747 | *t* =  | 0.1101 | *t* =  | 0.0568 | *t* =  | 0.0195 |
| 21     |        | 46     |        | 71     |        | 96     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.3964 | *t* =  | 0.4372 | *t* =  | 0.4500 | *t* =  | 0.4366 |
| 22     |        | 47     |        | 72     |        | 97     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.5114 | *t* =  | 0.3795 | *t* =  | 0.2371 | *t* =  | 0.0924 |
| 23     |        | 48     |        | 73     |        | 98     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.6183 | *t* =  | 0.7092 | *t* =  | 0.7705 | *t* =  | 0.7984 |
| 24     |        | 49     |        | 74     |        | 99     |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| *t* =  | 0.3330 | *t* =  | 0.2400 | *t* =  | 0.1246 | *t* =  | 0.0077 |
| 25     |        | 50     |        | 75     |        | 100    |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
