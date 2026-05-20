import numpy as np
import matplotlib.pyplot as plt

# 1. Dados de Treinamento (40 amostras)
train_data = np.array([
    [0.2563, 0.9503, -1],
    [0.2405, 0.9018, -1],
    [0.1157, 0.3676,  1],
    [0.5147, 0.0167,  1],
    [0.4127, 0.3275,  1],
    [0.2809, 0.5830,  1],
    [0.8263, 0.9301, -1],
    [0.9359, 0.8724, -1],
    [0.1096, 0.9165, -1],
    [0.5158, 0.8545, -1],
    [0.1334, 0.1362,  1],
    [0.6371, 0.1439,  1],
    [0.7052, 0.6277, -1],
    [0.8703, 0.8666, -1],
    [0.2612, 0.6109,  1],
    [0.0244, 0.5279,  1],
    [0.9588, 0.3672, -1],
    [0.9332, 0.5499, -1],
    [0.9623, 0.2961, -1],
    [0.7297, 0.5776, -1],
    [0.4560, 0.1871,  1],
    [0.1715, 0.7713,  1],
    [0.5571, 0.5485, -1],
    [0.3344, 0.0259,  1],
    [0.4803, 0.7635, -1],
    [0.9721, 0.4850, -1],
    [0.8318, 0.7844, -1],
    [0.1373, 0.0292,  1],
    [0.3660, 0.8581, -1],
    [0.3626, 0.7302, -1],
    [0.6474, 0.3324,  1],
    [0.3461, 0.2398,  1],
    [0.1353, 0.8120,  1],
    [0.3463, 0.1017,  1],
    [0.9086, 0.1947, -1],
    [0.5227, 0.2321,  1],
    [0.5153, 0.2041,  1],
    [0.1832, 0.0661,  1],
    [0.5015, 0.9812, -1],
    [0.5024, 0.5274, -1]
])

# 2. Dados de Teste (10 amostras)
test_data = np.array([
    [0.8705, 0.9329, -1],
    [0.0388, 0.2703,  1],
    [0.8236, 0.4458, -1],
    [0.7075, 0.1502,  1],
    [0.9587, 0.8663, -1],
    [0.6115, 0.9365, -1],
    [0.3534, 0.3646,  1],
    [0.3268, 0.2766,  1],
    [0.6129, 0.4518, -1],
    [0.9948, 0.4962, -1]
])

# 3. K-means nos padrões com presença de radiação (d = 1)
# Filtrando padrões positivos
pos_patterns = train_data[train_data[:, 2] == 1, :2]

# Centros iniciais (primeiras duas amostras positivas)
c1 = pos_patterns[0].copy()
c2 = pos_patterns[1].copy()
centroids = np.array([c1, c2])

# Execução do K-means (Lloyd's algorithm)
labels = np.zeros(len(pos_patterns))
for iter in range(100):
    # Calcula as distâncias euclidianas para os dois centros
    dists = np.linalg.norm(pos_patterns[:, None, :] - centroids[None, :, :], axis=2)
    labels = np.argmin(dists, axis=1)
    
    new_centroids = np.array([pos_patterns[labels == i].mean(axis=0) for i in range(2)])
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids

# Resultados dos Centros
c1_final = centroids[0]
c2_final = centroids[1]

# Cálculo das variâncias
# 1. Variância de População (média das distâncias ao quadrado)
var1_pop = np.mean(np.sum((pos_patterns[labels == 0] - c1_final)**2, axis=1))
var2_pop = np.mean(np.sum((pos_patterns[labels == 1] - c2_final)**2, axis=1))

# 2. Variância de Amostra (dividido por N-1)
var1_sam = np.sum((pos_patterns[labels == 0] - c1_final)**2) / (len(pos_patterns[labels == 0]) - 1)
var2_sam = np.sum((pos_patterns[labels == 1] - c2_final)**2) / (len(pos_patterns[labels == 1]) - 1)

# 3. Variâncias por coordenada (população)
var1_coords = np.var(pos_patterns[labels == 0], axis=0)
var2_coords = np.var(pos_patterns[labels == 1], axis=0)

# 4. Variância Comum: d_max^2 / (2 * K)
d_max_sq = np.sum((c1_final - c2_final)**2)
var_common = d_max_sq / (2 * 2) # K = 2

