# Primeiro programa Python para testar o ambiente
import numpy as np
import matplotlib.pyplot as plt

# Criando alguns dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Criando um gráfico simples
plt.figure(figsize=(8, 4))
plt.plot(x, y, 'b-', linewidth=2, label='sen(x)')
plt.title('Meu Primeiro Gráfico Python')
plt.xlabel('x')
plt.ylabel('sen(x)')
plt.grid(True)
plt.legend()
plt.savefig('meu_grafico.png')  # Salva o gráfico como imagem
plt.show()  # Exibe o gráfico

print("Ambiente Python configurado com sucesso!")