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

No processamento de bebidas, a aplicação de um determinado conservante é
feita em função da combinação de 04 variáveis reais definidas por *x*~1~
(teor de água), *x*~2~ (grau de acidez), *x*~3~ (temperatura) e *x*~4~
(tensão superficial). Sabe-se que existem apenas três tipos de
conservantes que podem ser aplicados, os quais são definidos por tipo A,
B e C. A partir dessas variáveis, realizam-se ensaios em laboratório
para especificar que tipo de conservante deve ser aplicado em
determinada bebida.

A partir de 148 ensaios feitos em laboratório, a equipe de engenheiros e
cientistas resolveu aplicar uma rede perceptron multicamadas como
classificadora de padrões, visando que a mesma identifique qual
conservante será aplicado em determinado lote de bebida. Por questões
operacionais da própria linha de produção, utilizar-se-á uma rede
perceptron com três saídas conforme apresentado na figura abaixo.

A padronização para a saída, representando o conservante a ser aplicado,
ficou definida da seguinte forma:

  ----------------------------------- ----------- ------------ -----------
  Tipo de Conservante                 *y*~1~      *y*~2~       *y*~3~

  Tipo A                              1           0            0

  Tipo B                              0           1            0

  Tipo C                              0           0            1
  ----------------------------------- ----------- ------------ -----------

Utilizando os dados de treinamento apresentados no Anexo, execute o
treinamento de uma rede perceptron multicamadas (04 entradas e 03
saídas) que possa classificar, em função apenas dos valores medidos de
*x*~1~, *x*~2~, *x*~3~ e *x*~4~ (já normalizados), qual o tipo de
conservante que pode ser aplicado em determinada bebida. Para tanto,
faça as seguintes atividades:

1.  Execute o treinamento da rede Perceptron através do algoritmo de
    > aprendizagem ***backpropagation* *padrão***, inicializando as
    > matrizes de pesos com valores aleatórios entre 0 e 1. Utilize a
    > função de ativação logística (*sigmoid*) para todos os neurônios,
    > taxa de aprendizado η = 0.1 e precisão ε = 10^-6^.

2.  Execute o treinamento da rede Perceptron através do algoritmo de
    > aprendizagem ***backpropagation com momentum***, utilizando as
    > mesmas matrizes de pesos iniciais que foram usadas no item
    > anterior. Utilize a função de ativação logística (*sigmoid*) para
    > todos os neurônios, taxa de aprendizado η = 0.1, fator de momentum
    > α= 0.9 e precisão ε = 10^-6^.

Para os dois treinamentos realizados acima, trace os respectivos
gráficos dos valores de erro quadrático médio (EQM) em função de cada
época de treinamento. Imprima os dois gráficos numa mesma folha de modo
não superpostos. Meça também o tempo de processamento envolvido com cada
treinamento.

3.  Dado que o problema se configura como um típico processo de
    > classificação de padrões, implemente a rotina que faz o
    > pós-processamento das saídas fornecidas pela rede (números reais)
    > para números inteiros. Utilize o critério do arredondamento
    > simétrico:

> ![](media/image2.wmf), utilizado apenas no pós-processamento do
> conjunto de teste.

4.  Faça a validação da rede aplicando o conjunto de teste fornecido na
    > tabela abaixo. Forneça a taxa de acerto (%) entre os valores
    > desejados e os valores fornecidos pela rede (após o
    > pós-processamento) em relação a todos os padrões de teste.

