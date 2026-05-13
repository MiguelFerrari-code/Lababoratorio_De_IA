import re
import numpy as np
import matplotlib.pyplot as plt

# 1. Parsing dos dados
with open('/home/alunos/Lababoratorio_De_IA/PMC3/PMC3.md', 'r') as f:
    lines = f.readlines()

# Extrair validação (t=101 a 120)
val_values = []
for line in lines[109:149]:
    match = re.search(r'\*t\* = 1\d\d\s+(0\.\d+)', line)
    if match:
        val_values.append(float(match.group(1)))

# Extrair treino (t=1 a 100)
# As linhas úteis são as que contêm os valores, por exemplo:
# | *t* =  | 0.1701 | *t* =  | 0.2398 | *t* =  | 0.3087 | *t* =  | 0.3701 |
train_data = {}
for line in lines[188:264]:
    if "| *t* =" in line:
        parts = [p.strip() for p in line.split('|')]
        # parts: ['', '*t* =', '0.1701', '*t* =', '0.2398', '*t* =', '0.3087', '*t* =', '0.3701', '']
        if len(parts) >= 9:
            # We need to know which t this corresponds to. We look at the next line for the t indices.
            pass
    elif line.startswith('|') and not "*t* =" in line and "####" not in line and "mostra" not in line and "+---" not in line:
        parts = [p.strip() for p in line.split('|')]
        # parts: ['', '1', '', '26', '', '51', '', '76', '']
        pass

# Melhor forma: regex de (t, value)
# No anexo:
# row 1 tem "*t* =", e row 2 tem os índices e os espaços vazios.
# Isso é mais fácil fazer lendo a string toda e achando "*t* =\s+\|\s+0\.\d+"? Não.
# Vamos usar regex no texto inteiro:
text = "".join(lines[184:]) # Anexo
# Regex para achar *t* = \n | <numero> | <vazio> |
# Como é markdown:
# | *t* =  | 0.1701 |
# | 1      |        |
# Dá pra extrair todos os valores 0.\d{4} do anexo ordenadamente? Não, estão misturados.
# Vou parsear a cada 2 linhas no anexo.
train_values = np.zeros(100)
idx_line = False
vals = []
for line in lines[188:264]:
    if "| *t* =" in line:
        # Extrai os valores
        matches = re.findall(r'0\.\d{4}', line)
        vals = [float(m) for m in matches]
    elif line.startswith('|') and not "+---" in line:
        # Extrai os indices
        matches = re.findall(r'\|\s*(\d+)\s*\|', line)
        if len(matches) == len(vals):
            for i, idx in enumerate(matches):
                train_values[int(idx)-1] = vals[i]

time_series = np.concatenate([train_values, val_values])

# 2. Configurações da Rede TDNN
eta = 0.1
alpha = 0.8
epsilon = 0.5e-6

def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(s):
    return s * (1 - s)

class TDNN:
    def __init__(self, p, hidden_size):
        self.p = p
        self.W1 = np.random.rand(p, hidden_size)
        self.b1 = np.random.rand(1, hidden_size)
        self.W2 = np.random.rand(hidden_size, 1)
        self.b2 = np.random.rand(1, 1)
        
        self.v_W1 = np.zeros_like(self.W1)
        self.v_b1 = np.zeros_like(self.b1)
        self.v_W2 = np.zeros_like(self.W2)
        self.v_b2 = np.zeros_like(self.b2)

    def forward(self, X):
        self.a1 = sigmoid(np.dot(X, self.W1) + self.b1)
        self.a2 = sigmoid(np.dot(self.a1, self.W2) + self.b2)
        return self.a2

    def backward(self, X, y, output):
        m = X.shape[0]
        
        error_output = output - y
        d_output = error_output * sigmoid_derivative(self.a2)
        
        error_hidden = np.dot(d_output, self.W2.T)
        d_hidden = error_hidden * sigmoid_derivative(self.a1)
        
        grad_W2 = np.dot(self.a1.T, d_output) / m
        grad_b2 = np.sum(d_output, axis=0, keepdims=True) / m
        grad_W1 = np.dot(X.T, d_hidden) / m
        grad_b1 = np.sum(d_hidden, axis=0, keepdims=True) / m
        
        self.v_W2 = alpha * self.v_W2 - eta * grad_W2
        self.v_b2 = alpha * self.v_b2 - eta * grad_b2
        self.v_W1 = alpha * self.v_W1 - eta * grad_W1
        self.v_b1 = alpha * self.v_b1 - eta * grad_b1
        
        self.W2 += self.v_W2
        self.b2 += self.v_b2
        self.W1 += self.v_W1
        self.b1 += self.v_b1

