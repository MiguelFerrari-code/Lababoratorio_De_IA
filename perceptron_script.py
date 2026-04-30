import random

train_data_raw = [
    [1, -0.6508, 0.1097, 4.0009, -1.0],
    [2, -1.4492, 0.8896, 4.4005, -1.0],
    [3, 2.0850, 0.6876, 12.0710, -1.0],
    [4, 0.2626, 1.1476, 7.7985, 1.0],
    [5, 0.6418, 1.0234, 7.0427, 1.0],
    [6, 0.2569, 0.6730, 8.3265, -1.0],
    [7, 1.1155, 0.6043, 7.4446, 1.0],
    [8, 0.0914, 0.3399, 7.0677, -1.0],
    [9, 0.0121, 0.5256, 4.6316, 1.0],
    [10, -0.0429, 0.4660, 5.4323, 1.0],
    [11, 0.4340, 0.6870, 8.2287, -1.0],
    [12, 0.2735, 1.0287, 7.1934, 1.0],
    [13, 0.4839, 0.4851, 7.4850, -1.0],
    [14, 0.4089, -0.1267, 5.5019, -1.0],
    [15, 1.4391, 0.1614, 8.5843, -1.0],
    [16, -0.9115, -0.1973, 2.1962, -1.0],
    [17, 0.3654, 1.0475, 7.4858, 1.0],
    [18, 0.2144, 0.7515, 7.1699, 1.0],
    [19, 0.2013, 1.0014, 6.5489, 1.0],
    [20, 0.6483, 0.2183, 5.8991, 1.0],
    [21, -0.1147, 0.2242, 7.2435, -1.0],
    [22, -0.7970, 0.8795, 3.8762, 1.0],
    [23, -1.0625, 0.6366, 2.4707, 1.0],
    [24, 0.5307, 0.1285, 5.6883, 1.0],
    [25, -1.2200, 0.7777, 1.7252, 1.0],
    [26, 0.3957, 0.1076, 5.6623, -1.0],
    [27, -0.1013, 0.5989, 7.1812, -1.0],
    [28, 2.4482, 0.9455, 11.2095, 1.0],
    [29, 2.0149, 0.6192, 10.9263, -1.0],
    [30, 0.2012, 0.2611, 5.4631, 1.0]
]

test_data_raw = [
    [1, -0.3565, 0.0620, 5.9891],
    [2, -0.7842, 1.1267, 5.5912],
    [3, 0.3012, 0.5611, 5.8234],
    [4, 0.7757, 1.0648, 8.0677],
    [5, 0.1570, 0.8028, 6.3040],
    [6, -0.7014, 1.0316, 3.6005],
    [7, 0.3748, 0.1536, 6.1537],
    [8, -0.6920, 0.9404, 4.4058],
    [9, -1.3970, 0.7141, 4.9263],
    [10, -1.8842, -0.2805, 1.2548]
]

def activation(v):
    return 1 if v >= 0 else -1

eta = 0.01
num_trainings = 5

train_results = []
models = []

for t in range(num_trainings):
    random.seed(t * 100 + 42) # Different seed for each run
    w = [random.uniform(0, 1) for _ in range(4)]
    initial_w = list(w)
    epochs = 0
    
    while True:
        error_count = 0
        for sample in train_data_raw:
            x = [-1, sample[1], sample[2], sample[3]]
            d = sample[4]
            
            v = sum(w[i] * x[i] for i in range(4))
            y = activation(v)
            
            if y != d:
                error_count += 1
                for i in range(4):
                    w[i] = w[i] + eta * (d - y) * x[i]
        
        epochs += 1
        if error_count == 0:
            break
        if epochs > 10000:
            print(f"Run {t+1} did not converge!")
            break
            
    train_results.append({
        "initial_w": initial_w,
        "final_w": list(w),
        "epochs": epochs
    })
    models.append(list(w))

print("=== Training Results ===")
for i, res in enumerate(train_results):
    print(f"T{i+1}:")
    print(f"Initial: {res['initial_w']}")
    print(f"Final:   {res['final_w']}")
    print(f"Epochs:  {res['epochs']}\n")

print("=== Classification Results ===")
classifications = []
for sample in test_data_raw:
    x = [-1, sample[1], sample[2], sample[3]]
    outputs = []
    for w in models:
        v = sum(w[i] * x[i] for i in range(4))
        y = activation(v)
        outputs.append(y)
    classifications.append(outputs)
    print(f"Sample {sample[0]}: {outputs}")

import json
with open('results.json', 'w') as f:
    json.dump({'train': train_results, 'test': classifications}, f)
