#Projeto Ceu Profundo 2023
#Wandeclayt Melo/@ceuprofundo
#GPL 2.0

import matplotlib.pyplot as plt

# Configurar figura com tamanho de 15cm por 15cm
fig, ax = plt.subplots(figsize=(15, 15))

# Configurar escala log-log
ax.set_xscale('log')
ax.set_yscale('log')

# Configurar intervalo dos eixos
ax.set_xlim(10**-1, 10**3)
ax.set_ylim(10**-1, 10**3)

# Adicionar título ao gráfico
ax.set_title('@ceuprofundo - Leis de Kepler', fontsize=12)

# Configurar rótulos dos eixos
ax.set_xlabel('Distância Média')
ax.set_ylabel('Período Orbital')

# Ativar as linhas de grade
ax.grid(True, which='both', linestyle='dashed')

# Configurar relação de aspecto 1:1
ax.set_aspect('equal')

# Configurar os marcadores dos eixos
ax.tick_params(bottom=True, top=False, left=False, right=False)

# Configurar as bordas
ax.spines['top'].set_linestyle('-')
ax.spines['bottom'].set_linestyle('-')
ax.spines['left'].set_linestyle('-')
ax.spines['right'].set_linestyle('-')

# Salvar o gráfico em um arquivo PDF
plt.savefig('log_log_grid.pdf', format='pdf')

# Exibir o gráfico
plt.show()