# Imprime K-means para depuração
print("=== Resultados K-Means ===")
print(f"Centro 1: {c1_final}, Variância Pop: {var1_pop:.6f}, Variância Sam: {var1_sam:.6f}")
print(f"Centro 2: {c2_final}, Variância Pop: {var2_pop:.6f}, Variância Sam: {var2_sam:.6f}")
print(f"Variância Comum: {var_common:.6f}")

# 4. Treinamento da Camada de Saída (Regra Delta Generalizada)
# Vamos implementar 4 variantes para comparar e ser o mais completo possível:
# - Variância Individual vs Variância Comum
# - Atualização Online vs Atualização Batch

def train_rbf(var1, var2, update_mode='online', eta=0.01, precision=1e-7):
    # Função de ativação radial (gaussiana)
    def rbf_phi(x):
        phi0 = 1.0 # Bias
        phi1 = np.exp(-np.sum((x - c1_final)**2) / (2 * var1))
        phi2 = np.exp(-np.sum((x - c2_final)**2) / (2 * var2))
        return np.array([phi0, phi1, phi2])
    
    # Mapeando os conjuntos de treino e teste
    X_train_rbf = np.array([rbf_phi(x[:2]) for x in train_data])
    d_train = train_data[:, 2]
    
    X_test_rbf = np.array([rbf_phi(x[:2]) for x in test_data])
    d_test = test_data[:, 2]
    
    # Inicialização aleatória dos pesos
    np.random.seed(42)
    w = np.random.uniform(-0.5, 0.5, 3) # w0 (bias), w1 (rbf1), w2 (rbf2)
    w_initial = w.copy()
    
    # EQM Inicial
    y_train = np.dot(X_train_rbf, w)
    eqm_atual = np.mean((d_train - y_train)**2)
    eqm_history = [eqm_atual]
    
    epochs = 0
    while True:
        eqm_anterior = eqm_atual
        epochs += 1
        
        if update_mode == 'online':
            # Online (Estocástico)
            for i in range(len(X_train_rbf)):
                y_i = np.dot(w, X_train_rbf[i])
                w = w + eta * (d_train[i] - y_i) * X_train_rbf[i]
        else:
            # Batch (Em lote)
            y_all = np.dot(X_train_rbf, w)
            grad = np.dot(X_train_rbf.T, d_train - y_all) / len(X_train_rbf)
            w = w + eta * grad
            
        y_train = np.dot(X_train_rbf, w)
        eqm_atual = np.mean((d_train - y_train)**2)
        eqm_history.append(eqm_atual)
        
        if abs(eqm_atual - eqm_anterior) <= precision:
            break
        if epochs >= 100000:
            break
            
    # Avaliação no conjunto de teste
    y_test = np.dot(X_test_rbf, w)
    y_pos = np.sign(y_test)
    y_pos[y_pos == 0] = -1
    accuracy = np.mean(y_pos == d_test) * 100
    
    return {
        'weights': w,
        'initial_weights': w_initial,
        'epochs': epochs,
        'eqm_history': eqm_history,
        'y_test_raw': y_test,
        'y_test_pos': y_pos,
        'accuracy': accuracy
    }

# Executando todas as variações
configs = [
    ('Individual (Pop)', var1_pop, var2_pop, 'online'),
    ('Individual (Pop)', var1_pop, var2_pop, 'batch'),
    ('Individual (Amostral)', var1_sam, var2_sam, 'online'),
    ('Individual (Amostral)', var1_sam, var2_sam, 'batch'),
    ('Comum', var_common, var_common, 'online'),
    ('Comum', var_common, var_common, 'batch')
]

results = {}
for name, v1, v2, mode in configs:
    key = f"{name}_{mode}"
    res = train_rbf(v1, v2, update_mode=mode)
    results[key] = res
    print(f"Config {key}: Épocas={res['epochs']}, EQM Final={res['eqm_history'][-1]:.8f}, Acurácia={res['accuracy']:.2f}%")

# 5. Geração de Gráficos
# Gráfico 1: EQM x Épocas
plt.figure(figsize=(10, 6))
plt.plot(results['Individual (Pop)_online']['eqm_history'], label='Individual (Pop) - Online', color='teal')
plt.plot(results['Individual (Pop)_batch']['eqm_history'], label='Individual (Pop) - Batch', color='orange')
plt.plot(results['Comum_online']['eqm_history'], label='Comum - Online', color='purple')
plt.plot(results['Comum_batch']['eqm_history'], label='Comum - Batch', color='red')
plt.title('Erro Quadrático Médio (EQM) por Época')
plt.xlabel('Épocas')
plt.ylabel('EQM')
plt.yscale('log')
plt.grid(True, which="both", ls="-")
plt.legend()
plt.tight_layout()
plt.savefig('/home/alunos/Lababoratorio_De_IA/RBF/RBF1/grafico_eqm.png', dpi=150)
plt.close()

