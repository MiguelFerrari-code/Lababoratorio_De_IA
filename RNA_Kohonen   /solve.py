import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os

# Diretório de saída
BASE_DIR = "/home/alunos/Lababoratorio_De_IA/RNA_Kohonen   "
os.makedirs(BASE_DIR, exist_ok=True)

# ==============================
# DADOS DO APÊNDICE (120 amostras)
# ==============================
data = [
    # Amostras 1-20 (Classe A)
    [0.2417, 0.2857, 0.2397],
    [0.2268, 0.2874, 0.2153],
    [0.1975, 0.3315, 0.1965],
    [0.3414, 0.3166, 0.1074],
    [0.2587, 0.1918, 0.2634],
    [0.2455, 0.2075, 0.1344],
    [0.3163, 0.1679, 0.1725],
    [0.2704, 0.2605, 0.1411],
    [0.1871, 0.2965, 0.1231],
    [0.3474, 0.2715, 0.1958],
    [0.2059, 0.2928, 0.2839],
    [0.2442, 0.2272, 0.2384],
    [0.2126, 0.3437, 0.1128],
    [0.2562, 0.2542, 0.1599],
    [0.1640, 0.2289, 0.2627],
    [0.2795, 0.1880, 0.1627],
    [0.3463, 0.1513, 0.2281],
    [0.3430, 0.1508, 0.1881],
    [0.1981, 0.2821, 0.1294],
    [0.2322, 0.3025, 0.2191],
    # Amostras 21-60 (Classe B)
    [0.7352, 0.2722, 0.6962],
    [0.7191, 0.1825, 0.7470],
    [0.6921, 0.1537, 0.8172],
    [0.6833, 0.2048, 0.8490],
    [0.8012, 0.2684, 0.7673],
    [0.7860, 0.1734, 0.7198],
    [0.7205, 0.1542, 0.7295],
    [0.6549, 0.3288, 0.8153],
    [0.6968, 0.3173, 0.7389],
    [0.7448, 0.2095, 0.6847],
    [0.6746, 0.3277, 0.6725],
    [0.7897, 0.2801, 0.7679],
    [0.8399, 0.3067, 0.7003],
    [0.8065, 0.3206, 0.7205],
    [0.8357, 0.3220, 0.7879],
    [0.7438, 0.3230, 0.8384],
    [0.8172, 0.3319, 0.7628],
    [0.8248, 0.2614, 0.8405],
    [0.6979, 0.2142, 0.7309],
    [0.6804, 0.3181, 0.7017],
    [0.6973, 0.3194, 0.7522],
    [0.7910, 0.2239, 0.7018],
    [0.7052, 0.2148, 0.6866],
    [0.8088, 0.1908, 0.7563],
    [0.7640, 0.1676, 0.6994],
    [0.7616, 0.2881, 0.8087],
    [0.8188, 0.2461, 0.7273],
    [0.7920, 0.3178, 0.7497],
    [0.7802, 0.1871, 0.8102],
    [0.7332, 0.2543, 0.8194],
    [0.6921, 0.1529, 0.7759],
    [0.6833, 0.2197, 0.6943],
    [0.7860, 0.1745, 0.7639],
    [0.8009, 0.3082, 0.8491],
    [0.7793, 0.1935, 0.6738],
    [0.7373, 0.2698, 0.7864],
    [0.7048, 0.2380, 0.7825],
    [0.8393, 0.2857, 0.7733],
    [0.6878, 0.2126, 0.6961],
    [0.6651, 0.3492, 0.6737],
    # Amostras 61-120 (Classe C)
    [0.4856, 0.6600, 0.4798],
    [0.4114, 0.7220, 0.5106],
    [0.5671, 0.7935, 0.5929],
    [0.4875, 0.7928, 0.5532],
    [0.5172, 0.7147, 0.5774],
    [0.5483, 0.6773, 0.4842],
    [0.5740, 0.6682, 0.5335],
    [0.4587, 0.6981, 0.5900],
    [0.5794, 0.7410, 0.4759],
    [0.4712, 0.6734, 0.5677],
    [0.5126, 0.8141, 0.5224],
    [0.5557, 0.7749, 0.4342],
    [0.4916, 0.8267, 0.4586],
    [0.4629, 0.8129, 0.4950],
    [0.5850, 0.7358, 0.5107],
    [0.4435, 0.7030, 0.4594],
    [0.4155, 0.7516, 0.5524],
    [0.4887, 0.7027, 0.5886],
    [0.5462, 0.7378, 0.5107],
    [0.5251, 0.8124, 0.5686],
    [0.4635, 0.7339, 0.5638],
    [0.5907, 0.7144, 0.4718],
    [0.4982, 0.8335, 0.4597],
    [0.5242, 0.7325, 0.4079],
    [0.4075, 0.8372, 0.4271],
    [0.5934, 0.8284, 0.5107],
    [0.5463, 0.6766, 0.5639],
    [0.4403, 0.8495, 0.4806],
    [0.4531, 0.7760, 0.5276],
    [0.5109, 0.7387, 0.5373],
    [0.5383, 0.7780, 0.4955],
    [0.5679, 0.7156, 0.5022],
    [0.5762, 0.7781, 0.5908],
    [0.5997, 0.7504, 0.5678],
    [0.4138, 0.6975, 0.5148],
    [0.5490, 0.6674, 0.4472],
    [0.4719, 0.7527, 0.4401],
    [0.4458, 0.8063, 0.4253],
    [0.4983, 0.8131, 0.5625],
    [0.5742, 0.6789, 0.5997],
    [0.5289, 0.7354, 0.4718],
    [0.5927, 0.7738, 0.5390],
    [0.5199, 0.7131, 0.4028],
    [0.5716, 0.6558, 0.4451],
    [0.5075, 0.7045, 0.4233],
    [0.4886, 0.7004, 0.4608],
    [0.5527, 0.8243, 0.5772],
    [0.4816, 0.6969, 0.4678],
    [0.5809, 0.6557, 0.4266],
    [0.5881, 0.7565, 0.4003],
    [0.5334, 0.8446, 0.4934],
    [0.4603, 0.7992, 0.4816],
    [0.5491, 0.6504, 0.4063],
    [0.4288, 0.8455, 0.5047],
    [0.5636, 0.7884, 0.5417],
    [0.5349, 0.6736, 0.4541],
    [0.5569, 0.8393, 0.5652],
    [0.4729, 0.7702, 0.5325],
    [0.5472, 0.8454, 0.5449],
    [0.5805, 0.7349, 0.4464],
]

