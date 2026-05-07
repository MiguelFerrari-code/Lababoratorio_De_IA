import numpy as np
import matplotlib.pyplot as plt

# 1. Configurações Iniciais
taxa_aprendizagem = 0.0025
precisao = 1e-6

# Dados de Treinamento: [x1, x2, x3, x4, d]
dados_treinamento = np.array([
    [ 0.4329, -1.3719,  0.7022, -0.8535,  1], [ 0.3024,  0.2286,  0.8630,  2.7909, -1],
    [ 0.1349, -0.6445,  1.0530,  0.5687, -1], [ 0.3374, -1.7163,  0.3670, -0.6283, -1],
    [ 1.1434, -0.0485,  0.6637,  1.2606,  1], [ 1.3749, -0.5071,  0.4464,  1.3009,  1],
    [ 0.7221, -0.7587,  0.7681, -0.5592,  1], [ 0.4403, -0.8072,  0.5154, -0.3129,  1],
    [-0.5231,  0.3548,  0.2538,  1.5776, -1], [ 0.3255, -2.0000,  0.7112, -1.1209,  1],
    [ 0.5824,  1.3915, -0.2291,  4.1735, -1], [ 0.1340,  0.6081,  0.4450,  3.2230, -1],
    [ 0.1480, -0.2988,  0.4778,  0.8649,  1], [ 0.7359,  0.1869, -0.0872,  2.3584,  1],
    [ 0.7115, -1.1469,  0.3394,  0.9573, -1], [ 0.8251, -1.2840,  0.8452,  1.2382, -1],
    [ 0.1569,  0.3712,  0.8825,  1.7633,  1], [ 0.0033,  0.6835,  0.5389,  2.8249, -1],
    [ 0.4243,  0.8313,  0.2634,  3.5855, -1], [ 1.0490,  0.1326,  0.9138,  1.9792,  1],
    [ 1.4276,  0.5331, -0.0145,  3.7286,  1], [ 0.5971,  1.4865,  0.2904,  4.6069, -1],
    [ 0.8475,  2.1479,  0.3179,  5.8235, -1], [ 1.3967, -0.4171,  0.6443,  1.3927,  1],
    [ 0.0044,  1.5378,  0.6099,  4.7755, -1], [ 0.2201, -0.5668,  0.0515,  0.7829,  1],
    [ 0.6300, -1.2480,  0.8591,  0.8093, -1], [-0.2479,  0.8960,  0.0547,  1.7381,  1],
    [-0.3088, -0.0929,  0.8659,  1.5483, -1], [-0.5180,  1.4974,  0.5453,  2.3993,  1],
    [ 0.6833,  0.8266,  0.0829,  2.8864,  1], [ 0.4353, -1.4066,  0.4207, -0.4879,  1],
    [-0.1069, -3.2329,  0.1856, -2.4572, -1], [ 0.4662,  0.6261,  0.7304,  3.4370, -1],
    [ 0.8298, -1.4089,  0.3119,  1.3235, -1]
])

# Amostras para Teste: [x1, x2, x3, x4]
dados_teste = np.array([
    [ 0.9694,  0.6909,  0.4334,  3.4965], [ 0.5427,  1.3832,  0.6390,  4.0352],
    [ 0.6081, -0.9196,  0.5925,  0.1016], [-0.1618,  0.4694,  0.2030,  3.0117],
    [ 0.1870, -0.2578,  0.6124,  1.7749], [ 0.4891, -0.5276,  0.4378,  0.6439],
    [ 0.3777,  2.0149,  0.7423,  3.3932], [ 1.1498, -0.4067,  0.2469,  1.5866],
    [ 0.9325,  1.0950,  1.0359,  3.3591], [ 0.5060,  1.3317,  0.9222,  3.7174],
    [ 0.0497, -2.0656,  0.6124, -0.6585], [ 0.4004,  3.5369,  0.9766,  5.3532],
    [-0.1874,  1.3343,  0.5374,  3.2189], [ 0.5060,  1.3317,  0.9222,  3.7174],
    [ 1.6375, -0.7911,  0.7537,  0.5515]
])