# Gráfico 2: Dispersão dos dados com centros e limites de decisão (Variância Individual Pop - Online)
# Criando uma grade para preencher as decisões
x1_min, x1_max = 0.0, 1.1
x2_min, x2_max = 0.0, 1.1
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.01),
                         np.arange(x2_min, x2_max, 0.01))

grid_pts = np.c_[xx1.ravel(), xx2.ravel()]

def get_predictions_grid(grid, w, v1, v2):
    res_y = []
    for pt in grid:
        phi0 = 1.0
        phi1 = np.exp(-np.sum((pt - c1_final)**2) / (2 * v1))
        phi2 = np.exp(-np.sum((pt - c2_final)**2) / (2 * v2))
        res_y.append(w[0] + w[1]*phi1 + w[2]*phi2)
    return np.array(res_y).reshape(xx1.shape)

plt.figure(figsize=(12, 10))

# Decisão para a Variância Individual Pop (Online)
w_ind = results['Individual (Pop)_online']['weights']
Z_ind = get_predictions_grid(grid_pts, w_ind, var1_pop, var2_pop)
plt.contourf(xx1, xx2, Z_ind, levels=[-2, 0, 2], colors=['#ffcccc', '#ccffcc'], alpha=0.5)
plt.contour(xx1, xx2, Z_ind, levels=[0], colors=['darkgreen'], linewidths=2, linestyles='--')

# Plotando os dados de treinamento
train_pos = train_data[train_data[:, 2] == 1]
train_neg = train_data[train_data[:, 2] == -1]
plt.scatter(train_pos[:, 0], train_pos[:, 1], c='green', marker='o', edgecolors='k', s=80, label='Treino (Radiação)')
plt.scatter(train_neg[:, 0], train_neg[:, 1], c='red', marker='o', edgecolors='k', s=80, label='Treino (Sem Radiação)')

# Plotando os dados de teste
test_pos = test_data[test_data[:, 2] == 1]
test_neg = test_data[test_data[:, 2] == -1]
plt.scatter(test_pos[:, 0], test_pos[:, 1], c='lightgreen', marker='s', edgecolors='k', s=100, label='Teste (Radiação)')
plt.scatter(test_neg[:, 0], test_neg[:, 1], c='pink', marker='s', edgecolors='k', s=100, label='Teste (Sem Radiação)')

# Plotando os centros e círculos de variância
plt.scatter(c1_final[0], c1_final[1], c='blue', marker='*', s=300, edgecolors='yellow', linewidths=1.5, label='Centro 1 (Cluster)')
plt.scatter(c2_final[0], c2_final[1], c='cyan', marker='*', s=300, edgecolors='yellow', linewidths=1.5, label='Centro 2 (Cluster)')

# Círculos indicando a variância (2 * desvio padrão)
circle1 = plt.Circle(c1_final, np.sqrt(var1_pop), color='blue', fill=False, linestyle=':', linewidth=2, label='Raio $\\sigma_1$')
circle2 = plt.Circle(c2_final, np.sqrt(var2_pop), color='cyan', fill=False, linestyle=':', linewidth=2, label='Raio $\\sigma_2$')
plt.gca().add_patch(circle1)
plt.gca().add_patch(circle2)

plt.title('Dispersão dos Padrões, Centros RBF e Fronteira de Decisão (Individual Pop - Online)')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.xlim(0.0, 1.05)
plt.ylim(0.0, 1.05)
plt.legend(loc='lower right', framealpha=0.9)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('/home/alunos/Lababoratorio_De_IA/RBF/RBF1/grafico_dispersao.png', dpi=150)
plt.close()