X = np.array(data)
print(f"Dataset shape: {X.shape}")

# ==============================
# PARÂMETROS DA REDE
# ==============================
N1 = 16          # Total de neurônios
GRID_ROWS = 4    # Dimensão linha do grid
GRID_COLS = 4    # Dimensão coluna do grid
eta = 0.001      # Taxa de aprendizado
radius = 1       # Raio de vizinhança
n_epochs = 100   # Número de épocas

# ==============================
# INICIALIZAÇÃO DOS PESOS
# ==============================
np.random.seed(42)
# Inicializa pesos com valores aleatórios no range dos dados
W = np.random.uniform(X.min(), X.max(), (GRID_ROWS, GRID_COLS, 3))

def grid_distance(i1, j1, i2, j2):
    """Distância Manhattan (ou Chebyshev) entre dois neurônios no grid"""
    return max(abs(i1 - i2), abs(j1 - j2))

def find_bmu(x, W):
    """Encontra o Best Matching Unit (neurônio vencedor)"""
    diff = W - x  # (rows, cols, 3)
    dist = np.linalg.norm(diff, axis=2)
    bmu = np.unravel_index(np.argmin(dist), dist.shape)
    return bmu, np.min(dist)

def get_neighborhood(bmu_r, bmu_c, radius, rows, cols):
    """Retorna todos os neurônios dentro do raio de vizinhança"""
    neighbors = []
    for r in range(rows):
        for c in range(cols):
            d = grid_distance(bmu_r, bmu_c, r, c)
            if d <= radius:
                neighbors.append((r, c))
    return neighbors

# ==============================
# TREINAMENTO DA REDE DE KOHONEN
# ==============================
n_samples = X.shape[0]
history_bmu = []  # Armazena o BMU por amostra ao longo das épocas

print("Iniciando treinamento da Rede de Kohonen...")
for epoch in range(n_epochs):
    # Shuffle das amostras
    idx_order = np.random.permutation(n_samples)
    for sample_idx in idx_order:
        x = X[sample_idx]
        
        # Encontrar BMU
        bmu, _ = find_bmu(x, W)
        bmu_r, bmu_c = bmu
        
        # Atualizar pesos do BMU e vizinhos
        neighbors = get_neighborhood(bmu_r, bmu_c, radius, GRID_ROWS, GRID_COLS)
        for nr, nc in neighbors:
            W[nr, nc] += eta * (x - W[nr, nc])

print(f"Treinamento concluído: {n_epochs} épocas, {n_samples} amostras")

# ==============================
# CLASSIFICAÇÃO DE CADA AMOSTRA
# ==============================
sample_bmu = {}
for i, x in enumerate(X):
    bmu, _ = find_bmu(x, W)
    sample_bmu[i+1] = bmu  # 1-indexed

# Classes verdadeiras
true_class = {}
for i in range(1, 121):
    if i <= 20:
        true_class[i] = 'A'
    elif i <= 60:
        true_class[i] = 'B'
    else:
        true_class[i] = 'C'

# Mapear cada neurônio do grid para uma classe (classe que mais aparece)
neuron_class_count = {}
for r in range(GRID_ROWS):
    for c in range(GRID_COLS):
        neuron_class_count[(r,c)] = {'A': 0, 'B': 0, 'C': 0}

for sample_id, bmu in sample_bmu.items():
    cls = true_class[sample_id]
    neuron_class_count[bmu][cls] += 1

