import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importar los datos
df = pd.read_csv("medical_examination.csv")

# Agregar una columna 'overweight'
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# Normalizar los datos (0 es bueno, 1 es malo)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Función para dibujar la gráfica categórica
def draw_cat_plot():
    # Crear DataFrame para catplot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Agrupar y contar los datos
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Dibujar el gráfico categórico
    fig = sns.catplot(
        x='variable', y='total', hue='value', col='cardio',
        data=df_cat, kind='bar', height=5, aspect=1
    ).fig

    return fig

# Función para dibujar el mapa de calor
def draw_heat_map():
    # Limpiar los datos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcular la matriz de correlación
    corr = df_heat.corr()

    # Generar una máscara para el triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configurar la figura de matplotlib
    fig, ax = plt.subplots(figsize=(12, 12))

    # Dibujar el mapa de calor
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".1f", center=0,
        square=True, linewidths=0.5, cbar_kws={"shrink": 0.5}
    )

    # 16
    fig.savefig('heatmap.png')
    return fig
