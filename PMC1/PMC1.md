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

Para a confecção de um sistema de ressonância magnética, observou-se que
é de extrema importância para o bom desempenho do processador de imagens
que a variável {*y*} que mede a energia absorvida do sistema possa ser
estimada a partir da medição de três outras grandezas {*x*~1~ , *x*~2~ ,
*x*~3~}. Entretanto, em função da complexidade do sistema, sabe-se que
este mapeamento é de difícil obtenção por técnicas convencionais, sendo
que o modelo matemático disponível para representação do mesmo não
fornece resultados satisfatórios.

Assim, a equipe de engenheiros e cientistas pretende utilizar uma rede
perceptron multicamadas como um aproximador universal de funções, tendo
como objetivo final de que dado como entrada os valores de {*x*~1~ ,
*x*~2~ , *x*~3~} a mesma possa estimar (após o treinamento) o respectivo
valor da variável {*y*} que representa a energia absorvida. A topologia
da rede perceptron constituída de duas camadas neurais está ilustrada na
figura abaixo.

Utilizando o algoritmo de aprendizagem *backpropagation* (Regra Delta
Generalizada) e os dados de treinamento apresentados no Anexo, sendo que
as variáveis de entrada {*x*~1~ , *x*~2~ , *x*~3~} já estão todas
normalizadas, realize as seguintes atividades:

1.  Execute 5 treinamentos para a rede PERCEPTRON inicializando as
    > matrizes de pesos em cada treinamento com valores aleatórios entre
    > 0 e 1. Se for o caso, reinicie o gerador de números aleatórios em
    > cada treinamento de tal forma que os elementos das matrizes de
    > pesos iniciais não sejam os mesmos. Utilize a função de ativação
    > *logística* para todos os neurônios, taxa de aprendizado η = 0.1 e
    > precisão ε = 10^-6^.

  --------------- ----------------------------- --------------------------
  Treinamento     Erro Quadrático Médio         Número de Épocas

  1^o^ (T1)                                     

  2^o^ (T2)                                     

  3^o^ (T3)                                     

  4^o^ (T4)                                     

  5^o^ (T5)                                     
  --------------- ----------------------------- --------------------------

2.  Registre os resultados finais desses 5 treinamentos na tabela
    > abaixo:

3.  Para os dois treinamentos acima com maiores números de épocas, trace
    > os respectivos gráficos dos valores de erro quadrático médio (EQM)
    > em função de cada época de treinamento. Imprima os dois gráficos
    > numa mesma folha de modo não superpostos.

4.  Baseado na tabela do item 2, explique de forma detalhada por que
    > tanto o erro quadrático médio quanto o número de épocas variam de
    > treinamento para treinamento.

5.  Para todos os treinamentos efetuados no item 2, faça a validação da
    > rede aplicando o conjunto de teste fornecido na tabela abaixo.
    > Forneça para cada treinamento o erro relativo médio (%) entre os
    > valores desejados e os valores fornecidos pela rede em relação a
    > todos os padrões de teste. Obtenha também a respectiva variância.

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 3%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h1 id="amostra">Amostra</h1></td>
<td><em>x</em><sub>1</sub></td>
<td colspan="2"><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>d</em></td>
<td colspan="2"><p><em>y</em><sub>rede</sub></p>
<p>(T1)</p></td>
<td colspan="2"><p><em>y</em><sub>rede</sub></p>
<p>(T2)</p></td>
<td colspan="2"><p><em>y</em><sub>rede</sub></p>
<p>(T3)</p></td>
<td colspan="2"><p><em>y</em><sub>rede</sub></p>
<p>(T4)</p></td>
<td colspan="2"><p><em>y</em><sub>rede</sub></p>
<p>(T5)</p></td>
</tr>
<tr class="even">
<td>1</td>
<td>0.0611</td>
<td colspan="2">0.2860</td>
<td>0.7464</td>
<td>0.4831</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>2</td>
<td>0.5102</td>
<td colspan="2">0.7464</td>
<td>0.0860</td>
<td>0.5965</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>3</td>
<td>0.0004</td>
<td colspan="2">0.6916</td>
<td>0.5006</td>
<td>0.5318</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>4</td>
<td>0.9430</td>
<td colspan="2">0.4476</td>
<td>0.2648</td>
<td>0.6843</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>5</td>
<td>0.1399</td>
<td colspan="2">0.1610</td>
<td>0.2477</td>
<td>0.2872</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>6</td>
<td>0.6423</td>
<td colspan="2">0.3229</td>
<td>0.8567</td>
<td>0.7663</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>7</td>
<td>0.6492</td>
<td colspan="2">0.0007</td>
<td>0.6422</td>
<td>0.5666</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>8</td>
<td>0.1818</td>
<td colspan="2">0.5078</td>
<td>0.9046</td>
<td>0.6601</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>9</td>
<td>0.7382</td>
<td colspan="2">0.2647</td>
<td>0.1916</td>
<td>0.5427</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>10</td>
<td>0.3879</td>
<td colspan="2">0.1307</td>
<td>0.8656</td>
<td>0.5836</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>11</td>
<td>0.1903</td>
<td colspan="2">0.6523</td>
<td>0.7820</td>
<td>0.6950</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>12</td>
<td>0.8401</td>
<td colspan="2">0.4490</td>
<td>0.2719</td>
<td>0.6790</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>13</td>
<td>0.0029</td>
<td colspan="2">0.3264</td>
<td>0.2476</td>
<td>0.2956</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>14</td>
<td>0.7088</td>
<td colspan="2">0.9342</td>
<td>0.2763</td>
<td>0.7742</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>15</td>
<td>0.1283</td>
<td colspan="2">0.1882</td>
<td>0.7253</td>
<td>0.4662</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>16</td>
<td>0.8882</td>
<td colspan="2">0.3077</td>
<td>0.8931</td>
<td>0.8093</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>17</td>
<td>0.2225</td>
<td colspan="2">0.9182</td>
<td>0.7820</td>
<td>0.7581</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>18</td>
<td>0.1957</td>
<td colspan="2">0.8423</td>
<td>0.3085</td>
<td>0.5826</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>19</td>
<td>0.9991</td>
<td colspan="2">0.5914</td>
<td>0.3933</td>
<td>0.7938</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>20</td>
<td>0.2299</td>
<td colspan="2">0.1524</td>
<td>0.7353</td>
<td>0.5012</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="4">Erro Relativo Médio (%)</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4">Variância (%)</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

