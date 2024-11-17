import random

bandeja = [6] * 100

print("Bandeja inicial:")
for i in range(0, len(bandeja), 10):
    print(f"{bandeja[i:i+10]}")

print()

soma = sum(bandeja)
print(f"Soma inicial: {soma}\n")

for balanco in range(1, 51):
    num_dados_para_girar = int(len(bandeja) * 0.05)

    for _ in range(num_dados_para_girar):
        indice = random.randint(0, len(bandeja) - 1)
        bandeja[indice] = random.randint(1, 6)

    soma = sum(bandeja)
    print(f"{soma}")

print("\nBandeja final:")
for i in range(0, len(bandeja), 10):
    print(f"{bandeja[i:i+10]}")

print(f"\nSoma final: {sum(bandeja)}")