## 

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h1 id="amostra">Amostra</h1></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>x</em><sub>4</sub></td>
<td><em>d</em><sub>1</sub></td>
<td><em>d</em><sub>2</sub></td>
<td><em>d</em><sub>3</sub></td>
<td><img src="media/image3.wmf" /></td>
<td><img src="media/image4.wmf" /></td>
<td><img src="media/image5.wmf" /></td>
<td><em>y</em><sub>1</sub></td>
<td><em>y</em><sub>2</sub></td>
<td><em>y</em><sub>3</sub></td>
</tr>
<tr class="even">
<td>1</td>
<td>0.8622</td>
<td>0.7101</td>
<td>0.6236</td>
<td>0.7894</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>0.2741</td>
<td>0.1552</td>
<td>0.1333</td>
<td>0.1516</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>3</td>
<td>0.6772</td>
<td>0.8516</td>
<td>0.6543</td>
<td>0.7573</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>4</td>
<td>0.2178</td>
<td>0.5039</td>
<td>0.6415</td>
<td>0.5039</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5</td>
<td>0.7260</td>
<td>0.7500</td>
<td>0.7007</td>
<td>0.4953</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6</td>
<td>0.2473</td>
<td>0.2941</td>
<td>0.4248</td>
<td>0.3087</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7</td>
<td>0.5682</td>
<td>0.5683</td>
<td>0.5054</td>
<td>0.4426</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>8</td>
<td>0.6566</td>
<td>0.6715</td>
<td>0.4952</td>
<td>0.3951</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>0.0705</td>
<td>0.4717</td>
<td>0.2921</td>
<td>0.2954</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>10</td>
<td>0.1187</td>
<td>0.2568</td>
<td>0.3140</td>
<td>0.3037</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>0.5673</td>
<td>0.7011</td>
<td>0.4083</td>
<td>0.5552</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>12</td>
<td>0.3164</td>
<td>0.2251</td>
<td>0.3526</td>
<td>0.2560</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>13</td>
<td>0.7884</td>
<td>0.9568</td>
<td>0.6825</td>
<td>0.6398</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>14</td>
<td>0.9633</td>
<td>0.7850</td>
<td>0.6777</td>
<td>0.6059</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>15</td>
<td>0.7739</td>
<td>0.8505</td>
<td>0.7934</td>
<td>0.6626</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>0.4219</td>
<td>0.4136</td>
<td>0.1408</td>
<td>0.0940</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>17</td>
<td>0.6616</td>
<td>0.4365</td>
<td>0.6597</td>
<td>0.8129</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>18</td>
<td>0.7325</td>
<td>0.4761</td>
<td>0.3888</td>
<td>0.5683</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="14">Taxa de Acerto:</td>
</tr>
</tbody>
</table>

