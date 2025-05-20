"""
Global Cybersecurity Threats (2015-2024)
Autor: [Cristopher Mardones]
GitHub: [https://github.com/Shadowcrys]
Fuente: [https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024?resource=download]
"""
import pandas as pd
import matplotlib.pyplot as plt

# Configuración inicial
plt.style.use('ggplot')  # Estilo profesional pero simple
pd.set_option('display.float_format', '{:,.2f}'.format)

# 1. Cargar datos
try:
    df = pd.read_csv('Global_Cybersecurity_Threats_2015-2024.csv')
    print("✅ Datos cargados correctamente")
except Exception as e:
    print(f"❌ Error al cargar datos: {e}")
    exit()

# 2. Análisis Exploratorio
print("\n🔍 ESTADÍSTICAS CLAVE:")
print(df[['Financial Loss (in Million $)', 
          'Number of Affected Users', 
          'Incident Resolution Time (in Hours)']].describe())

print("\n🌎 TOP 5 PAÍSES:")
print(df['Country'].value_counts().head(5))

print("\n⚡ TOP 3 ATAQUES:")
print(df['Attack Type'].value_counts().head(3))

# 3. Visualizaciones (Versión Mejorada)
def guardar_grafico(fig, nombre):
    """Guarda gráficos en la carpeta /graficos"""
    fig.tight_layout()
    fig.savefig(f'graficos/{nombre}.png', dpi=120)
    plt.close()

# Gráfico 1: Países con más ataques
plt.figure(figsize=(10, 5))
top_paises = df['Country'].value_counts().head(5).sort_values()
top_paises.plot(kind='barh', color=['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6'])
plt.title('Top 5 Países Más Afectados (2015-2024)', pad=15)
plt.xlabel('Número de Ataques')
guardar_grafico(plt.gcf(), 'top_paises')

# Gráfico 2: Evolución temporal
plt.figure(figsize=(10, 5))
df.groupby('Year')['Financial Loss (in Million $)'].mean().plot(
    marker='o', 
    color='#e74c3c',
    linewidth=2
)
plt.title('Pérdidas Financieras Promedio por Año', pad=15)
plt.ylabel('Millones de USD')
plt.grid(True, linestyle='--', alpha=0.6)
guardar_grafico(plt.gcf(), 'perdidas_anuales')

print("\n📊 Gráficos guardados en /graficos")

# Gráfico 3: Pie chart de tipos de ataque (¡NUEVO MEJORADO!)
plt.figure(figsize=(10, 8))
attack_counts = df['Attack Type'].value_counts().head(5)

# Personalización avanzada
explode = (0.05, 0, 0, 0, 0)  # Destacar el primer segmento
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
wedges, texts, autotexts = plt.pie(
    attack_counts,
    labels=attack_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    shadow=True,
    textprops={'fontsize': 11}
)

# Mejorar legibilidad
plt.setp(autotexts, size=11, weight="bold")
plt.title('Distribución de Tipos de Ataque', pad=20, fontsize=14)
plt.axis('equal')  # Para que sea un círculo perfecto
guardar_grafico(plt.gcf(), 'tipos_ataque_pie')


# 5. Análisis Exploratorio (consola)
print("\n🔍 ESTADÍSTICAS CLAVE:")
print(df[['Financial Loss (in Million $)', 
          'Number of Affected Users', 
          'Incident Resolution Time (in Hours)']].describe())

print("\n🌎 TOP 5 PAÍSES:")
print(df['Country'].value_counts().head(5))

print("\n⚡ TOP 5 TIPOS DE ATAQUE:")
print(attack_counts)  # Ya calculado para el pie chart