

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Datos directamente en el código


datos_produccion = [
    {"turno": "mañana", "cantidad_producida": 120, "defectos": 3, "tiempo_produccion": 5.2},
    {"turno": "tarde", "cantidad_producida": 100, "defectos": 5, "tiempo_produccion": 6.1},
    {"turno": "noche", "cantidad_producida": 80, "defectos": 8, "tiempo_produccion": 7.3},
    {"turno": "mañana", "cantidad_producida": 130, "defectos": 2, "tiempo_produccion": 4.8},
    {"turno": "tarde", "cantidad_producida": 105, "defectos": 4, "tiempo_produccion": 5.9},
    {"turno": "noche", "cantidad_producida": 95, "defectos": 6, "tiempo_produccion": 6.8},
    {"turno": "mañana", "cantidad_producida": 125, "defectos": 3, "tiempo_produccion": 5.0},
    {"turno": "tarde", "cantidad_producida": 98, "defectos": 5, "tiempo_produccion": 6.0},
    {"turno": "noche", "cantidad_producida": 90, "defectos": 7, "tiempo_produccion": 7.1}
]

# Convertir datos a DataFrame
df = pd.DataFrame(datos_produccion)


# Análisis estadístico


print("\n📋 Primeras filas del dataset:")
print(df.head())

print("\n📊 Estadísticas generales:")
print(df.describe())


# Visualizaciones


# Histograma de producción
plt.figure()
plt.hist(df["cantidad_producida"], bins=5, edgecolor="black")
plt.title("Histograma: Cantidad Producida")
plt.xlabel("Cantidad")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# Boxplot de defectos por turno
plt.figure()
sns.boxplot(x="turno", y="defectos", data=df)
plt.title("Boxplot: Defectos por Turno")
plt.xlabel("Turno")
plt.ylabel("Cantidad de Defectos")
plt.show()

# Scatter plot: Tiempo vs Defectos
plt.figure()
plt.scatter(df["tiempo_produccion"], df["defectos"], color="red")
plt.title("Relación entre Tiempo de Producción y Defectos")
plt.xlabel("Tiempo de Producción (horas)")
plt.ylabel("Defectos")
plt.grid(True)
plt.show()

# Correlaciones
correlacion = df.corr(numeric_only=True)
print("\n🧠 Matriz de correlación:")
print(correlacion)

plt.figure()
sns.heatmap(correlacion, annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()


# Análisis por turno


prom_defectos = df.groupby("turno")["defectos"].mean()
print("\n🔍 Promedio de defectos por turno:")
print(prom_defectos)

# Gráfico de barras
prom_defectos.plot(kind='bar', title="Promedio de Defectos por Turno", ylabel="Defectos Promedio", xlabel="Turno", color="orange")
plt.grid(axis='y')
plt.show()