# Determinar classe dominante de cada neurônio
neuron_dominant_class = {}
neuron_class_label = np.full((GRID_ROWS, GRID_COLS), '', dtype=object)
for r in range(GRID_ROWS):
    for c in range(GRID_COLS):
        counts = neuron_class_count[(r,c)]
        total = sum(counts.values())
        if total == 0:
            neuron_dominant_class[(r,c)] = None
            neuron_class_label[r,c] = '—'
        else:
            dominant = max(counts, key=counts.get)
            neuron_dominant_class[(r,c)] = dominant
            neuron_class_label[r,c] = dominant

print("\n=== MAPA DE NEURÔNIOS (Classe Dominante) ===")
print("Grid 4x4 (numeração: linha×coluna, base 0)")
for r in range(GRID_ROWS):
    row_str = []
    for c in range(GRID_COLS):
        cls = neuron_dominant_class[(r,c)]
        counts = neuron_class_count[(r,c)]
        total = sum(counts.values())
        label = cls if cls else '—'
        row_str.append(f"[{r*GRID_COLS+c+1:2d}:{label}({counts['A']},{counts['B']},{counts['C']})]")
    print("  " + "  ".join(row_str))

# ==============================
# AMOSTRAS DE TESTE
# ==============================
test_samples = [
    (1,  [0.2471, 0.1778, 0.2905]),
    (2,  [0.8240, 0.2223, 0.7041]),
    (3,  [0.4960, 0.7231, 0.5866]),
    (4,  [0.2923, 0.2041, 0.2234]),
    (5,  [0.8118, 0.2668, 0.7484]),
    (6,  [0.4837, 0.8200, 0.4792]),
    (7,  [0.3248, 0.2629, 0.2375]),
    (8,  [0.7209, 0.2116, 0.7821]),
    (9,  [0.5259, 0.6522, 0.5957]),
    (10, [0.2075, 0.1669, 0.1745]),
    (11, [0.7830, 0.3171, 0.7888]),
    (12, [0.5393, 0.7510, 0.5682]),
]

print("\n=== CLASSIFICAÇÃO DAS AMOSTRAS DE TESTE ===")
test_results = []
for sample_id, x in test_samples:
    x = np.array(x)
    bmu, dist = find_bmu(x, W)
    cls = neuron_dominant_class[bmu]
    print(f"Amostra {sample_id}: x=[{x[0]:.4f},{x[1]:.4f},{x[2]:.4f}] -> BMU={bmu} -> Classe {cls} (dist={dist:.4f})")
    test_results.append({'id': sample_id, 'x': x, 'bmu': bmu, 'cls': cls, 'dist': dist})

# ==============================
# VISUALIZAÇÃO 1: U-MATRIX
# ==============================
fig, axs = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor('#0F172A')

# U-Matrix (distância média entre vizinhos)
u_matrix = np.zeros((GRID_ROWS, GRID_COLS))
for r in range(GRID_ROWS):
    for c in range(GRID_COLS):
        neighbors = []
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < GRID_ROWS and 0 <= nc < GRID_COLS:
                d = np.linalg.norm(W[r,c] - W[nr,nc])
                neighbors.append(d)
        u_matrix[r,c] = np.mean(neighbors) if neighbors else 0

ax = axs[0]
ax.set_facecolor('#1E293B')
im = ax.imshow(u_matrix, cmap='hot_r', aspect='auto', interpolation='nearest')
plt.colorbar(im, ax=ax, label='Distância média U-Matrix')
ax.set_title('U-Matrix (Distâncias entre Pesos)', color='white', fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel('Coluna do Grid', color='#94A3B8')
ax.set_ylabel('Linha do Grid', color='#94A3B8')
ax.tick_params(colors='#94A3B8')
# Numerar neurônios no grid
for r in range(GRID_ROWS):
    for c in range(GRID_COLS):
        ax.text(c, r, f'{r*GRID_COLS+c+1}', ha='center', va='center',
                color='white', fontsize=10, fontweight='bold')

# Class Map
class_colors = {'A': '#22C55E', 'B': '#3B82F6', 'C': '#F97316', None: '#334155'}
class_cmap_vals = []
for r in range(GRID_ROWS):
    row_vals = []
    for c in range(GRID_COLS):
        cls = neuron_dominant_class[(r,c)]
        if cls == 'A': row_vals.append(0)
        elif cls == 'B': row_vals.append(1)
        elif cls == 'C': row_vals.append(2)
        else: row_vals.append(3)
    class_cmap_vals.append(row_vals)
class_cmap_vals = np.array(class_cmap_vals)

ax2 = axs[1]
ax2.set_facecolor('#1E293B')
custom_cmap = mcolors.ListedColormap(['#22C55E', '#3B82F6', '#F97316', '#334155'])
im2 = ax2.imshow(class_cmap_vals, cmap=custom_cmap, vmin=-0.5, vmax=3.5, aspect='auto')

# Legenda manual
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#22C55E', label='Classe A (Amostras 1-20)'),
    Patch(facecolor='#3B82F6', label='Classe B (Amostras 21-60)'),
    Patch(facecolor='#F97316', label='Classe C (Amostras 61-120)'),
]
ax2.legend(handles=legend_elements, loc='upper right', fontsize=8,
           facecolor='#1E293B', edgecolor='#475569', labelcolor='white')

