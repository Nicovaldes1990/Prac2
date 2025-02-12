import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Cargar los datos
    data = pd.read_csv('epa-sea-level.csv')

    # Crear el gráfico de dispersión
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Calcular la línea de mejor ajuste usando todos los datos (desde 1880 hasta el último año)
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Dibujar la línea de mejor ajuste (usando datos desde 1880 hasta el último año)
    years_extended = range(1880, 2051)
    plt.plot(years_extended, [slope * year + intercept for year in years_extended], label='Ajuste hasta 2050')

    # Filtrar los datos desde el año 2000 en adelante para una segunda línea de ajuste
    data_from_2000 = data[data['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(data_from_2000['Year'], data_from_2000['CSIRO Adjusted Sea Level'])

    # Dibujar la segunda línea de mejor ajuste (solo desde 2000 hasta 2050)
    years_from_2000 = range(2000, 2051)  # Aseguramos que solo sean 51 puntos
    plt.plot(years_from_2000, [slope2 * year + intercept2 for year in years_from_2000], label='Ajuste desde 2000')

    # Configuración del gráfico
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Guardar y mostrar el gráfico
    plt.savefig('sea_level_plot.png')
    plt.show()

    # Retornar el objeto de la gráfica para las pruebas
    return plt.gca()

# Llamar a la función para ejecutar el código
draw_plot()