def create_dataset(ts, p, start_idx, end_idx):
    # ts: 1D array de tamanho 120 (0 a 119) correspondendo a t=1..120
    # Queremos prever t de start_idx até end_idx
    X, Y = [], []
    for t in range(start_idx, end_idx + 1):
        # Para prever f(t), precisamos de f(t-1) ... f(t-p)
        # O índice em ts de f(t) é t-1.
        # Os delays são (t-1-1) ... (t-1-p) => ts[t-p-1 : t-1]
        # E eles devem estar na ordem f(t-p), ..., f(t-1)
        x = ts[t - p - 1 : t - 1]
        y = ts[t - 1]
        X.append(x)
        Y.append([y])
    return np.array(X), np.array(Y)

def train_network(p, hidden_size):
    # Treino de t=p+1 até 100
    X_train, Y_train = create_dataset(time_series, p, p + 1, 100)
    
    net = TDNN(p, hidden_size)
    epoch = 0
    mse_history = []
    
    while True:
        output = net.forward(X_train)
        mse = np.mean((output - Y_train) ** 2)
        mse_history.append(mse)
        
        net.backward(X_train, Y_train, output)
        
        epoch += 1
        if epoch > 1:
            diff = abs(mse_history[-1] - mse_history[-2])
            if diff < epsilon or epoch >= 100000:
                break
    return net, mse_history, epoch

networks_config = [
    {"name": "Rede 1", "p": 5, "N1": 10},
    {"name": "Rede 2", "p": 10, "N1": 15},
    {"name": "Rede 3", "p": 15, "N1": 25}
]

results = []

for config in networks_config:
    print(f"Treinando {config['name']}...")
    net_results = []
    for t in range(3):
        net, mse_history, epochs = train_network(config['p'], config['N1'])
        
        # Teste (t=101 a 120)
        X_test, Y_test = create_dataset(time_series, config['p'], 101, 120)
        preds = net.forward(X_test)
        
        # Erro relativo % para cada amostra de teste
        erros_rel = np.abs(preds - Y_test) / np.abs(Y_test) * 100
        
        net_results.append({
            "treinamento": f"T{t+1}",
            "eqm_final": mse_history[-1],
            "epocas": epochs,
            "hist": mse_history,
            "preds": preds.flatten(),
            "erro_relativo_medio": np.mean(erros_rel),
            "variancia": np.var(erros_rel),
            "net": net
        })
    results.append({
        "config": config,
        "trains": net_results
    })

# Encontrar o melhor treinamento para cada topologia (menor erro relativo médio)
best_trainings = []
for r in results:
    best_t = min(r["trains"], key=lambda x: x["erro_relativo_medio"])
    best_trainings.append(best_t)

# Gerar Gráficos
# 1. EQM x Épocas (3 subplots)
fig, axs = plt.subplots(3, 1, figsize=(10, 15))
for i, best in enumerate(best_trainings):
    axs[i].plot(best["hist"], color=f'C{i}')
    axs[i].set_title(f"{results[i]['config']['name']} (Melhor Treinamento: {best['treinamento']}) - EQM Final: {best['eqm_final']:.6f}")
    axs[i].set_xlabel("Épocas")
    axs[i].set_ylabel("EQM")
    axs[i].grid(True)
plt.tight_layout()
plt.savefig('/home/alunos/Lababoratorio_De_IA/PMC3/grafico_eqm.png')
plt.close()

# 2. Desejado x Estimado no Teste (t=101..120)
fig, axs = plt.subplots(3, 1, figsize=(10, 15))
t_test = np.arange(101, 121)
y_true = time_series[100:120]
for i, best in enumerate(best_trainings):
    axs[i].plot(t_test, y_true, label="Desejado", marker='o')
    axs[i].plot(t_test, best["preds"], label="Estimado", marker='x')
    axs[i].set_title(f"{results[i]['config']['name']} - Previsão no Conjunto de Teste")
    axs[i].set_xlabel("t")
    axs[i].set_ylabel("f(t)")
    axs[i].legend()
    axs[i].grid(True)
plt.tight_layout()
plt.savefig('/home/alunos/Lababoratorio_De_IA/PMC3/grafico_previsao.png')
plt.close()