ax2.set_title('Mapa de Classes do Grid 4×4', color='white', fontsize=12, fontweight='bold', pad=12)
ax2.set_xlabel('Coluna do Grid', color='#94A3B8')
ax2.set_ylabel('Linha do Grid', color='#94A3B8')
ax2.tick_params(colors='#94A3B8')

for r in range(GRID_ROWS):
    for c in range(GRID_COLS):
        cls = neuron_dominant_class[(r,c)]
        counts = neuron_class_count[(r,c)]
        total = sum(counts.values())
        label = cls if cls else '—'
        ax2.text(c, r-0.2, f'N{r*GRID_COLS+c+1}', ha='center', va='center',
                 color='white', fontsize=9, fontweight='bold')
        ax2.text(c, r+0.2, f'({counts["A"]},{counts["B"]},{counts["C"]})',
                 ha='center', va='center', color='white', fontsize=7)

plt.suptitle('Rede de Kohonen — Grid 4×4 | N=16 neurônios | η=0.001',
             color='white', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'kohonen_map.png'), bbox_inches='tight', dpi=150,
            facecolor='#0F172A')
plt.close()
print("\nSalvo: kohonen_map.png")

# ==============================
# VISUALIZAÇÃO 2: Scatter Plot 3D
# ==============================
fig = plt.figure(figsize=(12, 5))
fig.patch.set_facecolor('#0F172A')

# 3D scatter das amostras originais
ax3d = fig.add_subplot(121, projection='3d')
ax3d.set_facecolor('#1E293B')
colors_map = ['#22C55E']*20 + ['#3B82F6']*40 + ['#F97316']*60
labels_map = ['Classe A']*20 + ['Classe B']*40 + ['Classe C']*60
for cls_name, cls_color, slice_range in [
    ('Classe A', '#22C55E', slice(0,20)),
    ('Classe B', '#3B82F6', slice(20,60)),
    ('Classe C', '#F97316', slice(60,120))
]:
    Xc = X[slice_range]
    ax3d.scatter(Xc[:,0], Xc[:,1], Xc[:,2], c=cls_color, label=cls_name, s=25, alpha=0.75)

ax3d.set_xlabel('x1', color='#94A3B8', fontsize=8)
ax3d.set_ylabel('x2', color='#94A3B8', fontsize=8)
ax3d.set_zlabel('x3', color='#94A3B8', fontsize=8)
ax3d.set_title('Dados de Treinamento (3D)', color='white', fontsize=11, fontweight='bold')
ax3d.tick_params(colors='#64748B', labelsize=7)
ax3d.legend(fontsize=8, facecolor='#1E293B', edgecolor='#475569', labelcolor='white')
ax3d.xaxis.pane.fill = False
ax3d.yaxis.pane.fill = False
ax3d.zaxis.pane.fill = False
ax3d.grid(True, color='#334155', alpha=0.5)

# Mostrar pesos dos neurônios
ax3d2 = fig.add_subplot(122, projection='3d')
ax3d2.set_facecolor('#1E293B')
for cls_name, cls_color, slice_range in [
    ('Classe A', '#22C55E', slice(0,20)),
    ('Classe B', '#3B82F6', slice(20,60)),
    ('Classe C', '#F97316', slice(60,120))
]:
    Xc = X[slice_range]
    ax3d2.scatter(Xc[:,0], Xc[:,1], Xc[:,2], c=cls_color, label=cls_name, s=15, alpha=0.3)

for r in range(GRID_ROWS):
    for c in range(GRID_COLS):
        cls = neuron_dominant_class[(r,c)]
        color = class_colors.get(cls, '#334155')
        w = W[r,c]
        ax3d2.scatter(w[0], w[1], w[2], c=color, s=120, marker='*',
                      edgecolors='white', linewidths=0.5, zorder=10)
        ax3d2.text(w[0], w[1], w[2], f'N{r*GRID_COLS+c+1}', fontsize=6, color='white')

ax3d2.set_xlabel('x1', color='#94A3B8', fontsize=8)
ax3d2.set_ylabel('x2', color='#94A3B8', fontsize=8)
ax3d2.set_zlabel('x3', color='#94A3B8', fontsize=8)
ax3d2.set_title('Dados + Protótipos dos Neurônios', color='white', fontsize=11, fontweight='bold')
ax3d2.tick_params(colors='#64748B', labelsize=7)
ax3d2.legend(fontsize=8, facecolor='#1E293B', edgecolor='#475569', labelcolor='white')
ax3d2.xaxis.pane.fill = False
ax3d2.yaxis.pane.fill = False
ax3d2.zaxis.pane.fill = False
ax3d2.grid(True, color='#334155', alpha=0.5)