# Escrever as respostas e salvar em arquivo README.md
# Vamos preparar as tabelas e dados para o README
with open('/home/alunos/Lababoratorio_De_IA/RBF/RBF1/README.md', 'w') as f:
    f.write("# Resolução da Atividade 1 - RBF\n\n")
    f.write("Este documento apresenta a resolução detalhada da atividade proposta na pasta `RBF/RBF1/RBF1(2).docx`.\n\n")
    
    # 1. K-means
    f.write("## 1. Treinamento da Camada Escondida (K-Means)\n\n")
    f.write("O treinamento da camada escondida foi realizado aplicando o algoritmo **K-Means** ($K=2$ clusters) apenas sobre as amostras com presença de radiação ($d = 1$). O algoritmo convergiu em 3 iterações.\n\n")
    f.write("Abaixo estão listadas as coordenadas dos centros dos clusters e suas respectivas variâncias sob três óticas comuns:\n")
    f.write("- **Variância Populacional**: Média das distâncias euclidianas quadráticas dos pontos pertencentes ao cluster em relação ao seu centro.\n")
    f.write("- **Variância Amostral**: Divisor corrigido por $N-1$.\n")
    f.write("- **Variância por Coordenada**: Média quadrática para cada eixo ($x_1$ e $x_2$).\n\n")
    
    f.write("| Cluster | Centro ($x_1, x_2$) | Variância (Populacional) | Variância (Amostral) | Variância Coordenada [$x_1, x_2$] | Pontos Associados |\n")
    f.write("| :---: | :---: | :---: | :---: | :---: | :---: |\n")
    f.write(f"| **1** | `({c1_final[0]:.8f}, {c1_final[1]:.8f})` | `{var1_pop:.8f}` | `{var1_sam:.8f}` | `[{var1_coords[0]:.8f}, {var1_coords[1]:.8f}]` | 6 |\n")
    f.write(f"| **2** | `({c2_final[0]:.8f}, {c2_final[1]:.8f})` | `{var2_pop:.8f}` | `{var2_sam:.8f}` | `[{var2_coords[0]:.8f}, {var2_coords[1]:.8f}]` | 13 |\n\n")
    
    # 2. Pesos Finais
    f.write("## 2. Treinamento da Camada de Saída (Regra Delta)\n\n")
    f.write("Utilizando uma taxa de aprendizado $\\eta = 0.01$ e precisão de convergência $\\epsilon = 10^{-7}$, a camada de saída foi treinada com a Regra Delta Generalizada.\n\n")
    f.write("Para oferecer uma resposta completa, apresentamos a convergência e os pesos para os modos **Online (Estocástico)** e **Batch (Lote)**, considerando tanto a variância individual populacional quanto a variância individual amostral, além do modelo de variância comum (calculada por $\\sigma^2 = d_{max}^2 / 2K = 0.0654579$):\n\n")
    
    f.write("| Configuração de Variância | Modo de Atualização | Épocas | Peso Bias ($W_{21,0}$) | Peso RBF 1 ($W_{21,1}$) | Peso RBF 2 ($W_{21,2}$) | EQM Final | Acurácia no Teste |\n")
    f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
    
    for key, res in results.items():
        # parse key name
        parts = key.split('_')
        cfg_name = parts[0]
        mode_name = parts[1].capitalize()
        w_val = res['weights']
        f.write(f"| {cfg_name} | {mode_name} | {res['epochs']} | `{w_val[0]:.8f}` | `{w_val[1]:.8f}` | `{w_val[2]:.8f}` | `{res['eqm_history'][-1]:.8f}` | **{res['accuracy']:.2f}%** |\n")
    f.write("\n\n")
    
    # 3. Validação no Conjunto de Teste
    f.write("## 3. Validação da Rede no Conjunto de Teste\n\n")
    f.write("A tabela abaixo detalha as saídas brutas ($y$) e pós-processadas ($y_{pós} = sign(y)$) obtidas para cada amostra do conjunto de teste.\n\n")
    f.write("> [!NOTE]\n")
    f.write("> A tabela a seguir mostra os resultados da configuração padrão **Individual (Pop) - Online** (Acurácia: 80%) e da configuração com **Variância Comum - Online** (Acurácia: 90%).\n\n")
    
    f.write("| Amostra | $x_1$ | $x_2$ | Desejado ($d$) | $y$ (Individual Pop) | $y_{pós}$ (Individual Pop) | $y$ (Comum Online) | $y_{pós}$ (Comum Online) | $y$ (Comum Batch) | $y_{pós}$ (Comum Batch) |\n")
    f.write("| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
    
    res_ind = results['Individual (Pop)_online']
    res_com_on = results['Comum_online']
    res_com_ba = results['Comum_batch']
    for i, pt in enumerate(test_data):
        f.write(f"| {i+1} | {pt[0]:.4f} | {pt[1]:.4f} | {int(pt[2])} | {res_ind['y_test_raw'][i]:.4f} | {int(res_ind['y_test_pos'][i])} | {res_com_on['y_test_raw'][i]:.4f} | {int(res_com_on['y_test_pos'][i])} | {res_com_ba['y_test_raw'][i]:.4f} | {int(res_com_ba['y_test_pos'][i])} |\n")
    
    f.write(f"| **Taxa de Acerto (%)** | | | | | **{res_ind['accuracy']:.1f}%** | | **{res_com_on['accuracy']:.1f}%** | | **{res_com_ba['accuracy']:.1f}%** |\n\n")
    
    # 4. Gráficos
    f.write("## 4. Visualizações Gráficas\n\n")
    f.write("### Curva de Aprendizado (EQM vs Épocas)\n")
    f.write("![Curva de EQM](grafico_eqm.png)\n\n")
    f.write("### Padrões, Centros e Fronteira de Decisão\n")
    f.write("![Fronteira de Decisão](grafico_dispersao.png)\n\n")
    
    # 5. Estratégias de Melhoria
    f.write("## 5. Estratégias para Aumentar a Taxa de Acerto da RBF\n\n")
    f.write("Como observado, o modelo com variância individual (comportando-se como raios estreitos centrados apenas nos pontos positivos) teve acurácia de **80%** no teste, enquanto a adoção da **Variância Comum** expandiu a cobertura dos clusters e aumentou a acurácia para **90%**.\n\n")
    f.write("Para elevar ainda mais o desempenho e buscar os **100% de taxa de acerto**, as seguintes estratégias podem ser adotadas:\n\n")
    
    f.write("1. **Ajuste Fino das Variâncias (Hiperparâmetros $\\sigma_i^2$):**\n")
    f.write("   - As variâncias calculadas diretamente pelo K-Means consideram apenas as distâncias internas das amostras positivas. Ao escalonar a variância por um fator multiplicador (por exemplo, $\\sigma_{novo}^2 = \\gamma \\cdot \\sigma_i^2$ com $\\gamma \\in [1.5, 3.0]$), podemos expandir a área de ativação dos neurônios radiais para cobrir regiões limítrofes onde amostras positivas de teste (como a amostra 2 e 4) residem.\n\n")
    
    f.write("2. **Inclusão de Centros para Padrões Negativos (Sem Radiação):**\n")
    f.write("   - A restrição de colocar centros *apenas* na classe positiva faz com que o neurônio de saída dependa exclusivamente do bias constante $W_{21,0}$ para prever a classe negativa. Se executarmos o K-Means em *ambas* as classes (por exemplo, 2 centros para classe positiva e 2 centros para classe negativa, totalizando $K=4$ neurônios intermediários), a rede terá representações ativas específicas para as nuances geométricas da classe negativa, melhorando a precisão da fronteira de decisão.\n\n")
    
    f.write("3. **Otimização Supervisionada dos Centros e Variâncias (Ajuste por Gradiente):**\n")
    f.write("   - Na arquitetura RBF padrão, os centros e larguras são fixados na primeira fase (não supervisionada). Se aplicarmos o algoritmo de retropropagação do erro para atualizar conjuntamente os centros ($c_i$), as variâncias ($\\sigma_i^2$) e os pesos de saída ($w$), a RBF ajustará dinamicamente a posição e a forma geométrica dos clusters para otimizar diretamente a perda supervisionada, superando mínimos subótimos do K-Means.\n\n")
    
    f.write("4. **Aumento do Número de Centros ($K > 2$):**\n")
    f.write("   - Utilizar apenas 2 clusters pode simplificar excessivamente a distribuição dos compostos radioativos. Ao aumentar $K$ (por exemplo, para 4 ou 5 na classe positiva), a rede conseguirá capturar formatos de distribuição não convexos ou múltiplos focos de radiação dispersos no espaço bidimensional das variáveis $x_1$ e $x_2$.\n\n")
    
    f.write("5. **Regularização L2 (Weight Decay):**\n")
    f.write("   - Para evitar pesos excessivamente grandes que prejudicam a generalização (overfitting) em amostras de teste próximas à fronteira, pode-se introduzir um termo de penalização na Regra Delta (regressão Ridge no mapeamento RBF).\n")

print("Tudo resolvido e arquivos gravados!")
