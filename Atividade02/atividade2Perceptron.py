import numpy as np

# 1. Configurações Iniciais e Dados de Treinamento
taxa_aprendizagem = 0.01

# Dados de Treinamento: [x1, x2, x3, d]
dados_treinamento = np.array([
    [-0.6508, 0.1097, 4.0009, -1], [-1.4492, 0.8896, 4.4005, -1], [ 2.0850, 0.6876, 12.0710, -1],
    [ 0.2626, 1.1476, 7.7985,  1], [ 0.6418, 1.0234, 7.0427,  1], [ 0.2569, 0.6730, 8.3265, -1],
    [ 1.1155, 0.6043, 7.4446,  1], [ 0.0914, 0.3399, 7.0677, -1], [ 0.0121, 0.5256, 4.6316,  1],
    [-0.0429, 0.4660, 5.4323,  1], [ 0.4340, 0.6870, 8.2287, -1], [ 0.2735, 1.0287, 7.1934,  1],
    [ 0.4839, 0.4851, 7.4850, -1], [ 0.4089,-0.1267, 5.5019, -1], [ 1.4391, 0.1614, 8.5843, -1],
    [-0.9115,-0.1973, 2.1962, -1], [ 0.3654, 1.0475, 7.4858,  1], [ 0.2144, 0.7515, 7.1699,  1],
    [ 0.2013, 1.0014, 6.5489,  1], [ 0.6483, 0.2183, 5.8991,  1], [-0.1147, 0.2242, 7.2435, -1],
    [-0.7970, 0.8795, 3.8762,  1], [-1.0625, 0.6366, 2.4707,  1], [ 0.5307, 0.1285, 5.6883,  1],
    [-1.2200, 0.7777, 1.7252,  1], [ 0.3957, 0.1076, 5.6623, -1], [-0.1013, 0.5989, 7.1812, -1],
    [ 2.4482, 0.9455, 11.2095, 1], [ 2.0149, 0.6192, 10.9263, -1], [ 0.2012, 0.2611, 5.4631,  1]
])

# Amostras para Teste: [x1, x2, x3]
dados_teste = np.array([
    [-0.3565, 0.0620, 5.9891], [-0.7842, 1.1267, 5.5912], [ 0.3012, 0.5611, 5.8234],
    [ 0.7757, 1.0648, 8.0677], [ 0.1570, 0.8028, 6.3040], [-0.7014, 1.0316, 3.6005],
    [ 0.3748, 0.1536, 6.1537], [-0.6920, 0.9404, 4.4058], [-1.3970, 0.7141, 4.9263],
    [-1.8842,-0.2805, 1.2548]
])

# Inserindo x0 = -1 (bias) nas entradas
X_treino = np.c_[np.full(dados_treinamento.shape[0], -1), dados_treinamento[:, :3]]
d_treino = dados_treinamento[:, 3]

X_teste = np.c_[np.full(dados_teste.shape[0], -1), dados_teste]

# 2. Função de Ativação e Treinamento do Perceptron
def func_ativacao(v):
    return 1 if v >= 0 else -1

def treinar_perceptron():
    # Inicializa pesos aleatórios entre 0 e 1 (w0, w1, w2, w3)
    w = np.random.uniform(0, 1, 4)
    w_inicial = w.copy()
    epocas = 0
    
    while True:
        epocas += 1
        erro_na_epoca = False
        
        for i in range(len(X_treino)):
            x = X_treino[i]
            d = d_treino[i]
            
            # Produto escalar: v = (w0*x0) + (w1*x1) + (w2*x2) + (w3*x3)
            v = np.dot(w, x)
            y = func_ativacao(v)
            
            # Regra de aprendizado
            if y != d:
                erro_na_epoca = True
                w = w + taxa_aprendizagem * (d - y) * x
                
        # Condição de parada: nenhum erro na época
        if not erro_na_epoca:
            break
            
    return w_inicial, w, epocas

# 3. Execução dos 5 Treinamentos e Testes
resultados_treino = []
modelos_pesos = []

print("=== TABELA 1: RESULTADOS DOS TREINAMENTOS ===")
print("| Treinamento | w0 inicial | w1 inicial | w2 inicial | w3 inicial | w0 final | w1 final | w2 final | w3 final | Épocas |")
print("|---|---|---|---|---|---|---|---|---|---|")

for t in range(5):
    w_ini, w_fin, epocas = treinar_perceptron()
    modelos_pesos.append(w_fin)
    
    linha = f"| {t+1}º (T{t+1}) | {w_ini[0]:.4f} | {w_ini[1]:.4f} | {w_ini[2]:.4f} | {w_ini[3]:.4f} | {w_fin[0]:.4f} | {w_fin[1]:.4f} | {w_fin[2]:.4f} | {w_fin[3]:.4f} | {epocas} |"
    print(linha)

print("\n=== TABELA 2: CLASSIFICAÇÃO DAS AMOSTRAS DE TESTE ===")
print("| Amostra | x1 | x2 | x3 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |")
print("|---|---|---|---|---|---|---|---|---|")

for i, amostra in enumerate(X_teste):
    # Calcula a saída (y) para cada um dos 5 modelos treinados
    saidas = []
    for w in modelos_pesos:
        v = np.dot(w, amostra)
        saidas.append(func_ativacao(v))
        
    x1, x2, x3 = amostra[1], amostra[2], amostra[3]
    linha = f"| {i+1} | {x1:.4f} | {x2:.4f} | {x3:.4f} | {saidas[0]} | {saidas[1]} | {saidas[2]} | {saidas[3]} | {saidas[4]} |"
    print(linha)