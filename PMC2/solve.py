import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Ler as tabelas
dfs = pd.read_html('/home/alunos/Lababoratorio_De_IA/PMC2/PMC2.md')

# Conjunto de teste
df_test = dfs[0]
# Filtrar as linhas numéricas (Amostra 1 a 18)
X_test = []
Y_test = []
for i in range(1, len(df_test)):
    try:
        x_row = df_test.iloc[i, 1:5].values.astype(float)
        d_row = df_test.iloc[i, 5:8].values.astype(float)
        if not np.isnan(x_row).any() and not np.isnan(d_row).any():
            X_test.append(x_row)
            Y_test.append(d_row)
    except ValueError:
        pass
X_test = np.array(X_test)
Y_test = np.array(Y_test)

# Conjunto de treinamento
df_train = dfs[1]
b1_x = df_train.iloc[1:, 1:5].values
b1_d = df_train.iloc[1:, 5:8].values
b2_x = df_train.iloc[1:, 9:13].values
b2_d = df_train.iloc[1:, 13:16].values

# Limpar nan
b1_mask = ~pd.isna(b1_x).any(axis=1) & ~pd.isna(b1_d).any(axis=1)
b2_mask = ~pd.isna(b2_x).any(axis=1) & ~pd.isna(b2_d).any(axis=1)

b1_x = b1_x[b1_mask].astype(float)
b1_d = b1_d[b1_mask].astype(float)
b2_x = b2_x[b2_mask].astype(float)
b2_d = b2_d[b2_mask].astype(float)

X_train = np.vstack([b1_x, b2_x])
Y_train = np.vstack([b1_d, b2_d])

# Configurações do treinamento
eta = 0.1
alpha = 0.9
epsilon = 1e-6
num_hidden = 15

def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(s):
    # assumindo que s = sigmoid(x)
    return s * (1 - s)

class MLP:
    def __init__(self, input_size, hidden_size, output_size, init_W1=None, init_b1=None, init_W2=None, init_b2=None):
        if init_W1 is not None:
            self.W1 = init_W1.copy()
            self.b1 = init_b1.copy()
            self.W2 = init_W2.copy()
            self.b2 = init_b2.copy()
        else:
            self.W1 = np.random.rand(input_size, hidden_size)
            self.b1 = np.random.rand(1, hidden_size)
            self.W2 = np.random.rand(hidden_size, output_size)
            self.b2 = np.random.rand(1, output_size)
            
        # Velocidades para o momentum
        self.v_W1 = np.zeros_like(self.W1)
        self.v_b1 = np.zeros_like(self.b1)
        self.v_W2 = np.zeros_like(self.W2)
        self.v_b2 = np.zeros_like(self.b2)

    def forward(self, X):
        self.a1 = sigmoid(np.dot(X, self.W1) + self.b1)
        self.a2 = sigmoid(np.dot(self.a1, self.W2) + self.b2)
        return self.a2

    def backward(self, X, y, output, use_momentum=False):
        m = X.shape[0]
        
        error_output = output - y
        d_output = error_output * sigmoid_derivative(self.a2)
        
        error_hidden = np.dot(d_output, self.W2.T)
        d_hidden = error_hidden * sigmoid_derivative(self.a1)
        
        grad_W2 = np.dot(self.a1.T, d_output) / m
        grad_b2 = np.sum(d_output, axis=0, keepdims=True) / m
        grad_W1 = np.dot(X.T, d_hidden) / m
        grad_b1 = np.sum(d_hidden, axis=0, keepdims=True) / m
        
        if use_momentum:
            self.v_W2 = alpha * self.v_W2 - eta * grad_W2
            self.v_b2 = alpha * self.v_b2 - eta * grad_b2
            self.v_W1 = alpha * self.v_W1 - eta * grad_W1
            self.v_b1 = alpha * self.v_b1 - eta * grad_b1
            
            self.W2 += self.v_W2
            self.b2 += self.v_b2
            self.W1 += self.v_W1
            self.b1 += self.v_b1
        else:
            self.W2 -= eta * grad_W2
            self.b2 -= eta * grad_b2
            self.W1 -= eta * grad_W1
            self.b1 -= eta * grad_b1

def train_mlp(mlp, use_momentum=False):
    epoch = 0
    mse_history = []
    
    start_time = time.time()
    while True:
        output = mlp.forward(X_train)
        mse = np.mean((output - Y_train) ** 2)
        mse_history.append(mse)
        
        mlp.backward(X_train, Y_train, output, use_momentum)
        
        epoch += 1
        
        if epoch > 1:
            diff = abs(mse_history[-1] - mse_history[-2])
            if diff < epsilon or epoch >= 100000:
                break
                
    end_time = time.time()
    return mse_history, epoch, end_time - start_time