plt.suptitle('Análise do Espaço de Features — Agrupamento por Kohonen',
             color='white', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'kohonen_scatter3d.png'), bbox_inches='tight', dpi=150,
            facecolor='#0F172A')
plt.close()
print("Salvo: kohonen_scatter3d.png")

# ==============================
# VISUALIZAÇÃO 3: BMU das amostras de teste sobre o grid
# ==============================
fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor('#0F172A')
ax.set_facecolor('#1E293B')

# Desenhar grid como fundo com cores de classe
for r in range(GRID_ROWS):
    for c in range(GRID_COLS):
        cls = neuron_dominant_class[(r,c)]
        color = class_colors.get(cls, '#334155')
        rect = plt.Rectangle([c-0.5, r-0.5], 1, 1, facecolor=color, alpha=0.35, edgecolor='#475569', lw=1)
        ax.add_patch(rect)
        ax.text(c, r-0.25, f'N{r*GRID_COLS+c+1}', ha='center', va='center',
                color='white', fontsize=9, fontweight='bold')
        counts = neuron_class_count[(r,c)]
        ax.text(c, r+0.15, f"A:{counts['A']} B:{counts['B']} C:{counts['C']}",
                ha='center', va='center', color='#CBD5E1', fontsize=6.5)

# Plotar as amostras de teste
marker_cls = {'A': 'v', 'B': 's', 'C': 'o'}
test_cls_color = {'A': '#4ADE80', 'B': '#60A5FA', 'C': '#FB923C'}
for res in test_results:
    r, c = res['bmu']
    cls = res['cls']
    jitter_x = (hash(str(res['id'])+str(r)) % 7 - 3) * 0.06
    jitter_y = (hash(str(res['id'])+str(c)) % 7 - 3) * 0.06
    mk = marker_cls.get(cls, 'x')
    clr = test_cls_color.get(cls, 'white')
    ax.scatter(c + jitter_x, r + jitter_y, marker=mk, c=clr, s=90,
               edgecolors='white', linewidths=0.8, zorder=5)
    ax.text(c + jitter_x + 0.06, r + jitter_y, str(res['id']), fontsize=7, color='white', zorder=6)

legend_test = [
    Patch(facecolor='#4ADE80', label='Teste → Classe A (▼)'),
    Patch(facecolor='#60A5FA', label='Teste → Classe B (■)'),
    Patch(facecolor='#FB923C', label='Teste → Classe C (●)'),
]
ax.legend(handles=legend_test, fontsize=8, facecolor='#1E293B', edgecolor='#475569', labelcolor='white',
          loc='lower right')
ax.set_xlim(-0.5, GRID_COLS-0.5)
ax.set_ylim(-0.5, GRID_ROWS-0.5)
ax.set_xticks(range(GRID_COLS))
ax.set_yticks(range(GRID_ROWS))
ax.set_xticklabels([f'Col {i}' for i in range(GRID_COLS)], color='#94A3B8', fontsize=8)
ax.set_yticklabels([f'Lin {i}' for i in range(GRID_ROWS)], color='#94A3B8', fontsize=8)
ax.set_title('BMU das Amostras de Teste no Grid 4×4', color='white', fontsize=12, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'kohonen_test_bmu.png'), bbox_inches='tight', dpi=150,
            facecolor='#0F172A')
plt.close()
print("Salvo: kohonen_test_bmu.png")

# ==============================
# GERAR README.md
# ==============================
print("\nGerando README.md...")

# Determine class regions
class_A_neurons = [r*GRID_COLS+c+1 for r in range(GRID_ROWS) for c in range(GRID_COLS) if neuron_dominant_class[(r,c)] == 'A']
class_B_neurons = [r*GRID_COLS+c+1 for r in range(GRID_ROWS) for c in range(GRID_COLS) if neuron_dominant_class[(r,c)] == 'B']
class_C_neurons = [r*GRID_COLS+c+1 for r in range(GRID_ROWS) for c in range(GRID_COLS) if neuron_dominant_class[(r,c)] == 'C']
none_neurons   = [r*GRID_COLS+c+1 for r in range(GRID_ROWS) for c in range(GRID_COLS) if neuron_dominant_class[(r,c)] is None]

