# Documentación de Datos [Topological Data Analysis of Macroeconomics variables in Colombian Economy]

## Variables y Bases de Datos usadas


### Índice de Precios al Consumidor (IPC)
El IPC es el indicador que mide la variación promedio en los precios de una canasta representativa de bienes y servicios consumidos por los hogares colombianos. Es la principal medida de inflación en el país y un insumo fundamental para la política monetaria.

- **Medida:** Variación porcentual mensual (%), base diciembre de 2018 = 100.  
- **Fuente:** DANE (Departamento Administrativo Nacional de Estadística).  
- **Frecuencia:** Mensual.  
- **Rango Temporal:** Enero 2003 – Julio 2025 (última actualización: 8 de agosto de 2025).  
- **Relevancia:**  
  - Variable central en la política monetaria del Banco de la República.  
  - Captura cambios en el poder adquisitivo de los hogares.  
  - Permite identificar episodios de inflación alta y periodos de estabilidad.  
  - Su inclusión en TDA aporta sensibilidad a choques de corto plazo y estabilidad de precios.  
- **Conjetura:**  
  - Cambios abruptos en la topología del dataset pueden coincidir con picos inflacionarios o procesos de desinflación rápida.  
  - La interacción topológica entre IPC y otras variables podría revelar estructuras persistentes que anteceden fases de recesión o expansión.  


### Tasa de Cambio Representativa del Mercado (TRM)
La TRM es el valor promedio ponderado de las tasas de cambio de compra y venta de dólares de los Estados Unidos con respecto al peso colombiano, calculado diariamente con base en las operaciones del mercado cambiario. Es publicada por la Superintendencia Financiera de Colombia y constituye el indicador oficial de referencia para transacciones y obligaciones en moneda extranjera.

- **Medida:** Pesos colombianos (COP) por dólar estadounidense (USD).  
- **Fuente:** Superintendencia Financiera de Colombia.  
- **Frecuencia:** Diario (con vigencias de uno o varios días, dependiendo de la resolución).  
- **Rango Temporal:** Actualmente disponible con registros históricos desde 1967.  
- **Relevancia:**  
  - Determina el precio oficial del dólar en la economía colombiana.  
  - Afecta variables como importaciones, exportaciones, inflación y deuda externa.  
  - Su volatilidad puede reflejar presiones macroeconómicas y choques externos.  
  - En el TDA, aporta sensibilidad a choques cambiarios y puede revelar patrones asociados a fases de devaluación o apreciación prolongadas.  
- **Conjetura:**  
  - La topología de la TRM puede mostrar cambios estructurales vinculados con crisis financieras, choques externos (ej. precios del petróleo) o políticas cambiarias.  
  - Interacciones topológicas entre la TRM y el IPC podrían anticipar episodios de traspaso inflacionario (pass-through) del tipo de cambio hacia los precios internos.  

---

## Ajustes y transformaciones aplicados 


### Índice de Precios al Consumidor (IPC)
Para usar el IPC en conjunto con otras variables dentro del análisis topológico, será necesario realizar ciertos ajustes:

- **Normalización (z-score):**  
  Centra la serie en 0 y la escala con desviación estándar 1.  
  - *Motivo:* cada variable está en magnitudes diferentes (PIB en billones, IPC en %, TRM en COP/USD). El z-score evita que la variable con mayor escala domine la distancia en el espacio métrico.  

- **Ajuste estacional (STL o X-13ARIMA):**  
  Elimina patrones de calendario recurrentes (ej. subidas típicas en enero y diciembre).  
  - *Motivo:* sin este ajuste, el TDA podría detectar “ciclos” artificiales que solo corresponden a estacionalidad, no a cambios estructurales en la economía.  

- **Conversión a frecuencia trimestral:**  
  Se resume la serie mensual en trimestres, usando el promedio o acumulado de las variaciones mensuales, o alguna otra técnica de ajuste.  
  - *Motivo:* permite homogenizar la frecuencia de todos los indicadores y analizar estructuras comunes en ventanas temporales comparables.  

- **Ajuste de Rango:**  
  Se utilizan los datos desde enero de 2003 hasta enero de 2025.  
  - *Motivo:* Definir un rango temporal homogéneo que abarque series completas de años, lo cual facilita el cálculo de variaciones anuales, comparaciones históricas y análisis de tendencias de largo plazo. Además, este ajuste garantiza consistencia en la base de datos al evitar cortes incompletos de periodos.  

- **Cambio de formato (wide → tidy):**  
  La tabla original está organizada en formato “wide”, con los años como columnas y los meses como filas. Para el análisis se transforma al formato “tidy”, donde cada observación corresponde a una fecha (`YYYY-MM`) y un valor del IPC.  
  - *Motivo:* el formato tidy es el estándar en ciencia de datos, facilita operaciones como filtrado, resampleo, fusión con otras variables y preparación de matrices multidimensionales para análisis topológico.


### Tasa de Cambio Representativa del Mercado (TRM)
Para integrar la TRM con otras variables macroeconómicas dentro del análisis topológico, se aplican los siguientes ajustes:

- **Normalización (z-score):**  
  Convierte la serie de valores COP/USD en media 0 y desviación estándar 1.  
  - *Motivo:* evita que la escala numérica de la TRM (miles de pesos) domine sobre otras variables expresadas en porcentajes u órdenes de magnitud distintos (ej. IPC).  

- **Resampleo temporal (mensual o trimestral):**  
  A partir de la serie diaria se generan series de menor frecuencia utilizando estadísticas representativas (mediana, promedio o valor de cierre).  
  - *Motivo:* homogeneizar la frecuencia con el IPC y el resto de variables, reduciendo ruido de alta frecuencia y capturando la tendencia central del tipo de cambio.  

- **Ajuste de Rango Temporal:**  
  Se utilizarán datos desde enero de 2003 hasta enero de 2025, en consistencia con el IPC y el resto de la base macroeconómica.  
  - *Motivo:* garantizar comparabilidad entre todas las variables en un periodo de estudio uniforme y suficientemente amplio para capturar diferentes fases del ciclo económico.  

- **Transformación de formato (wide → tidy):**  
  La fuente original presenta intervalos de vigencia (`VIGENCIADESDE` y `VIGENCIAHASTA`). Estos se expanden en una serie diaria continua y luego se reorganizan en formato tidy, donde cada fila corresponde a una fecha (`YYYY-MM-DD`) con un valor único de TRM. Posteriormente, la serie se convierte a frecuencia mensual, tomando la mediana de los valores diarios de cada mes (`YYYY-MM`).  
  - *Motivo:* el formato tidy permite un manejo más flexible de los datos. A su vez, el uso de la mediana mensual homogeniza la frecuencia con otras bases de datos.

---


## Base de datos central