# Inserindo x0 = -1 (bias)
X_treino = np.c_[np.full(dados_treinamento.shape[0], -1), dados_treinamento[:, :4]]
d_treino = dados_treinamento[:, 4]
X_teste = np.c_[np.full(dados_teste.shape[0], -1), dados_teste]

# 2. Função de Treinamento ADALINE (Regra Delta)
def treinar_adaline():
    w = np.random.uniform(0, 1, 5) # w0, w1, w2, w3, w4
    w_inicial = w.copy()
    epocas = 0
    historico_eqm = []
    
    # EQM Inicial
    u = np.dot(X_treino, w)
    eqm_atual = np.mean((d_treino - u)**2)
    
    while True:
        eqm_anterior = eqm_atual
        epocas += 1
        
        for i in range(len(X_treino)):
            u_i = np.dot(w, X_treino[i])
            w = w + taxa_aprendizagem * (d_treino[i] - u_i) * X_treino[i]
            
        u = np.dot(X_treino, w)
        eqm_atual = np.mean((d_treino - u)**2)
        historico_eqm.append(eqm_atual)
        
        if abs(eqm_atual - eqm_anterior) <= precisao:
            break
            
    return w_inicial, w, epocas, historico_eqm

# 3. Execução dos Treinamentos
modelos_pesos = []
historicos = []

print("=== TABELA 1: RESULTADOS DOS TREINAMENTOS ADALINE ===")
print("| T | w0 ini | w1 ini | w2 ini | w3 ini | w4 ini | w0 fin | w1 fin | w2 fin | w3 fin | w4 fin | Épocas |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")

for t in range(5):
    w_ini, w_fin, epocas, hist_eqm = treinar_adaline()
    modelos_pesos.append(w_fin)
    historicos.append(hist_eqm)
    
    linha = f"| T{t+1} | {w_ini[0]:.4f} | {w_ini[1]:.4f} | {w_ini[2]:.4f} | {w_ini[3]:.4f} | {w_ini[4]:.4f} | {w_fin[0]:.4f} | {w_fin[1]:.4f} | {w_fin[2]:.4f} | {w_fin[3]:.4f} | {w_fin[4]:.4f} | {epocas} |"
    print(linha)

# 4. Gráficos do Treinamento 1 e 2
plt.figure(figsize=(10, 5))
plt.plot(historicos[0], label='Treinamento 1 (T1)')
plt.plot(historicos[1], label='Treinamento 2 (T2)', linestyle='--')
plt.title('Erro Quadrático Médio (EQM) por Época - ADALINE')
plt.xlabel('Épocas')
plt.ylabel('EQM')
plt.legend()
plt.grid(True)
plt.savefig('grafico_eqm.png')
print("\n[!] Gráfico 'grafico_eqm.png' salvo com sucesso!")

# 5. Classificação (Teste)
def func_ativacao(v):
    return 1 if v >= 0 else -1

print("\n=== TABELA 2: CLASSIFICAÇÃO DAS AMOSTRAS (A = -1 / B = 1) ===")
print("| Amostra | x1 | x2 | x3 | x4 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |")
print("|---|---|---|---|---|---|---|---|---|---|")

for i, amostra in enumerate(X_teste):
    saidas = []
    for w in modelos_pesos:
        v = np.dot(w, amostra)
        saidas.append(func_ativacao(v))
        
    x1, x2, x3, x4 = amostra[1], amostra[2], amostra[3], amostra[4]
    linha = f"| {i+1} | {x1:.4f} | {x2:.4f} | {x3:.4f} | {x4:.4f} | {saidas[0]} | {saidas[1]} | {saidas[2]} | {saidas[3]} | {saidas[4]} |"
    print(linha)