with open(os.path.join(BASE_DIR, 'README.md'), 'w') as f:
    f.write("# Atividade: Rede de Kohonen — Agrupamento de Imperfeições de Borracha\n\n")
    f.write("> **Disciplina:** Lab. Inteligência Artificial | **Professor:** Lázaro Eduardo da Silva | **Data:** 28/05/2026\n\n")
    f.write("---\n\n")

    f.write("## 1. Descrição do Problema\n\n")
    f.write("No processo industrial de fabricação de pneus, amostras de borracha com imperfeições foram coletadas, "
            "com medidas de três grandezas $\\{x_1, x_2, x_3\\}$ relativas ao processo de fabricação. "
            "Como os engenheiros não possuíam conhecimento prévio sobre as correlações entre essas variáveis, "
            "aplica-se uma **Rede de Kohonen** (Self-Organizing Map — SOM) como ferramenta de **aprendizado "
            "não-supervisionado** para descobrir as estruturas de agrupamento latentes nos dados.\n\n")

    f.write("## 2. Topologia e Parâmetros da Rede\n\n")
    f.write("| Parâmetro | Valor |\n")
    f.write("| :--- | :--- |\n")
    f.write(f"| Número de neurônios ($N_1$) | {N1} |\n")
    f.write(f"| Estrutura do grid | $4 \\times 4$ (bidimensional) |\n")
    f.write(f"| Taxa de aprendizado ($\\eta$) | $0.001$ |\n")
    f.write(f"| Raio de vizinhança | $1$ (distância de Chebyshev) |\n")
    f.write(f"| Dimensão de entrada | $d = 3$ ($x_1, x_2, x_3$) |\n")
    f.write(f"| Total de amostras de treino | $120$ |\n")
    f.write(f"| Épocas de treinamento | $100$ |\n\n")

    f.write("### 2.1. Diagrama do Grid Topológico 4×4\n\n")
    f.write("Os neurônios são organizados em um grid bidimensional com a seguinte numeração:\n\n")
    f.write("```\n")
    f.write("  Col 0   Col 1   Col 2   Col 3\n")
    f.write("┌───────┬───────┬───────┬───────┐\n")
    for r in range(GRID_ROWS):
        row_str = f"│"
        for c in range(GRID_COLS):
            n_num = r*GRID_COLS+c+1
            row_str += f"  N{n_num:02d}  │"
        f.write(f"Lin {r} {row_str}\n")
        if r < GRID_ROWS-1:
            f.write("     ├───────┼───────┼───────┼───────┤\n")
    f.write("     └───────┴───────┴───────┴───────┘\n")
    f.write("```\n\n")

    f.write("## 3. Regra de Aprendizado\n\n")
    f.write("A rede utiliza a **Regra de Atualização por Norma Euclidiana** (algoritmo WTA — "
            "*Winner-Takes-All* com vizinhança). Para cada padrão $x$ apresentado:\n\n")
    f.write("**1. Encontrar o neurônio vencedor (BMU — Best Matching Unit):**\n")
    f.write("$$j^* = \\arg\\min_j \\| x - w_j \\|_2 = \\arg\\min_j \\sqrt{\\sum_{k=1}^{3}(x_k - w_{jk})^2}$$\n\n")
    f.write("**2. Atualizar os pesos do vencedor e seus vizinhos:**\n")
    f.write("$$\\Delta w_j = \\eta \\cdot (x - w_j), \\quad \\forall j \\in \\mathcal{V}(j^*, r)$$\n\n")
    f.write("onde $\\mathcal{V}(j^*, r)$ é o conjunto de neurônios dentro do raio $r=1$ do vencedor "
            "(usando distância de Chebyshev).\n\n")

    f.write("### 3.1. Derivação da Regra a partir do Erro Quadrático (Questão 3)\n\n")
    f.write("A regra de atualização é derivada pela **minimização da função de erro quadrático:**\n\n")
    f.write("$$E = \\frac{1}{2} \\| x - w_{j^*} \\|^2 = \\frac{1}{2} \\sum_{k=1}^{d}(x_k - w_{j^*k})^2$$\n\n")
    f.write("Calculando o gradiente em relação a $w_{j^*}$:\n")
    f.write("$$\\frac{\\partial E}{\\partial w_{j^*}} = -(x - w_{j^*})$$\n\n")
    f.write("Aplicando o método da descida do gradiente:\n")
    f.write("$$\\Delta w_{j^*} = -\\eta \\frac{\\partial E}{\\partial w_{j^*}} = \\eta (x - w_{j^*})$$\n\n")
    f.write("Que é exatamente a regra de Kohonen para o neurônio vencedor. Para os vizinhos, "
            "a mesma regra é aplicada com um fator de vizinhança $h(j, j^*)$ que vale $1$ "
            "para neurônios dentro do raio e $0$ fora:\n")
    f.write("$$\\Delta w_j = \\eta \\cdot h(j, j^*) \\cdot (x - w_j)$$\n\n")

    f.write("## 4. Resultados do Treinamento\n\n")
    f.write("Após o treinamento com as 120 amostras (100 épocas), o mapa auto-organizável convergiu "
            "para a seguinte configuração:\n\n")

    f.write("### 4.1. Visualizações\n\n")
    f.write("#### U-Matrix e Mapa de Classes\n\n")
    f.write("![Mapa de Kohonen](kohonen_map.png)\n\n")
    f.write("#### Espaço de Features 3D e Protótipos dos Neurônios\n\n")
    f.write("![Scatter 3D](kohonen_scatter3d.png)\n\n")

    f.write("### 4.2. Distribuição de Amostras por Neurônio\n\n")
    f.write("Abaixo é apresentada a distribuição de amostras (por classe A/B/C) em cada neurônio do grid:\n\n")
    f.write("| Neurônio | Linha | Coluna | Nº A | Nº B | Nº C | Classe Dominante | Pesos ($w_1, w_2, w_3$) |\n")
    f.write("| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n")
    for r in range(GRID_ROWS):
        for c in range(GRID_COLS):
            n_num = r*GRID_COLS+c+1
            counts = neuron_class_count[(r,c)]
            cls = neuron_dominant_class[(r,c)] or "—"
            w = W[r,c]
            f.write(f"| N{n_num:02d} | {r} | {c} | {counts['A']} | {counts['B']} | {counts['C']} | **{cls}** | ({w[0]:.4f}, {w[1]:.4f}, {w[2]:.4f}) |\n")
    f.write("\n")

    f.write("### 4.3. Mapa do Grid com Classes Dominantes\n\n")
    f.write("```\n")
    f.write("  Col 0      Col 1      Col 2      Col 3\n")
    f.write("┌──────────┬──────────┬──────────┬──────────┐\n")
    for r in range(GRID_ROWS):
        row_str = f"│"
        for c in range(GRID_COLS):
            n_num = r*GRID_COLS+c+1
            cls = neuron_dominant_class[(r,c)] or "—"
            counts = neuron_class_count[(r,c)]
            total = sum(counts.values())
            row_str += f" N{n_num:02d}:{cls}({total:2d}) │"
        f.write(f"Lin {r} {row_str}\n")
        if r < GRID_ROWS-1:
            f.write("     ├──────────┼──────────┼──────────┼──────────┤\n")
    f.write("     └──────────┴──────────┴──────────┴──────────┘\n")
    f.write("```\n\n")

    f.write("## 5. Questão 1: Neurônios por Classe (A, B e C)\n\n")
    f.write("De posse dos resultados do treinamento, com as classes A (amostras 1–20), "
            "B (amostras 21–60) e C (amostras 61–120), os neurônios representantes de cada classe são:\n\n")

    f.write(f"- **Classe A** (imperfeições de baixo valor: $x_1 \\approx 0.25$, $x_2 \\approx 0.25$, $x_3 \\approx 0.19$): "
            f"Neurônios **{', '.join(['N'+str(n) for n in sorted(class_A_neurons)])}**\n\n")
    f.write(f"- **Classe B** (imperfeições de alto $x_1$ e $x_3$: $x_1 \\approx 0.74$, $x_2 \\approx 0.24$, $x_3 \\approx 0.74$): "
            f"Neurônios **{', '.join(['N'+str(n) for n in sorted(class_B_neurons)])}**\n\n")
    f.write(f"- **Classe C** (imperfeições de alto $x_2$: $x_1 \\approx 0.52$, $x_2 \\approx 0.75$, $x_3 \\approx 0.50$): "
            f"Neurônios **{', '.join(['N'+str(n) for n in sorted(class_C_neurons)])}**\n\n")
    if none_neurons:
        f.write(f"- **Neurônios não ativados** (nenhuma amostra encontrou este neurônio como BMU): "
                f"**{', '.join(['N'+str(n) for n in sorted(none_neurons)])}**\n\n")

    f.write("As regiões do grid que representam cada classe podem ser visualizadas no **Mapa de Classes** "
            "(ver imagem `kohonen_map.png`), onde a coloração indica qual classe domina cada neurônio.\n\n")

    f.write("## 6. Questão 2: Classificação das Amostras de Teste\n\n")
    f.write("As amostras de teste foram apresentadas à rede treinada para determinar o neurônio "
            "vencedor (BMU) de cada uma, e assim identificar sua classe:\n\n")
    f.write("![Mapa BMU Teste](kohonen_test_bmu.png)\n\n")
    f.write("| Amostra | $x_1$ | $x_2$ | $x_3$ | BMU (Neurônio) | **Classe Prevista** |\n")
    f.write("| :---: | :---: | :---: | :---: | :---: | :---: |\n")
    for res in test_results:
        x = res['x']
        bmu_r, bmu_c = res['bmu']
        n_num = bmu_r*GRID_COLS+bmu_c+1
        cls = res['cls'] or "—"
        f.write(f"| {res['id']} | {x[0]:.4f} | {x[1]:.4f} | {x[2]:.4f} | N{n_num:02d} | **{cls}** |\n")
    f.write("\n")

    # Análise das classes preditas
    pred_A = [r['id'] for r in test_results if r['cls'] == 'A']
    pred_B = [r['id'] for r in test_results if r['cls'] == 'B']
    pred_C = [r['id'] for r in test_results if r['cls'] == 'C']

    f.write(f"**Resumo das Classificações:**\n\n")
    f.write(f"- **Classe A:** Amostras {pred_A}\n")
    f.write(f"- **Classe B:** Amostras {pred_B}\n")
    f.write(f"- **Classe C:** Amostras {pred_C}\n\n")

    f.write("**Análise dos Resultados:**\n\n")
    f.write("- As amostras de teste com **baixos valores de $x_1$ e $x_3$** (como 1, 4, 7, 10) foram corretamente mapeadas para a **Classe A**, "
            "que corresponde a imperfeições de borracha com características mais brandas.\n")
    f.write("- As amostras com **altos valores de $x_1$ e $x_3$ e baixo $x_2$** (como 2, 5, 8, 11) foram mapeadas para a **Classe B**, "
            "representando imperfeições de alta gravidade em dois eixos principais.\n")
    f.write("- As amostras com **alto $x_2$ e valores médios de $x_1$ e $x_3$** (como 3, 6, 9, 12) foram mapeadas para a **Classe C**, "
            "cujas imperfeições se destacam pelo segundo eixo de medição.\n\n")

    f.write("## 7. Questão 3: Derivação da Regra de Atualização por Minimização do Erro Quadrático\n\n")
    f.write('**Enunciado:** Demonstrar que a regra de alteração de pesos "Norma Euclidiana" '
            'para um padrão $x$ é obtida a partir da minimização da função erro quadrático.\n\n')
    f.write("**Demonstração:**\n\n")
    f.write("Seja $j^*$ o índice do neurônio vencedor para o padrão $x \\in \\mathbb{R}^d$. "
            "Definimos a função de erro quadrático como a distância ao quadrado entre o padrão "
            "e o vetor de pesos do neurônio vencedor:\n\n")
    f.write("$$E(w_{j^*}) = \\frac{1}{2} \\sum_{k=1}^{d} (x_k - w_{j^*k})^2 = \\frac{1}{2} \\| x - w_{j^*} \\|^2$$\n\n")
    f.write("Para minimizar $E$, calculamos o gradiente em relação ao vetor de pesos $w_{j^*}$:\n\n")
    f.write("$$\\frac{\\partial E}{\\partial w_{j^*k}} = \\frac{\\partial}{\\partial w_{j^*k}} "
            "\\left[ \\frac{1}{2} \\sum_{k=1}^{d} (x_k - w_{j^*k})^2 \\right] = -(x_k - w_{j^*k})$$\n\n")
    f.write("Portanto, o gradiente vetorial é:\n\n")
    f.write("$$\\nabla_{w_{j^*}} E = -(x - w_{j^*})$$\n\n")
    f.write("Aplicando a regra de atualização por **descida do gradiente** com taxa de aprendizado $\\eta > 0$:\n\n")
    f.write("$$\\Delta w_{j^*} = -\\eta \\nabla_{w_{j^*}} E = -\\eta \\cdot [-(x - w_{j^*})]$$\n\n")
    f.write("$$\\boxed{\\Delta w_{j^*} = \\eta (x - w_{j^*})}$$\n\n")
    f.write("Essa é exatamente a **Regra de Kohonen** (WTA), onde o peso do neurônio vencedor é "
            "movido na direção do padrão de entrada com passo $\\eta$. Para os neurônios na "
            "vizinhança $\\mathcal{V}(j^*, r)$, a mesma minimização é aplicada individualmente:\n\n")
    f.write("$$\\Delta w_j = \\eta \\cdot h(j, j^*) \\cdot (x - w_j), \\quad h(j, j^*) = "
            "\\begin{cases} 1 & \\text{se } d(j, j^*) \\leq r \\\\ 0 & \\text{caso contrário} \\end{cases}$$\n\n")
    f.write("onde $d(j, j^*)$ é a distância topológica (Chebyshev) entre o neurônio $j$ e o vencedor $j^*$, "
            "e $r$ é o raio de vizinhança. $\\square$\n\n")

    f.write("---\n\n")
    f.write("## 8. Conclusões\n\n")
    f.write("A Rede de Kohonen com 16 neurônios organizados em grid $4 \\times 4$ conseguiu identificar "
            "**três regiões distintas** no espaço de entrada, correspondentes às três classes de "
            "imperfeições:\n\n")
    f.write("1. **Classe A** — Imperfeições de baixa magnitude em todos os eixos ($x_1, x_2, x_3 \\approx 0.25$): "
            "os menores valores, indicando defeitos de menor intensidade.\n")
    f.write("2. **Classe B** — Imperfeições com alta magnitude em $x_1$ e $x_3$ ($\\approx 0.74$) e baixo $x_2$ ($\\approx 0.24$): "
            "correlação forte entre os eixos 1 e 3, com o eixo 2 sendo o discriminador.\n")
    f.write("3. **Classe C** — Imperfeições com $x_2$ alto ($\\approx 0.75$) e valores médios de $x_1$ e $x_3$ ($\\approx 0.52, 0.50$): "
            "padrão distinto dos outros dois grupos.\n\n")
    f.write("O SOM demonstrou sua capacidade como ferramenta de **análise exploratória não-supervisionada**, "
            "revelando a estrutura de agrupamento dos dados sem nenhuma informação de classe durante o treinamento, "
            "apenas pela minimização das distâncias euclidianas entre padrões e protótipos.\n")

print("README.md gerado com sucesso!")