6.  Baseado nas análises da tabela acima indique qual das configurações
    finais de treinamento {T1, T2, T3, T4 ou T5} seria a mais adequada
    para o sistema de ressonância magnética, ou seja, qual delas está
    oferecendo a melhor generalização.

## ANEXO

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="amostra-1">Amostra</h4></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>d</em></td>
<td><h3 id="amostra-2">Amostra</h3></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>d</em></td>
<td><h3 id="amostra-3">Amostra</h3></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>d</em></td>
</tr>
<tr class="even">
<td><strong>1</strong></td>
<td>0.8799</td>
<td>0.7998</td>
<td>0.3972</td>
<td>0.8399</td>
<td><strong>71</strong></td>
<td>0.3644</td>
<td>0.2948</td>
<td>0.3937</td>
<td>0.5240</td>
<td><strong>141</strong></td>
<td>0.2858</td>
<td>0.9688</td>
<td>0.2262</td>
<td>0.5988</td>
</tr>
<tr class="odd">
<td><strong>2</strong></td>
<td>0.5700</td>
<td>0.5111</td>
<td>0.2418</td>
<td>0.6258</td>
<td><strong>72</strong></td>
<td>0.2014</td>
<td>0.6326</td>
<td>0.9782</td>
<td>0.7143</td>
<td><strong>142</strong></td>
<td>0.7931</td>
<td>0.8993</td>
<td>0.9028</td>
<td>0.9728</td>
</tr>
<tr class="even">
<td><strong>3</strong></td>
<td>0.6796</td>
<td>0.4117</td>
<td>0.3370</td>
<td>0.6622</td>
<td><strong>73</strong></td>
<td>0.4039</td>
<td>0.0645</td>
<td>0.4629</td>
<td>0.4547</td>
<td><strong>143</strong></td>
<td>0.7841</td>
<td>0.0778</td>
<td>0.9012</td>
<td>0.6832</td>
</tr>
<tr class="odd">
<td><strong>4</strong></td>
<td>0.3567</td>
<td>0.2967</td>
<td>0.6037</td>
<td>0.5969</td>
<td><strong>74</strong></td>
<td>0.7137</td>
<td>0.0670</td>
<td>0.2359</td>
<td>0.4602</td>
<td><strong>144</strong></td>
<td>0.1380</td>
<td>0.5881</td>
<td>0.2367</td>
<td>0.4622</td>
</tr>
<tr class="even">
<td><strong>5</strong></td>
<td>0.3866</td>
<td>0.8390</td>
<td>0.0232</td>
<td>0.5316</td>
<td><strong>75</strong></td>
<td>0.4277</td>
<td>0.9555</td>
<td>0.0000</td>
<td>0.5477</td>
<td><strong>145</strong></td>
<td>0.6345</td>
<td>0.5165</td>
<td>0.7139</td>
<td>0.8191</td>
</tr>
<tr class="odd">
<td><strong>6</strong></td>
<td>0.0271</td>
<td>0.7788</td>
<td>0.7445</td>
<td>0.6335</td>
<td><strong>76</strong></td>
<td>0.0259</td>
<td>0.7634</td>
<td>0.2889</td>
<td>0.4738</td>
<td><strong>146</strong></td>
<td>0.2453</td>
<td>0.5888</td>
<td>0.1559</td>
<td>0.4765</td>
</tr>
<tr class="even">
<td><strong>7</strong></td>
<td>0.8174</td>
<td>0.8422</td>
<td>0.3229</td>
<td>0.8068</td>
<td><strong>77</strong></td>
<td>0.1871</td>
<td>0.7682</td>
<td>0.9697</td>
<td>0.7397</td>
<td><strong>147</strong></td>
<td>0.1174</td>
<td>0.5436</td>
<td>0.3657</td>
<td>0.4953</td>
</tr>
<tr class="odd">
<td><strong>8</strong></td>
<td>0.6027</td>
<td>0.1468</td>
<td>0.3759</td>
<td>0.5342</td>
<td><strong>78</strong></td>
<td>0.3216</td>
<td>0.5420</td>
<td>0.0677</td>
<td>0.4526</td>
<td><strong>148</strong></td>
<td>0.3667</td>
<td>0.3228</td>
<td>0.6952</td>
<td>0.6376</td>
</tr>
<tr class="even">
<td><strong>9</strong></td>
<td>0.1203</td>
<td>0.3260</td>
<td>0.5419</td>
<td>0.4768</td>
<td><strong>79</strong></td>
<td>0.2524</td>
<td>0.7688</td>
<td>0.9523</td>
<td>0.7711</td>
<td><strong>149</strong></td>
<td>0.9532</td>
<td>0.6949</td>
<td>0.4451</td>
<td>0.8426</td>
</tr>
<tr class="odd">
<td><strong>10</strong></td>
<td>0.1325</td>
<td>0.2082</td>
<td>0.4934</td>
<td>0.4105</td>
<td><strong>80</strong></td>
<td>0.3621</td>
<td>0.5295</td>
<td>0.2521</td>
<td>0.5571</td>
<td><strong>150</strong></td>
<td>0.7954</td>
<td>0.8346</td>
<td>0.0449</td>
<td>0.6676</td>
</tr>
<tr class="even">
<td><strong>11</strong></td>
<td>0.6950</td>
<td>1.0000</td>
<td>0.4321</td>
<td>0.8404</td>
<td><strong>81</strong></td>
<td>0.2942</td>
<td>0.1625</td>
<td>0.2745</td>
<td>0.3759</td>
<td><strong>151</strong></td>
<td>0.1427</td>
<td>0.0480</td>
<td>0.6267</td>
<td>0.3780</td>
</tr>
<tr class="odd">
<td><strong>12</strong></td>
<td>0.0036</td>
<td>0.1940</td>
<td>0.3274</td>
<td>0.2697</td>
<td><strong>82</strong></td>
<td>0.8180</td>
<td>0.0023</td>
<td>0.1439</td>
<td>0.4018</td>
<td><strong>152</strong></td>
<td>0.1516</td>
<td>0.9824</td>
<td>0.0827</td>
<td>0.4627</td>
</tr>
<tr class="even">
<td><strong>13</strong></td>
<td>0.2650</td>
<td>0.0161</td>
<td>0.5947</td>
<td>0.4125</td>
<td><strong>83</strong></td>
<td>0.8429</td>
<td>0.1704</td>
<td>0.5251</td>
<td>0.6563</td>
<td><strong>153</strong></td>
<td>0.4868</td>
<td>0.6223</td>
<td>0.7462</td>
<td>0.8116</td>
</tr>
<tr class="odd">
<td><strong>14</strong></td>
<td>0.5849</td>
<td>0.6019</td>
<td>0.4376</td>
<td>0.7464</td>
<td><strong>84</strong></td>
<td>0.9612</td>
<td>0.6898</td>
<td>0.6630</td>
<td>0.9128</td>
<td><strong>154</strong></td>
<td>0.3408</td>
<td>0.5115</td>
<td>0.0783</td>
<td>0.4559</td>
</tr>
<tr class="even">
<td><strong>15</strong></td>
<td>0.0108</td>
<td>0.3538</td>
<td>0.1810</td>
<td>0.2800</td>
<td><strong>85</strong></td>
<td>0.1009</td>
<td>0.4190</td>
<td>0.0826</td>
<td>0.3055</td>
<td><strong>155</strong></td>
<td>0.8146</td>
<td>0.6378</td>
<td>0.5837</td>
<td>0.8628</td>
</tr>
<tr class="odd">
<td><strong>16</strong></td>
<td>0.9008</td>
<td>0.7264</td>
<td>0.9184</td>
<td>0.9602</td>
<td><strong>86</strong></td>
<td>0.7071</td>
<td>0.7704</td>
<td>0.8328</td>
<td>0.9298</td>
<td><strong>156</strong></td>
<td>0.2820</td>
<td>0.5409</td>
<td>0.7256</td>
<td>0.6939</td>
</tr>
<tr class="even">
<td><strong>17</strong></td>
<td>0.0023</td>
<td>0.9659</td>
<td>0.3182</td>
<td>0.4986</td>
<td><strong>87</strong></td>
<td>0.3371</td>
<td>0.7819</td>
<td>0.0959</td>
<td>0.5377</td>
<td><strong>157</strong></td>
<td>0.5716</td>
<td>0.2958</td>
<td>0.5477</td>
<td>0.6619</td>
</tr>
<tr class="odd">
<td><strong>18</strong></td>
<td>0.1366</td>
<td>0.6357</td>
<td>0.6967</td>
<td>0.6459</td>
<td><strong>88</strong></td>
<td>0.1555</td>
<td>0.5599</td>
<td>0.9221</td>
<td>0.6663</td>
<td><strong>158</strong></td>
<td>0.9323</td>
<td>0.0229</td>
<td>0.4797</td>
<td>0.5731</td>
</tr>
<tr class="even">
<td><strong>19</strong></td>
<td>0.8621</td>
<td>0.7353</td>
<td>0.2742</td>
<td>0.7718</td>
<td><strong>89</strong></td>
<td>0.7318</td>
<td>0.1877</td>
<td>0.3311</td>
<td>0.5689</td>
<td><strong>159</strong></td>
<td>0.2907</td>
<td>0.7245</td>
<td>0.5165</td>
<td>0.6911</td>
</tr>
<tr class="odd">
<td><strong>20</strong></td>
<td>0.0682</td>
<td>0.9624</td>
<td>0.4211</td>
<td>0.5764</td>
<td><strong>90</strong></td>
<td>0.1665</td>
<td>0.7449</td>
<td>0.0997</td>
<td>0.4508</td>
<td><strong>160</strong></td>
<td>0.0068</td>
<td>0.0545</td>
<td>0.0861</td>
<td>0.0851</td>
</tr>
<tr class="even">
<td><strong>21</strong></td>
<td>0.6112</td>
<td>0.6014</td>
<td>0.5254</td>
<td>0.7868</td>
<td><strong>91</strong></td>
<td>0.8762</td>
<td>0.2498</td>
<td>0.9167</td>
<td>0.7829</td>
<td><strong>161</strong></td>
<td>0.2636</td>
<td>0.9885</td>
<td>0.2175</td>
<td>0.5847</td>
</tr>
<tr class="odd">
<td><strong>22</strong></td>
<td>0.0030</td>
<td>0.7585</td>
<td>0.8928</td>
<td>0.6388</td>
<td><strong>92</strong></td>
<td>0.9885</td>
<td>0.6229</td>
<td>0.2085</td>
<td>0.7200</td>
<td><strong>162</strong></td>
<td>0.0350</td>
<td>0.3653</td>
<td>0.7801</td>
<td>0.5117</td>
</tr>
<tr class="even">
<td><strong>23</strong></td>
<td>0.7644</td>
<td>0.5964</td>
<td>0.0407</td>
<td>0.6055</td>
<td><strong>93</strong></td>
<td>0.0461</td>
<td>0.7745</td>
<td>0.5632</td>
<td>0.5949</td>
<td><strong>163</strong></td>
<td>0.9670</td>
<td>0.3031</td>
<td>0.7127</td>
<td>0.7836</td>
</tr>
<tr class="odd">
<td><strong>24</strong></td>
<td>0.6441</td>
<td>0.2097</td>
<td>0.5847</td>
<td>0.6545</td>
<td><strong>94</strong></td>
<td>0.3209</td>
<td>0.6229</td>
<td>0.5233</td>
<td>0.6810</td>
<td><strong>164</strong></td>
<td>0.0000</td>
<td>0.7763</td>
<td>0.8735</td>
<td>0.6388</td>
</tr>
<tr class="even">
<td><strong>25</strong></td>
<td>0.0803</td>
<td>0.3799</td>
<td>0.6020</td>
<td>0.4991</td>
<td><strong>95</strong></td>
<td>0.9189</td>
<td>0.5930</td>
<td>0.7288</td>
<td>0.8989</td>
<td><strong>165</strong></td>
<td>0.4395</td>
<td>0.0501</td>
<td>0.9761</td>
<td>0.5712</td>
</tr>
<tr class="odd">
<td><strong>26</strong></td>
<td>0.1908</td>
<td>0.8046</td>
<td>0.5402</td>
<td>0.6665</td>
<td><strong>96</strong></td>
<td>0.0382</td>
<td>0.5515</td>
<td>0.8818</td>
<td>0.5999</td>
<td><strong>166</strong></td>
<td>0.9359</td>
<td>0.0366</td>
<td>0.9514</td>
<td>0.6826</td>
</tr>
<tr class="even">
<td><strong>27</strong></td>
<td>0.6937</td>
<td>0.3967</td>
<td>0.6055</td>
<td>0.7595</td>
<td><strong>97</strong></td>
<td>0.3726</td>
<td>0.9988</td>
<td>0.3814</td>
<td>0.7086</td>
<td><strong>167</strong></td>
<td>0.0173</td>
<td>0.9548</td>
<td>0.4289</td>
<td>0.5527</td>
</tr>
<tr class="odd">
<td><strong>28</strong></td>
<td>0.2591</td>
<td>0.0582</td>
<td>0.3978</td>
<td>0.3604</td>
<td><strong>98</strong></td>
<td>0.4211</td>
<td>0.2668</td>
<td>0.3307</td>
<td>0.5080</td>
<td><strong>168</strong></td>
<td>0.6112</td>
<td>0.9070</td>
<td>0.6286</td>
<td>0.8803</td>
</tr>
<tr class="even">
<td><strong>29</strong></td>
<td>0.4241</td>
<td>0.1850</td>
<td>0.9066</td>
<td>0.6298</td>
<td><strong>99</strong></td>
<td>0.2378</td>
<td>0.0817</td>
<td>0.3574</td>
<td>0.3452</td>
<td><strong>169</strong></td>
<td>0.2010</td>
<td>0.9573</td>
<td>0.6791</td>
<td>0.7283</td>
</tr>
<tr class="odd">
<td><strong>30</strong></td>
<td>0.3332</td>
<td>0.9303</td>
<td>0.2475</td>
<td>0.6287</td>
<td><strong>100</strong></td>
<td>0.9893</td>
<td>0.7637</td>
<td>0.2526</td>
<td>0.7755</td>
<td><strong>170</strong></td>
<td>0.8914</td>
<td>0.9144</td>
<td>0.2641</td>
<td>0.7966</td>
</tr>
<tr class="even">
<td><strong>31</strong></td>
<td>0.3625</td>
<td>0.1592</td>
<td>0.9981</td>
<td>0.5948</td>
<td><strong>101</strong></td>
<td>0.8203</td>
<td>0.0682</td>
<td>0.4260</td>
<td>0.5643</td>
<td><strong>171</strong></td>
<td>0.0061</td>
<td>0.0802</td>
<td>0.8621</td>
<td>0.3711</td>
</tr>
<tr class="odd">
<td><strong>32</strong></td>
<td>0.9259</td>
<td>0.0960</td>
<td>0.1645</td>
<td>0.4716</td>
<td><strong>102</strong></td>
<td>0.6226</td>
<td>0.2146</td>
<td>0.1021</td>
<td>0.4452</td>
<td><strong>172</strong></td>
<td>0.2212</td>
<td>0.4664</td>
<td>0.3821</td>
<td>0.5260</td>
</tr>
<tr class="even">
<td><strong>33</strong></td>
<td>0.8606</td>
<td>0.6779</td>
<td>0.0033</td>
<td>0.6242</td>
<td><strong>103</strong></td>
<td>0.4589</td>
<td>0.3147</td>
<td>0.2236</td>
<td>0.4962</td>
<td><strong>173</strong></td>
<td>0.2401</td>
<td>0.6964</td>
<td>0.0751</td>
<td>0.4637</td>
</tr>
<tr class="odd">
<td><strong>34</strong></td>
<td>0.0838</td>
<td>0.5472</td>
<td>0.3758</td>
<td>0.4835</td>
<td><strong>104</strong></td>
<td>0.3471</td>
<td>0.8889</td>
<td>0.1564</td>
<td>0.5875</td>
<td><strong>174</strong></td>
<td>0.7881</td>
<td>0.9833</td>
<td>0.3038</td>
<td>0.8049</td>
</tr>
<tr class="even">
<td><strong>35</strong></td>
<td>0.0303</td>
<td>0.9191</td>
<td>0.7233</td>
<td>0.6491</td>
<td><strong>105</strong></td>
<td>0.5762</td>
<td>0.8292</td>
<td>0.4116</td>
<td>0.7853</td>
<td><strong>175</strong></td>
<td>0.2435</td>
<td>0.0794</td>
<td>0.5551</td>
<td>0.4223</td>
</tr>
<tr class="odd">
<td><strong>36</strong></td>
<td>0.9293</td>
<td>0.8319</td>
<td>0.9664</td>
<td>0.9840</td>
<td><strong>106</strong></td>
<td>0.9053</td>
<td>0.6245</td>
<td>0.5264</td>
<td>0.8506</td>
<td><strong>176</strong></td>
<td>0.2752</td>
<td>0.8414</td>
<td>0.2797</td>
<td>0.6079</td>
</tr>
<tr class="even">
<td><strong>37</strong></td>
<td>0.7268</td>
<td>0.1440</td>
<td>0.9753</td>
<td>0.7096</td>
<td><strong>107</strong></td>
<td>0.2860</td>
<td>0.0793</td>
<td>0.0549</td>
<td>0.2224</td>
<td><strong>177</strong></td>
<td>0.7616</td>
<td>0.4698</td>
<td>0.5337</td>
<td>0.7809</td>
</tr>
<tr class="odd">
<td><strong>38</strong></td>
<td>0.2888</td>
<td>0.6593</td>
<td>0.4078</td>
<td>0.6328</td>
<td><strong>108</strong></td>
<td>0.9567</td>
<td>0.3034</td>
<td>0.4425</td>
<td>0.6993</td>
<td><strong>178</strong></td>
<td>0.3395</td>
<td>0.0022</td>
<td>0.0087</td>
<td>0.1836</td>
</tr>
<tr class="even">
<td><strong>39</strong></td>
<td>0.5515</td>
<td>0.1364</td>
<td>0.2894</td>
<td>0.4745</td>
<td><strong>109</strong></td>
<td>0.5170</td>
<td>0.9266</td>
<td>0.1565</td>
<td>0.6594</td>
<td><strong>179</strong></td>
<td>0.7849</td>
<td>0.9981</td>
<td>0.4449</td>
<td>0.8641</td>
</tr>
<tr class="odd">
<td><strong>40</strong></td>
<td>0.7683</td>
<td>0.0067</td>
<td>0.5546</td>
<td>0.5708</td>
<td><strong>110</strong></td>
<td>0.8149</td>
<td>0.0396</td>
<td>0.6227</td>
<td>0.6165</td>
<td><strong>180</strong></td>
<td>0.8312</td>
<td>0.0961</td>
<td>0.2129</td>
<td>0.4857</td>
</tr>
<tr class="even">
<td><strong>41</strong></td>
<td>0.6462</td>
<td>0.6761</td>
<td>0.8340</td>
<td>0.8933</td>
<td><strong>111</strong></td>
<td>0.3710</td>
<td>0.3554</td>
<td>0.5633</td>
<td>0.6171</td>
<td><strong>181</strong></td>
<td>0.9763</td>
<td>0.1102</td>
<td>0.6227</td>
<td>0.6667</td>
</tr>
<tr class="odd">
<td><strong>42</strong></td>
<td>0.3694</td>
<td>0.2212</td>
<td>0.1233</td>
<td>0.3658</td>
<td><strong>112</strong></td>
<td>0.8702</td>
<td>0.3185</td>
<td>0.2762</td>
<td>0.6287</td>
<td><strong>182</strong></td>
<td>0.8597</td>
<td>0.3284</td>
<td>0.6932</td>
<td>0.7829</td>
</tr>
<tr class="even">
<td><strong>43</strong></td>
<td>0.2706</td>
<td>0.3222</td>
<td>0.9996</td>
<td>0.6310</td>
<td><strong>113</strong></td>
<td>0.1016</td>
<td>0.6382</td>
<td>0.3173</td>
<td>0.4957</td>
<td><strong>183</strong></td>
<td>0.9295</td>
<td>0.3275</td>
<td>0.7536</td>
<td>0.8016</td>
</tr>
<tr class="odd">
<td><strong>44</strong></td>
<td>0.6282</td>
<td>0.1404</td>
<td>0.8474</td>
<td>0.6733</td>
<td><strong>114</strong></td>
<td>0.3890</td>
<td>0.2369</td>
<td>0.0083</td>
<td>0.3235</td>
<td><strong>184</strong></td>
<td>0.2435</td>
<td>0.2163</td>
<td>0.7625</td>
<td>0.5449</td>
</tr>
<tr class="even">
<td><strong>45</strong></td>
<td>0.5861</td>
<td>0.6693</td>
<td>0.3818</td>
<td>0.7433</td>
<td><strong>115</strong></td>
<td>0.2702</td>
<td>0.8617</td>
<td>0.1218</td>
<td>0.5319</td>
<td><strong>185</strong></td>
<td>0.9281</td>
<td>0.8356</td>
<td>0.5285</td>
<td>0.8991</td>
</tr>
<tr class="odd">
<td><strong>46</strong></td>
<td>0.6057</td>
<td>0.9901</td>
<td>0.5141</td>
<td>0.8466</td>
<td><strong>116</strong></td>
<td>0.7473</td>
<td>0.6507</td>
<td>0.5582</td>
<td>0.8464</td>
<td><strong>186</strong></td>
<td>0.8313</td>
<td>0.7566</td>
<td>0.6192</td>
<td>0.9047</td>
</tr>
<tr class="even">
<td><strong>47</strong></td>
<td>0.5915</td>
<td>0.5588</td>
<td>0.3055</td>
<td>0.6787</td>
<td><strong>117</strong></td>
<td>0.9108</td>
<td>0.2139</td>
<td>0.4641</td>
<td>0.6625</td>
<td><strong>187</strong></td>
<td>0.1712</td>
<td>0.0545</td>
<td>0.5033</td>
<td>0.3561</td>
</tr>
<tr class="odd">
<td><strong>48</strong></td>
<td>0.8359</td>
<td>0.4145</td>
<td>0.5016</td>
<td>0.7597</td>
<td><strong>118</strong></td>
<td>0.4343</td>
<td>0.6028</td>
<td>0.1344</td>
<td>0.5546</td>
<td><strong>188</strong></td>
<td>0.0609</td>
<td>0.1702</td>
<td>0.4306</td>
<td>0.3310</td>
</tr>
<tr class="even">
<td><strong>49</strong></td>
<td>0.5497</td>
<td>0.6319</td>
<td>0.8382</td>
<td>0.8521</td>
<td><strong>119</strong></td>
<td>0.6847</td>
<td>0.4062</td>
<td>0.9318</td>
<td>0.8204</td>
<td><strong>189</strong></td>
<td>0.5899</td>
<td>0.9408</td>
<td>0.0369</td>
<td>0.6245</td>
</tr>
<tr class="odd">
<td><strong>50</strong></td>
<td>0.7072</td>
<td>0.1721</td>
<td>0.3812</td>
<td>0.5772</td>
<td><strong>120</strong></td>
<td>0.8657</td>
<td>0.9448</td>
<td>0.9900</td>
<td>0.9904</td>
<td><strong>190</strong></td>
<td>0.7858</td>
<td>0.5115</td>
<td>0.0916</td>
<td>0.6066</td>
</tr>
<tr class="even">
<td><strong>51</strong></td>
<td>0.1185</td>
<td>0.5084</td>
<td>0.8376</td>
<td>0.6211</td>
<td><strong>121</strong></td>
<td>0.4011</td>
<td>0.4138</td>
<td>0.8715</td>
<td>0.7222</td>
<td><strong>191</strong></td>
<td>1.0000</td>
<td>0.1653</td>
<td>0.7103</td>
<td>0.7172</td>
</tr>
<tr class="odd">
<td><strong>52</strong></td>
<td>0.6365</td>
<td>0.5562</td>
<td>0.4965</td>
<td>0.7693</td>
<td><strong>122</strong></td>
<td>0.5949</td>
<td>0.2600</td>
<td>0.0810</td>
<td>0.4480</td>
<td><strong>192</strong></td>
<td>0.2007</td>
<td>0.1163</td>
<td>0.3431</td>
<td>0.3385</td>
</tr>
<tr class="even">
<td><strong>53</strong></td>
<td>0.4145</td>
<td>0.5797</td>
<td>0.8599</td>
<td>0.7878</td>
<td><strong>123</strong></td>
<td>0.1845</td>
<td>0.7906</td>
<td>0.9725</td>
<td>0.7425</td>
<td><strong>193</strong></td>
<td>0.2306</td>
<td>0.0330</td>
<td>0.0293</td>
<td>0.1590</td>
</tr>
<tr class="odd">
<td><strong>54</strong></td>
<td>0.2575</td>
<td>0.5358</td>
<td>0.4028</td>
<td>0.5777</td>
<td><strong>124</strong></td>
<td>0.3438</td>
<td>0.6725</td>
<td>0.9821</td>
<td>0.7926</td>
<td><strong>194</strong></td>
<td>0.8477</td>
<td>0.6378</td>
<td>0.4623</td>
<td>0.8254</td>
</tr>
<tr class="even">
<td><strong>55</strong></td>
<td>0.2026</td>
<td>0.3300</td>
<td>0.3054</td>
<td>0.4261</td>
<td><strong>125</strong></td>
<td>0.8398</td>
<td>0.1360</td>
<td>0.9119</td>
<td>0.7222</td>
<td><strong>195</strong></td>
<td>0.9677</td>
<td>0.7895</td>
<td>0.9467</td>
<td>0.9782</td>
</tr>
<tr class="odd">
<td><strong>56</strong></td>
<td>0.3385</td>
<td>0.0476</td>
<td>0.5941</td>
<td>0.4625</td>
<td><strong>126</strong></td>
<td>0.2245</td>
<td>0.0971</td>
<td>0.6136</td>
<td>0.4402</td>
<td><strong>196</strong></td>
<td>0.0339</td>
<td>0.4669</td>
<td>0.1526</td>
<td>0.3250</td>
</tr>
<tr class="even">
<td><strong>57</strong></td>
<td>0.4094</td>
<td>0.1726</td>
<td>0.7803</td>
<td>0.6015</td>
<td><strong>127</strong></td>
<td>0.3742</td>
<td>0.9668</td>
<td>0.8194</td>
<td>0.8371</td>
<td><strong>197</strong></td>
<td>0.0080</td>
<td>0.8988</td>
<td>0.4201</td>
<td>0.5404</td>
</tr>
<tr class="odd">
<td><strong>58</strong></td>
<td>0.1261</td>
<td>0.6181</td>
<td>0.4927</td>
<td>0.5739</td>
<td><strong>128</strong></td>
<td>0.9572</td>
<td>0.9836</td>
<td>0.3793</td>
<td>0.8556</td>
<td><strong>198</strong></td>
<td>0.9955</td>
<td>0.8897</td>
<td>0.6175</td>
<td>0.9360</td>
</tr>
<tr class="even">
<td><strong>59</strong></td>
<td>0.1224</td>
<td>0.4662</td>
<td>0.2146</td>
<td>0.4007</td>
<td><strong>129</strong></td>
<td>0.7496</td>
<td>0.0410</td>
<td>0.1360</td>
<td>0.4059</td>
<td><strong>199</strong></td>
<td>0.7408</td>
<td>0.5351</td>
<td>0.2732</td>
<td>0.6949</td>
</tr>
<tr class="odd">
<td><strong>60</strong></td>
<td>0.6793</td>
<td>0.6774</td>
<td>1.0000</td>
<td>0.9141</td>
<td><strong>130</strong></td>
<td>0.9123</td>
<td>0.3510</td>
<td>0.0682</td>
<td>0.5455</td>
<td><strong>200</strong></td>
<td>0.6843</td>
<td>0.3737</td>
<td>0.1562</td>
<td>0.5625</td>
</tr>
<tr class="even">
<td><strong>61</strong></td>
<td>0.8176</td>
<td>0.0358</td>
<td>0.2506</td>
<td>0.4707</td>
<td><strong>131</strong></td>
<td>0.6954</td>
<td>0.5500</td>
<td>0.6801</td>
<td>0.8388</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>62</strong></td>
<td>0.6937</td>
<td>0.6685</td>
<td>0.5075</td>
<td>0.8220</td>
<td><strong>132</strong></td>
<td>0.5252</td>
<td>0.6529</td>
<td>0.5729</td>
<td>0.7893</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>63</strong></td>
<td>0.2404</td>
<td>0.5411</td>
<td>0.8754</td>
<td>0.6980</td>
<td><strong>133</strong></td>
<td>0.3156</td>
<td>0.3851</td>
<td>0.5983</td>
<td>0.6161</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>64</strong></td>
<td>0.6553</td>
<td>0.2609</td>
<td>0.1188</td>
<td>0.4851</td>
<td><strong>134</strong></td>
<td>0.1460</td>
<td>0.1637</td>
<td>0.0249</td>
<td>0.1813</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>65</strong></td>
<td>0.8886</td>
<td>0.0288</td>
<td>0.2604</td>
<td>0.4802</td>
<td><strong>135</strong></td>
<td>0.7780</td>
<td>0.4491</td>
<td>0.4614</td>
<td>0.7498</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>66</strong></td>
<td>0.3974</td>
<td>0.5275</td>
<td>0.6457</td>
<td>0.7215</td>
<td><strong>136</strong></td>
<td>0.5959</td>
<td>0.8647</td>
<td>0.8601</td>
<td>0.9176</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>67</strong></td>
<td>0.2108</td>
<td>0.4910</td>
<td>0.5432</td>
<td>0.5913</td>
<td><strong>137</strong></td>
<td>0.2204</td>
<td>0.1785</td>
<td>0.4607</td>
<td>0.4276</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>68</strong></td>
<td>0.8675</td>
<td>0.5571</td>
<td>0.1849</td>
<td>0.6805</td>
<td><strong>138</strong></td>
<td>0.7355</td>
<td>0.8264</td>
<td>0.7015</td>
<td>0.9214</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>69</strong></td>
<td>0.5693</td>
<td>0.0242</td>
<td>0.9293</td>
<td>0.6033</td>
<td><strong>139</strong></td>
<td>0.9931</td>
<td>0.6727</td>
<td>0.3139</td>
<td>0.7829</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>70</strong></td>
<td>0.8439</td>
<td>0.4631</td>
<td>0.6345</td>
<td>0.8226</td>
<td><strong>140</strong></td>
<td>0.9123</td>
<td>0.0000</td>
<td>0.1106</td>
<td>0.3944</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