##  ANEXO

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="amostra-1">Amostra</h4></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>x</em><sub>4</sub></td>
<td><em>d</em><sub>1</sub></td>
<td><em>d</em><sub>2</sub></td>
<td><em>d</em><sub>3</sub></td>
<td><h3 id="amostra-2">Amostra</h3></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>x</em><sub>4</sub></td>
<td><em>d</em><sub>1</sub></td>
<td><em>d</em><sub>2</sub></td>
<td><em>d</em><sub>3</sub></td>
</tr>
<tr class="even">
<td><strong>1</strong></td>
<td>0.3841</td>
<td>0.2021</td>
<td>0.0000</td>
<td>0.2438</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>71</strong></td>
<td>0.3460</td>
<td>0.2722</td>
<td>0.1866</td>
<td>0.5049</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>2</strong></td>
<td>0.1765</td>
<td>0.1613</td>
<td>0.3401</td>
<td>0.0843</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>72</strong></td>
<td>0.2241</td>
<td>0.2046</td>
<td>0.3575</td>
<td>0.2891</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>3</strong></td>
<td>0.3170</td>
<td>0.5786</td>
<td>0.3387</td>
<td>0.4192</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>73</strong></td>
<td>0.1412</td>
<td>0.2264</td>
<td>0.4025</td>
<td>0.2661</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>4</strong></td>
<td>0.2467</td>
<td>0.0337</td>
<td>0.2699</td>
<td>0.3454</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>74</strong></td>
<td>0.5782</td>
<td>0.6418</td>
<td>0.7212</td>
<td>0.6396</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>5</strong></td>
<td>0.6102</td>
<td>0.8192</td>
<td>0.4679</td>
<td>0.4762</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>75</strong></td>
<td>0.9153</td>
<td>0.6571</td>
<td>0.8229</td>
<td>0.6689</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>6</strong></td>
<td>0.7030</td>
<td>0.7784</td>
<td>0.7482</td>
<td>0.6562</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>76</strong></td>
<td>0.6014</td>
<td>0.7664</td>
<td>0.6385</td>
<td>0.5513</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>7</strong></td>
<td>0.4767</td>
<td>0.4348</td>
<td>0.4852</td>
<td>0.3640</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>77</strong></td>
<td>0.7328</td>
<td>0.8708</td>
<td>0.8812</td>
<td>0.7060</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>8</strong></td>
<td>0.7589</td>
<td>0.8256</td>
<td>0.6514</td>
<td>0.6143</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>78</strong></td>
<td>0.4270</td>
<td>0.6352</td>
<td>0.6811</td>
<td>0.3884</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>9</strong></td>
<td>0.1579</td>
<td>0.3641</td>
<td>0.2551</td>
<td>0.2919</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>79</strong></td>
<td>0.6189</td>
<td>0.1652</td>
<td>0.4016</td>
<td>0.3042</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>10</strong></td>
<td>0.5561</td>
<td>0.5602</td>
<td>0.5605</td>
<td>0.2105</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>80</strong></td>
<td>0.2143</td>
<td>0.3868</td>
<td>0.1926</td>
<td>0.0000</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>11</strong></td>
<td>0.3267</td>
<td>0.2974</td>
<td>0.0343</td>
<td>0.1466</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>81</strong></td>
<td>0.5696</td>
<td>0.7238</td>
<td>0.7199</td>
<td>0.6677</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>12</strong></td>
<td>0.2303</td>
<td>0.0942</td>
<td>0.3889</td>
<td>0.1713</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>82</strong></td>
<td>0.8656</td>
<td>0.6700</td>
<td>0.6570</td>
<td>0.6065</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>13</strong></td>
<td>0.2953</td>
<td>0.2963</td>
<td>0.2600</td>
<td>0.3039</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>83</strong></td>
<td>0.9002</td>
<td>0.6858</td>
<td>0.7409</td>
<td>0.7047</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>14</strong></td>
<td>0.5797</td>
<td>0.4789</td>
<td>0.5780</td>
<td>0.3048</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>84</strong></td>
<td>0.4167</td>
<td>0.5255</td>
<td>0.5506</td>
<td>0.4093</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>15</strong></td>
<td>0.5860</td>
<td>0.5250</td>
<td>0.4792</td>
<td>0.4021</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>85</strong></td>
<td>0.8325</td>
<td>0.4804</td>
<td>0.7990</td>
<td>0.7471</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>16</strong></td>
<td>0.7045</td>
<td>0.6933</td>
<td>0.6449</td>
<td>0.6623</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>86</strong></td>
<td>0.4124</td>
<td>0.1191</td>
<td>0.4720</td>
<td>0.3184</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>17</strong></td>
<td>0.9134</td>
<td>0.9412</td>
<td>0.6078</td>
<td>0.5934</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>87</strong></td>
<td>1.0000</td>
<td>1.0000</td>
<td>0.7924</td>
<td>0.7074</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>18</strong></td>
<td>0.2333</td>
<td>0.4943</td>
<td>0.2525</td>
<td>0.2567</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>88</strong></td>
<td>0.5685</td>
<td>0.6924</td>
<td>0.6180</td>
<td>0.5792</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>19</strong></td>
<td>0.2676</td>
<td>0.4172</td>
<td>0.2775</td>
<td>0.2721</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>89</strong></td>
<td>0.6505</td>
<td>0.4864</td>
<td>0.2972</td>
<td>0.4599</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>20</strong></td>
<td>0.4850</td>
<td>0.5506</td>
<td>0.5269</td>
<td>0.6036</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>90</strong></td>
<td>0.8124</td>
<td>0.7690</td>
<td>0.9720</td>
<td>1.0000</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>21</strong></td>
<td>0.2434</td>
<td>0.2567</td>
<td>0.2312</td>
<td>0.2624</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>91</strong></td>
<td>0.9013</td>
<td>0.7160</td>
<td>1.0000</td>
<td>0.8046</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>22</strong></td>
<td>0.1250</td>
<td>0.3023</td>
<td>0.1826</td>
<td>0.3168</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>92</strong></td>
<td>0.8872</td>
<td>0.7556</td>
<td>0.9307</td>
<td>0.6791</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>23</strong></td>
<td>0.5598</td>
<td>0.4253</td>
<td>0.4258</td>
<td>0.3192</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>93</strong></td>
<td>0.3708</td>
<td>0.2139</td>
<td>0.2136</td>
<td>0.4295</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>24</strong></td>
<td>0.5738</td>
<td>0.7674</td>
<td>0.6154</td>
<td>0.4447</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>94</strong></td>
<td>0.5159</td>
<td>0.4349</td>
<td>0.3715</td>
<td>0.4086</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>25</strong></td>
<td>0.5692</td>
<td>0.8368</td>
<td>0.5832</td>
<td>0.4585</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>95</strong></td>
<td>0.6768</td>
<td>0.6304</td>
<td>0.8044</td>
<td>0.4885</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>26</strong></td>
<td>0.4655</td>
<td>0.7682</td>
<td>0.3221</td>
<td>0.2940</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>96</strong></td>
<td>0.1664</td>
<td>0.2404</td>
<td>0.2000</td>
<td>0.3425</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>27</strong></td>
<td>0.5568</td>
<td>0.7592</td>
<td>0.6293</td>
<td>0.5453</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>97</strong></td>
<td>0.2495</td>
<td>0.2807</td>
<td>0.4679</td>
<td>0.2200</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>28</strong></td>
<td>0.8842</td>
<td>0.7509</td>
<td>0.5723</td>
<td>0.5814</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>98</strong></td>
<td>0.2487</td>
<td>0.2348</td>
<td>0.0913</td>
<td>0.1281</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>29</strong></td>
<td>0.7959</td>
<td>0.9243</td>
<td>0.7339</td>
<td>0.7334</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>99</strong></td>
<td>0.5748</td>
<td>0.8552</td>
<td>0.5973</td>
<td>0.7317</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>30</strong></td>
<td>0.7124</td>
<td>0.7128</td>
<td>0.6065</td>
<td>0.6668</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>100</strong></td>
<td>0.3858</td>
<td>0.7585</td>
<td>0.3239</td>
<td>0.3565</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>31</strong></td>
<td>0.6749</td>
<td>0.8767</td>
<td>0.6543</td>
<td>0.7461</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>101</strong></td>
<td>0.3329</td>
<td>0.4946</td>
<td>0.5614</td>
<td>0.3152</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>32</strong></td>
<td>0.3674</td>
<td>0.4359</td>
<td>0.4230</td>
<td>0.2965</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>102</strong></td>
<td>0.3891</td>
<td>0.4805</td>
<td>0.7598</td>
<td>0.4231</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>33</strong></td>
<td>0.3473</td>
<td>0.0754</td>
<td>0.2183</td>
<td>0.1905</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>103</strong></td>
<td>0.2888</td>
<td>0.4888</td>
<td>0.1930</td>
<td>0.0177</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>34</strong></td>
<td>0.6931</td>
<td>0.5188</td>
<td>0.5386</td>
<td>0.5794</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>104</strong></td>
<td>0.3827</td>
<td>0.4900</td>
<td>0.2272</td>
<td>0.3599</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>35</strong></td>
<td>0.6439</td>
<td>0.4959</td>
<td>0.4322</td>
<td>0.4582</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>105</strong></td>
<td>0.6047</td>
<td>0.4224</td>
<td>0.6274</td>
<td>0.5809</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>36</strong></td>
<td>0.5627</td>
<td>0.4893</td>
<td>0.6831</td>
<td>0.5120</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>106</strong></td>
<td>0.9840</td>
<td>0.7031</td>
<td>0.6469</td>
<td>0.4701</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>37</strong></td>
<td>0.5182</td>
<td>0.7553</td>
<td>0.6368</td>
<td>0.4538</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>107</strong></td>
<td>0.6554</td>
<td>0.6785</td>
<td>0.9279</td>
<td>0.7723</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>38</strong></td>
<td>0.6046</td>
<td>0.7479</td>
<td>0.6542</td>
<td>0.4375</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>108</strong></td>
<td>0.0466</td>
<td>0.3388</td>
<td>0.0840</td>
<td>0.0762</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>39</strong></td>
<td>0.6328</td>
<td>0.6786</td>
<td>0.7751</td>
<td>0.6183</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>109</strong></td>
<td>0.6154</td>
<td>0.8196</td>
<td>0.6339</td>
<td>0.7729</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>40</strong></td>
<td>0.3429</td>
<td>0.4694</td>
<td>0.2855</td>
<td>0.2977</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>110</strong></td>
<td>0.8452</td>
<td>0.8897</td>
<td>0.8383</td>
<td>0.6961</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>41</strong></td>
<td>0.6371</td>
<td>0.5069</td>
<td>0.5316</td>
<td>0.4520</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>111</strong></td>
<td>0.6927</td>
<td>0.7870</td>
<td>0.7689</td>
<td>0.7213</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>42</strong></td>
<td>0.6388</td>
<td>0.6970</td>
<td>0.6407</td>
<td>0.7677</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>112</strong></td>
<td>0.4032</td>
<td>0.6188</td>
<td>0.4930</td>
<td>0.5380</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>43</strong></td>
<td>0.3529</td>
<td>0.5504</td>
<td>0.3706</td>
<td>0.4828</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>113</strong></td>
<td>0.4006</td>
<td>0.3094</td>
<td>0.3868</td>
<td>0.0811</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>44</strong></td>
<td>0.4302</td>
<td>0.3237</td>
<td>0.6397</td>
<td>0.4319</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>114</strong></td>
<td>0.7416</td>
<td>0.7138</td>
<td>0.6823</td>
<td>0.6067</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>45</strong></td>
<td>0.7078</td>
<td>0.9604</td>
<td>0.7470</td>
<td>0.6399</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>115</strong></td>
<td>0.7404</td>
<td>0.6764</td>
<td>0.8293</td>
<td>0.4694</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>46</strong></td>
<td>0.7350</td>
<td>0.8170</td>
<td>0.7227</td>
<td>0.6279</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>116</strong></td>
<td>0.7736</td>
<td>0.7097</td>
<td>0.6826</td>
<td>0.8142</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>47</strong></td>
<td>0.7011</td>
<td>0.2946</td>
<td>0.6625</td>
<td>0.4312</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>117</strong></td>
<td>0.5823</td>
<td>0.9635</td>
<td>0.3706</td>
<td>0.5636</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>48</strong></td>
<td>0.5961</td>
<td>0.3817</td>
<td>0.6363</td>
<td>0.3663</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>118</strong></td>
<td>0.2081</td>
<td>0.3738</td>
<td>0.3119</td>
<td>0.3552</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>49</strong></td>
<td>0.0000</td>
<td>0.2563</td>
<td>0.2603</td>
<td>0.3027</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>119</strong></td>
<td>0.5616</td>
<td>0.8972</td>
<td>0.5186</td>
<td>0.6650</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><strong>50</strong></td>
<td>0.5996</td>
<td>0.5704</td>
<td>0.6965</td>
<td>0.6548</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>120</strong></td>
<td>0.6594</td>
<td>0.8907</td>
<td>0.6000</td>
<td>0.7157</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>51</strong></td>
<td>0.4289</td>
<td>0.3709</td>
<td>0.3994</td>
<td>0.3656</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>121</strong></td>
<td>0.3979</td>
<td>0.3070</td>
<td>0.3637</td>
<td>0.1220</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>52</strong></td>
<td>0.2093</td>
<td>0.3655</td>
<td>0.3334</td>
<td>0.1802</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>122</strong></td>
<td>0.2644</td>
<td>0.0000</td>
<td>0.3572</td>
<td>0.1931</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>53</strong></td>
<td>0.2335</td>
<td>0.2856</td>
<td>0.3912</td>
<td>0.1601</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>123</strong></td>
<td>0.4816</td>
<td>0.4791</td>
<td>0.4213</td>
<td>0.5889</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>54</strong></td>
<td>0.3266</td>
<td>0.7751</td>
<td>0.4356</td>
<td>0.3448</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>124</strong></td>
<td>0.0848</td>
<td>0.0749</td>
<td>0.4349</td>
<td>0.3328</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>55</strong></td>
<td>0.2457</td>
<td>0.1203</td>
<td>0.1228</td>
<td>0.2206</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>125</strong></td>
<td>0.4608</td>
<td>0.6775</td>
<td>0.3533</td>
<td>0.3016</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>56</strong></td>
<td>0.4656</td>
<td>0.4815</td>
<td>0.4211</td>
<td>0.4862</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td><strong>126</strong></td>
<td>0.4155</td>
<td>0.6589</td>
<td>0.5310</td>
<td>0.5404</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>57</strong></td>
<td>0.7511</td>
<td>0.8868</td>
<td>0.5408</td>
<td>0.6253</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>127</strong></td>
<td>0.3934</td>
<td>0.6244</td>
<td>0.4817</td>
<td>0.4324</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>58</strong></td>
<td>0.7825</td>
<td>0.9386</td>
<td>0.6510</td>
<td>0.6996</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>128</strong></td>
<td>0.5843</td>
<td>0.8517</td>
<td>0.8576</td>
<td>0.7133</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><strong>59</strong></td>
<td>0.3463</td>
<td>0.4118</td>
<td>0.2507</td>
<td>0.0454</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>129</strong></td>
<td>0.1995</td>
<td>0.3690</td>
<td>0.3537</td>
<td>0.3462</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><strong>60</strong></td>
<td>0.5172</td>
<td>0.1482</td>
<td>0.3172</td>
<td>0.2323</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>130</strong></td>
<td>0.3832</td>
<td>0.2321</td>
<td>0.0341</td>
<td>0.2450</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><strong>61</strong></td>
<td>0.6942</td>
<td>0.4516</td>
<td>0.5387</td>
<td>0.5983</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>62</strong></td>
<td>0.7586</td>
<td>0.7017</td>
<td>0.7120</td>
<td>0.7509</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>63</strong></td>
<td>0.6880</td>
<td>0.6004</td>
<td>0.6602</td>
<td>0.4320</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>64</strong></td>
<td>0.4742</td>
<td>0.5079</td>
<td>0.4135</td>
<td>0.4161</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>65</strong></td>
<td>0.4419</td>
<td>0.5761</td>
<td>0.4515</td>
<td>0.4497</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>66</strong></td>
<td>0.3367</td>
<td>0.4333</td>
<td>0.2336</td>
<td>0.1678</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>67</strong></td>
<td>0.4744</td>
<td>0.4604</td>
<td>0.1507</td>
<td>0.4873</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>68</strong></td>
<td>0.7510</td>
<td>0.4350</td>
<td>0.5453</td>
<td>0.4831</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>69</strong></td>
<td>0.4045</td>
<td>0.5636</td>
<td>0.2534</td>
<td>0.5573</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>70</strong></td>
<td>0.1449</td>
<td>0.1539</td>
<td>0.2446</td>
<td>0.0559</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