print("Iniciando treinamento 1 (Padrão)...")
mlp_std = MLP(4, num_hidden, 3)
# Salvar os pesos para o momentum
W1_init, b1_init, W2_init, b2_init = mlp_std.W1.copy(), mlp_std.b1.copy(), mlp_std.W2.copy(), mlp_std.b2.copy()

mse_std, epochs_std, time_std = train_mlp(mlp_std, use_momentum=False)

print("Iniciando treinamento 2 (Momentum)...")
mlp_mom = MLP(4, num_hidden, 3, init_W1=W1_init, init_b1=b1_init, init_W2=W2_init, init_b2=b2_init)
mse_mom, epochs_mom, time_mom = train_mlp(mlp_mom, use_momentum=True)

# Plotar os gráficos separadamente
fig, axs = plt.subplots(2, 1, figsize=(10, 10))
axs[0].plot(mse_std, color='blue')
axs[0].set_title(f'Backpropagation Padrão (EQM final: {mse_std[-1]:.6f}, Épocas: {epochs_std}, Tempo: {time_std:.2f}s)')
axs[0].set_xlabel('Épocas')
axs[0].set_ylabel('EQM')
axs[0].grid(True)

axs[1].plot(mse_mom, color='green')
axs[1].set_title(f'Backpropagation com Momentum (EQM final: {mse_mom[-1]:.6f}, Épocas: {epochs_mom}, Tempo: {time_mom:.2f}s)')
axs[1].set_xlabel('Épocas')
axs[1].set_ylabel('EQM')
axs[1].grid(True)

plt.tight_layout()
plt.savefig('/home/alunos/Lababoratorio_De_IA/PMC2/grafico_eqm.png')
print("Gráfico salvo em grafico_eqm.png")

# Pós-processamento e Validação
def pos_processamento(y):
    return np.round(y)

out_std = pos_processamento(mlp_std.forward(X_test))
out_mom = pos_processamento(mlp_mom.forward(X_test))

def calc_acerto(y_pred, y_true):
    acertos = 0
    for i in range(len(y_true)):
        if np.array_equal(y_pred[i], y_true[i]):
            acertos += 1
    return (acertos / len(y_true)) * 100

acerto_std = calc_acerto(out_std, Y_test)
acerto_mom = calc_acerto(out_mom, Y_test)

with open('/home/alunos/Lababoratorio_De_IA/PMC2/relatorio.md', 'w') as f:
    f.write("# Resultados da Atividade - PMC2\n\n")
    
    f.write("## Desempenho no Treinamento\n\n")
    f.write("| Método | Épocas | EQM Final | Tempo de Processamento (s) |\n")
    f.write("|---|---|---|---|\n")
    f.write(f"| Padrão | {epochs_std} | {mse_std[-1]:.6f} | {time_std:.2f} |\n")
    f.write(f"| Momentum | {epochs_mom} | {mse_mom[-1]:.6f} | {time_mom:.2f} |\n\n")
    f.write("Os gráficos de EQM versus épocas foram gerados no arquivo `grafico_eqm.png`.\n\n")
    
    f.write("## Validação no Conjunto de Teste\n\n")
    f.write("| Amostra | $d_1$ | $d_2$ | $d_3$ | $y_1$ (Padrão) | $y_2$ (Padrão) | $y_3$ (Padrão) | $y_1$ (Momentum) | $y_2$ (Momentum) | $y_3$ (Momentum) |\n")
    f.write("|---|---|---|---|---|---|---|---|---|---|\n")
    for i in range(len(Y_test)):
        row = f"| {i+1} | {int(Y_test[i][0])} | {int(Y_test[i][1])} | {int(Y_test[i][2])} "
        row += f"| {int(out_std[i][0])} | {int(out_std[i][1])} | {int(out_std[i][2])} "
        row += f"| {int(out_mom[i][0])} | {int(out_mom[i][1])} | {int(out_mom[i][2])} |"
        f.write(row + "\n")
        
    f.write(f"\n**Taxa de Acerto (Backpropagation Padrão):** {acerto_std:.2f}%\n")
    f.write(f"**Taxa de Acerto (Backpropagation com Momentum):** {acerto_mom:.2f}%\n")

print("Relatório salvo em relatorio.md")