# Relatório
with open('/home/alunos/Lababoratorio_De_IA/PMC3/relatorio.md', 'w') as f:
    f.write("# Resultados da Atividade - PMC3 (TDNN)\n\n")
    
    f.write("## 2. Resultados dos Treinamentos\n\n")
    f.write("| Treinamento | Rede 1 (EQM) | Rede 1 (Épocas) | Rede 2 (EQM) | Rede 2 (Épocas) | Rede 3 (EQM) | Rede 3 (Épocas) |\n")
    f.write("|---|---|---|---|---|---|---|\n")
    for t in range(3):
        f.write(f"| T{t+1} | ")
        for r in results:
            tr = r["trains"][t]
            f.write(f"{tr['eqm_final']:.6f} | {tr['epocas']} | ")
        f.write("\n")
        
    f.write("\n## 3. Validação no Conjunto de Teste\n\n")
    f.write("| Amostra | $f(t)$ | Rede 1 (T1) | Rede 1 (T2) | Rede 1 (T3) | Rede 2 (T1) | Rede 2 (T2) | Rede 2 (T3) | Rede 3 (T1) | Rede 3 (T2) | Rede 3 (T3) |\n")
    f.write("|---|---|---|---|---|---|---|---|---|---|---|\n")
    for i in range(20):
        t_val = 101 + i
        row = f"| *t* = {t_val} | {y_true[i]:.4f} | "
        for r in results:
            for tr in r["trains"]:
                row += f"{tr['preds'][i]:.4f} | "
        f.write(row + "\n")
        
    f.write("| Erro Relativo Médio (%) | | ")
    for r in results:
        for tr in r["trains"]:
            f.write(f"{tr['erro_relativo_medio']:.4f} | ")
    f.write("\n| Variância (%) | | ")
    for r in results:
        for tr in r["trains"]:
            f.write(f"{tr['variancia']:.4f} | ")
    f.write("\n\n")
    
    f.write("## 4. e 5. Gráficos\n")
    f.write("Os gráficos de EQM versus Épocas estão no arquivo `grafico_eqm.png`.\n")
    f.write("Os gráficos de valores desejados versus estimados estão no arquivo `grafico_previsao.png`.\n\n")
    
    f.write("## 6. Melhor Configuração\n")
    # Encontrar a topologia que tem o melhor dentre os best_trainings
    overall_best = min(best_trainings, key=lambda x: x["erro_relativo_medio"])
    for r in results:
        if overall_best in r["trains"]:
            best_net_name = r["config"]["name"]
            
    f.write(f"Analisando o erro relativo médio e a variância no conjunto de testes, a topologia mais adequada é a **{best_net_name}** com a configuração de treinamento **{overall_best['treinamento']}**. Ela obteve o menor erro relativo, demonstrando melhor capacidade de generalização e captura das não linearidades da série temporal.\n\n")
    
    f.write("## 7. Comentários sobre Variantes do Backpropagation\n")
    f.write("**a. Algoritmo Resilient-Propagation (RProp):**\n")
    f.write("A principal característica do RProp é que ele utiliza apenas o *sinal* do gradiente da função de erro para atualizar os pesos, ignorando a magnitude do gradiente. Isso resolve o problema de desvanecimento do gradiente (comum em funções sigmóides cujas derivadas se aproximam de zero nas extremidades). A vantagem é uma convergência muito mais rápida e menos oscilações comparada ao Backpropagation padrão, e a eliminação da necessidade de tentar advinhar parâmetros perfeitos de taxa de aprendizagem global, já que ele adapta um tamanho de passo específico para cada peso individualmente.\n\n")
    
    f.write("**b. Algoritmo Levenberg-Marquardt (LM):**\n")
    f.write("O algoritmo LM é uma mescla entre o método do Gradiente Descendente e o Método de Gauss-Newton. Sua principal característica é a utilização da aproximação da matriz Hessiana baseada na matriz Jacobiana. A vantagem colossal deste método é sua velocidade extrema de convergência para redes de tamanho pequeno a médio (é frequentemente o algoritmo mais rápido disponível nestes casos). No entanto, sua desvantagem é o alto custo computacional por época e o alto uso de memória (devido ao cálculo e inversão da matriz Jacobiana), tornando-se inviável para redes muito grandes.\n")
    
print("Pronto! Resultados salvos.")
