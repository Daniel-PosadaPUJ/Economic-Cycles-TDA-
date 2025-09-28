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

---

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
  - Interacciones topológicas entre la otras variables podrían anticipar episodios de traspaso inflacionario (pass-through) del tipo de cambio hacia los precios internos.  

---

### Precio Histórico del Petróleo Brent
El precio del petróleo Brent es uno de los principales referentes internacionales para la cotización del crudo. Representa la mezcla de petróleo extraído del Mar del Norte y es utilizado como benchmark global para la determinación de precios de contratos energéticos, insumo clave en costos de transporte, producción industrial y decisiones de política económica en países exportadores e importadores de crudo.

- **Medida:** Precio nominal de cierre en dólares por barril (USD/bbl).  
- **Fuente:** Investing.com.  
- **Frecuencia:** Mensual.  
- **Rango Temporal:** Enero 2003 – Enero 2025. 
- **Relevancia:**  
  - Determina costos de importación energética para Colombia y afecta balanza de pagos.  
  - Alta correlación con inflación (vía precios de combustibles y transporte) y con ingresos fiscales de países exportadores.  
  - Refleja choques externos que pueden generar inestabilidad macroeconómica.  
  - En TDA aporta una dimensión ligada a choques globales de oferta y demanda energética, cuya persistencia puede alterar la topología del espacio económico.  
- **Conjetura:**  
  - Cambios abruptos en la topología de los datos podrían coincidir con episodios de alta volatilidad del crudo (caídas >10% o picos especulativos).  
  - Su interacción con otras variables puede generar ciclos persistentes que anticipen presiones inflacionarias o depreciaciones cambiarias.  

--- 

### Precio Histórico del COLCAP
El COLCAP es el índice de referencia del mercado accionario colombiano, que refleja el desempeño de las acciones más líquidas y representativas de la Bolsa de Valores de Colombia (BVC). Se utiliza como indicador del comportamiento general del mercado bursátil colombiano y sirve como benchmark para inversiones y análisis económico-financiero.

- **Medida:** Valor del índice en puntos (representa el desempeño relativo del mercado accionario colombiano, basado en la ponderación de las acciones más líquidas).
- **Fuente:** Bolsa de Valores de Colombia (BVC).  
- **Frecuencia:** Mensual.  
- **Rango Temporal:** Febrero 2008 – Julio 2025 (disponible desde la creación del índice en febrero de 2008).  
- **Relevancia:**  
  - Refleja la evolución del mercado accionario colombiano y la confianza de los inversionistas.  
  - Se utiliza como indicador de riesgo y crecimiento económico, dado que incorpora las empresas más relevantes y líquidas del país.  
  - Su comportamiento anticipa cambios en la inversión y puede correlacionarse con indicadores macroeconómicos como PIB, inflación y tasas de interés.  
  - En TDA aporta información sobre la dinámica del mercado financiero y posibles ciclos económicos, generando estructuras persistentes en el espacio de estados.  
- **Conjetura:**  
  - Cambios abruptos en la topología del índice podrían coincidir con crisis financieras, picos de volatilidad o correcciones bursátiles.  
  - La interacción topológica con otras variables macroeconómicas podría revelar patrones anticipatorios de expansión o contracción económica.  

---

### Registro Estadístico de Relaciones Laborales (RELAB)

El **Registro Estadístico de Relaciones Laborales (RELAB)** es un sistema de información construido por el **DANE** a partir de registros administrativos de la Planilla Integrada de Liquidación de Aportes (PILA). Su propósito es medir la **dinámica del empleo formal en Colombia**, tanto dependiente como independiente, con un alto nivel de desagregación por sector económico, tamaño del aportante y condición de comercio exterior.  

Este sistema constituye una de las fuentes más completas para analizar la estructura del mercado laboral formal, pues combina dimensiones de trabajadores y empleadores, diferenciando la naturaleza de la relación laboral y el sector en el que ocurre.  

- **Medida general:** Número de relaciones laborales (dependientes o independientes) y número de aportantes al sistema de seguridad social.  
- **Fuente:** DANE – Registro Estadístico de Relaciones Laborales (RELAB).  
- **Frecuencia:** Mensual.  
- **Rango Temporal:** Enero 2019 - Mayo 2025.   
- **Relevancia:**  
  - Permite caracterizar la evolución del **empleo formal** en Colombia.  
  - Identifica diferencias entre **relaciones laborales dependientes** e **independientes**, así como la relevancia del sector público, privado y externo.  
  - Constituye un insumo clave para evaluar la **dinámica empresarial y laboral**, así como los efectos de choques económicos sobre la generación de empleo.  
  - En **TDA (Análisis Topológico de Datos)**, RELAB permite explorar **patrones persistentes** y **anomalías** en la estructura del mercado laboral colombiano.  
- **Conjetura:**  
  - Cambios abruptos en la topología del RELAB podrían reflejar crisis sectoriales, choques externos (ej. caída exportadora) o reformas regulatorias.  
  - La interacción del RELAB con PIB sectorial, comercio exterior y variables financieras puede revelar **sincronización de ciclos económicos** y rigideces estructurales del mercado laboral.  


### Sub-bases seleccionadas del RELAB

#### 1. Relaciones laborales dependientes e independientes  
- **Descripción:** Contiene el número total de relaciones laborales clasificadas en dependientes e independientes.  
- **Utilidad:** Permite analizar la composición general del mercado laboral formal y la dinámica de sustitución o complementariedad entre empleo asalariado e independiente.  
- **Potencial en TDA:** ayuda a detectar ciclos de formalización o precarización laboral, y cambios de topología asociados a crisis económicas.  

#### 2. Relaciones laborales dependientes sector público - privado  
- **Descripción:** Desagrega las relaciones laborales dependientes según pertenezcan al sector público o al sector privado.  
- **Utilidad:** Permite comparar la resiliencia del empleo público frente al privado en diferentes coyunturas.  
- **Potencial en TDA:** revela estructuras persistentes en la estabilidad del sector público y mayor volatilidad en el privado.  

#### 3. Relaciones laborales dependientes por sector económico  
- **Descripción:** Presenta la distribución del empleo dependiente por ramas de actividad económica.  
- **Utilidad:** Identifica sectores líderes en creación de empleo formal y los más vulnerables a choques.  
- **Potencial en TDA:** facilita mapear la persistencia topológica de ciertos sectores y los cambios de configuración en crisis sectoriales.  

#### 4. Relaciones laborales aportantes con RL dependientes  
- **Descripción:** Registra el número de empleadores (aportantes) que las generan y el tamaño de su empresa.  
- **Utilidad:** Mide concentración o atomización empresarial en la creación de empleo formal.  
- **Potencial en TDA:** puede detectar anomalías como alta concentración en pocos aportantes o pérdida de aportantes en periodos de crisis.  

---

<!--
### Índice de Producción Industrial (IPI) – Variación y Contribución  
El **IPI** mide los cambios en la producción de la industria colombiana, incluyendo sectores como minería, manufacturas, energía y agua. Se presenta en dos dimensiones:  
- **Variación (%)**: cuánto cambia la producción.  
- **Contribución (p.p)**: cuánto aporta cada sector a la variación total.  

El DANE publica este índice bajo distintas perspectivas de comparación:  
- **Anual:** compara un mes con el mismo mes del año anterior, capturando efectos coyunturales.  
- **Año corrido:** compara el acumulado enero–mes actual frente al mismo periodo del año anterior, mostrando la tendencia en el año en curso.  

- **Medida:** Variación porcentual (%) y contribución en puntos porcentuales (p.p).  
- **Fuente:** DANE.  
- **Frecuencia:** Mensual.  
- **Rango Temporal:** Febrero 2018 - Junio 2025 (Base estadística 2018=100).  
- **Relevancia:** permite analizar la dinámica industrial en el corto y mediano plazo, identificar sectores impulsores o rezagados y relacionar la actividad productiva con indicadores macroeconómicos como el PIB, empleo o exportaciones.  

---
-->

### Índice de Seguimiento a la Economía (ISE)  
El **ISE** es un indicador mensual que mide la evolución de la economía colombiana, funcionando como un proxy del PIB. Se construye a partir de 12 agrupaciones sectoriales definidas según la **CIIU Rev. 4 A.C.** y se publica con año base **2015=100**. Su objetivo es ofrecer una lectura rápida de la coyuntura económica, anticipando la dinámica que luego se confirma en el PIB trimestral.  

El DANE entrega tres versiones, en este caso usaremos:   
- **Datos ajustados por estacionalidad y calendario:** eliminan efectos de estacionalidad y festivos, recomendados para comparaciones intermensuales.  

El ISE se presenta en distintas medidas de variación, usaremos:  
- **Mensual:** compara un mes con el mismo del año anterior.  

- **Medida:** Índice (base 2015=100) y variaciones (%).  
- **Fuente:** DANE.  
- **Frecuencia:** Mensual.  
- **Rango Temporal:** 2005 – 2025pr (junio).  
- **Relevancia:** permite anticipar la evolución del PIB y evaluar el desempeño sectorial de manera oportuna, siendo clave para análisis macroeconómico y de coyuntura.  



---


### Producto Interno Bruto (PIB) – Enfoque Producción  
El **PIB por producción** mide el valor agregado generado por las distintas ramas de actividad económica, siguiendo la clasificación **CIIU Rev. 4 A.C.**. Se publica en **series encadenadas de volumen con año base 2015**, lo que permite comparar en términos reales, eliminando el efecto de los precios.  

El DANE entrega varias versiones:  
- **Datos originales:** con estacionalidad.  
- **Datos ajustados por estacionalidad y calendario:** eliminan efectos estacionales y de festivos, recomendados para análisis de corto plazo y ciclos económicos.  

Para este proyecto usaremos:  
- **Datos ajustados por estacionalidad y calendario (Cuadro 5, 25 agrupaciones).**  
  - *Motivo:* ofrecen un balance entre detalle sectorial y estabilidad en la serie, adecuados para TDA.  

- **Medida:** Miles de millones de pesos constantes (2015=100, volumen encadenado).  
- **Fuente:** DANE.  
- **Frecuencia:** Trimestral (con versión mensual interpolada).  
- **Rango Temporal:** 2005 – 2025pr (segundo trimestre).  
- **Relevancia:** el PIB es la variable central para caracterizar los ciclos económicos. Su descomposición sectorial permite identificar qué ramas impulsan o frenan la actividad en distintas fases del ciclo.  

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

---

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

### Precio Histórico del Petróleo Brent – Transformaciones
Para usar el Brent en conjunto con otras variables dentro del análisis, será necesario realizar ciertos ajustes:

- **Normalización (z-score):**  
  Centra la serie en 0 y la escala con desviación estándar 1.    

- **Transformación logarítmica:**  
  Aplicar logaritmo natural al precio.  
  - *Motivo:* reduce heterocedasticidad y estabiliza la varianza, haciendo que cambios relativos tengan más peso que cambios absolutos.  

- **Ajuste de rango:**  
  Se utilizan los datos desde 2003 hasta 2025.  
  - *Motivo:* definir un rango temporal homogéneo que abarque series completas de años, facilitando comparaciones históricas y análisis de tendencias de largo plazo.  

- **Cambio de formato (wide → tidy):**  
  La tabla original se transforma a formato tidy, con columnas `Fecha`, `Precio_Brent_USD` y `Pct_var_brent`.  
  - *Motivo:* facilita operaciones como filtrado, resampleo, fusión con otras variables y preparación de matrices multidimensionales para análisis topológico

---

### Precio Histórico del COLCAP – Transformaciones
Para usar el COLCAP en conjunto con otras variables dentro del análisis topológico, será necesario realizar ciertos ajustes:

- **Normalización (z-score):**  
  Centra la serie en 0 y la escala con desviación estándar 1.   

- **Transformación logarítmica:**  
  Aplicar logaritmo natural al valor del índice.  
  - *Motivo:* reduce heterocedasticidad y estabiliza la varianza, haciendo que los cambios relativos tengan más peso que los absolutos.  

- **Ajuste de rango con otras variables:**  
  Se utilizan los datos desde febrero de 2008 hasta julio de 2025.  
  - *Motivo:* Se ha venido trabajando en el rango 2003-2025 y habrá que tomar decisiones respecto a este índice COLCAP.

- **Cambio de formato (wide → tidy):**  
  La tabla original se transforma a formato tidy, con columnas `Fecha`, `Valor_COLCAP`, y `Pct_var_COLCAP`.  


---

### RELAB – Transformaciones
Para usar la base RELAB (Registro Estadístico de Relaciones Laborales) en conjunto con otras variables dentro del análisis topológico, será necesario realizar ciertos ajustes:

- **Normalización (z-score):**  
  Centrar cada serie en 0 y escalarla con desviación estándar 1.  
  - *Motivo:* permite comparar variables medidas en distintas escalas (número de relaciones laborales, sectores, tipo de aportante).  

- **Transformación logarítmica (cuando aplique):**  
  Aplicar logaritmo natural a conteos de relaciones laborales o aportantes.  
  - *Motivo:* estabiliza la varianza y facilita interpretar cambios relativos más que absolutos.  

- **Ajuste de rango temporal:**  
  Mantener el periodo 2008–2025 (en línea con otras variables como PIB, COLCAP y Brent).  
  - *Motivo:* garantiza coherencia temporal para el análisis conjunto.  

- **Cambio de formato (multi-hoja → tidy con división en sub-bases):**  
  En lugar de consolidar todas las hojas en un único panel, se plantea **dividir el archivo Excel en varias bases de datos independientes (.csv)**, cada una correspondiente a una de las sub-bases seleccionadas. Cada archivo se convertirá a formato tidy, con columnas estandarizadas como `Fecha`, `Categoria`, `Variable`, `Valor`.  
  - *Motivo:* facilita el almacenamiento organizado, permite trabajar cada sub-base por separado y luego integrarlas de forma flexible según el análisis requerido.  

- **Estandarización de categorías:**  
  Homologar los nombres de sectores económicos, tipos de aportante y condición de comercio exterior (exportador/importador).  
  - *Motivo:* evita duplicaciones o inconsistencias en la identificación de categorías, asegurando coherencia entre las diferentes sub-bases y fortaleciendo la detección de topologías persistentes.  
 

---

<!--
### Índice de Producción Industrial (IPI) – Variación y Contribución  

- **Homologación temporal:** ajustar la columna de periodo al formato `YYYY-MM` para trabajar la serie como datos de tiempo.  
- **Formato (wide → tidy):** transformar a columnas `Fecha`, `Sector`, `Tipo_Variacion`, `Valor_%`, `Contribucion_pp`.  
- **Normalización:** estandarizar las series con z-score para comparaciones entre sectores y con otras variables macroeconómicas.  
- **Suavizamiento (rolling mean):** calcular promedios móviles de 3 o 6 meses para identificar tendencias persistentes más allá de la volatilidad mensual.  
- **Rango:** limitar el análisis a los periodos comunes con otras series (2005–2025 aprox.), para garantizar consistencia en los cruces.  
---
-->

### ISE – Transformaciones  

- **Homologación temporal:**  
  Convertir la columna de periodo al formato `YYYY-MM` para manejar las series como datos de tiempo.  

- **Formato (wide → tidy):**  
  Reorganizar en columnas `Fecha`, `Agrupacion_CIIU`, `Tipo_Variacion` (Mensual), `Valor`.  
  - *Motivo:* facilita análisis comparativos entre sectores y cruces con otras variables macroeconómicas.  

- **Normalización (z-score):**  
  Centrar cada serie en 0 y escalar con desviación estándar 1.  
  - *Motivo:* permite comparar sectores heterogéneos dentro del ISE y también con series como PIB, COLCAP o Brent.  

- **Transformación logarítmica (cuando aplique):**  
  Aplicar logaritmo natural sobre índices o niveles antes de calcular variaciones.  
  - *Motivo:* estabiliza varianza y resalta cambios relativos.  

- **Suavizamiento (rolling mean):**  
  Calcular promedios móviles de 3 o 6 meses sobre la variación mensual.  
  - *Motivo:* identificar tendencias persistentes y reducir ruido de corto plazo.  

- **Rango temporal ajustado:**  
  Mantener el intervalo 2005–2025 para garantizar consistencia con otras variables de estudio.  

- **Cruce con PIB:**  
  Evaluar la capacidad anticipatoria del ISE respecto al PIB trimestral, verificando coherencia en niveles y variaciones.  

---


### PIB – Transformaciones  

- **Homologación temporal:**  
  Convertir la columna de periodo al formato `YYYY-Q` para manejo estandarizado de series trimestrales.  

- **Versión mensual (monthly disaggregation):**  
  Generar una versión mensual del PIB a partir de la serie trimestral mediante interpolación. Inicialmente se aplicará **cubic spline interpolation** para suavizar y distribuir los valores trimestrales en meses.  
  - *Nota:* esta técnica no corresponde a cifras oficiales, solo se adopta para empatar frecuencias con otras variables (ISE, IPC, tasas financieras).  
  - *Estado:* **sujeto a cambios** según disponibilidad de metodologías más robustas.  

- **Metodologías alternativas de desagregación temporal:**  
  Para mejorar la estimación de PIB mensual, se consideran métodos estándar de *temporal disaggregation*:  
  - **Chow-Lin (1971):** combina información de series trimestrales con un indicador mensual correlacionado (ej. ISE, producción industrial) para desagregar con base econométrica.  
  - **Denton (1971):** ajusta la serie mensual manteniendo la coherencia con la serie trimestral y suavizando cambios, ampliamente usado en estadística oficial.  
  - *Uso futuro:* evaluar la coherencia de la interpolación spline frente a estas metodologías y decidir si migrar a un esquema más sólido.  

- **Formato (wide → tidy):**  
  Reorganizar en columnas `Fecha`, `Agrupacion_CIIU`, `Valor`.  
  - *Motivo:* facilita comparaciones entre sectores y su relación con otras variables macro.  

- **Normalización (z-score):**  
  Escalar cada serie sectorial con media 0 y desviación estándar 1.  
  - *Motivo:* permite comparar sectores de diferentes magnitudes dentro del PIB y con indicadores como ISE, inflación o desempleo.  

- **Transformación logarítmica:**  
  Aplicar logaritmo natural sobre niveles de PIB antes de calcular variaciones.  
  - *Motivo:* estabiliza la varianza y permite calcular tasas de crecimiento temporales aproximadas.  

- **Variaciones temporales:**  
  Calcular:  
  - Tasa interanual: `log(PIB_t) - log(PIB_{t-12})` (para la serie mensual interpolada).  
  - Tasa intertrimestral: `log(PIB_t) - log(PIB_{t-3})`.  

- **Suavizamiento (HP filter o rolling mean):**  
  Extraer tendencia y ciclo.  
  - *Motivo:* separar la componente cíclica que interesa en el análisis TDA.  

- **Cruce con ISE:**  
  Validar coherencia entre el PIB trimestral y el ISE mensual, aprovechando el desfase temporal para evaluar poder predictivo.  

---

## Base de datos central

La **base central** consolida múltiples series macroeconómicas y financieras de Colombia, integrando indicadores de actividad, precios, mercados financieros y empleo. Cada fila corresponde a una **fecha mensual** (`YYYY-MM`), y cada columna representa una variable específica de distintas fuentes.

---

### Contenido de la Base

1. **Producto Interno Bruto (PIB) – Enfoque Producción**
   - **Descripción:** mide el valor agregado generado por distintas ramas de actividad económica, siguiendo la clasificación **CIIU Rev. 4 A.C.**  
   - **Serie:** Miles de millones de pesos constantes (2015=100, volumen encadenado).  
   - **Frecuencia original:** Trimestral; **interpolada mensualmente** para análisis continuo.  
   - **Fuente:** DANE.  
   - **Rango temporal:** 2005 – 2025pr (segundo trimestre).  
   - **Relevancia:** variable central para caracterizar ciclos económicos; permite identificar qué sectores impulsan o frenan la actividad.

2. **Indicador de Seguimiento a la Economía (ISE)**
   - **Descripción:** indicador mensual que funciona como proxy del PIB, compuesto por 12 agrupaciones sectoriales según CIIU Rev. 4 A.C.  
   - **Serie:** Índice base 2015=100, con versiones ajustadas por estacionalidad y calendario.  
   - **Frecuencia:** Mensual (ya disponible en la base).  
   - **Fuente:** DANE.  
   - **Relevancia:** permite anticipar la dinámica del PIB y realizar análisis sectorial de coyuntura.

3. **Índice de Precios al Consumidor (IPC)**
   - **Descripción:** mide la evolución de los precios de una canasta representativa de bienes y servicios para consumidores.  
   - **Serie:** Índice mensual.  
   - **Fuente:** DANE.  
   - **Rango temporal:** 2005 – 2025.  
   - **Relevancia:** útil para análisis de inflación, poder adquisitivo y ciclos económicos.

4. **Mercados financieros**
   - **TRM (Tasa Representativa del Mercado):** valor de referencia del peso frente al dólar.
   - **COLCAP:** índice bursátil colombiano, con valores y variaciones porcentuales.  
   - **BRENT:** precio del petróleo Brent en USD y variaciones porcentuales.

5. **Empleo y mercado laboral**
   - **LAB:** datos sectoriales, públicos/privados, dependientes/independientes.  
   - **EMP:** aportantes a la seguridad social según tamaño de empresa.  
   - **Frecuencia:** mensual (ya normalizada en la base).

6. **Tratamiento de datos faltantes**
   - **Series económicas continuas (PIB, ISE, IPC, Brent):** interpolación temporal lineal mensual.  
   - **TRM y COLCAP:** forward-fill y backward-fill.  
   - **LAB y EMP:** relleno con 0 cuando no hay información reportada.  
   - **Motivo:** asegurar consistencia temporal y permitir análisis topológico y modelización.

---

### Consideraciones Generales

- Todas las series están alineadas temporalmente en **formato mensual**, lo que permite análisis integrados y cruce de variables.  
- Las variables ya contienen prefijos o nombres normalizados que indican su fuente (`PIB_`, `ISE_`, `IPC_`, `LAB_`, `EMP_`, etc.).  
- Esta base permite realizar análisis de **ciclos económicos, TDA y predicción de coyuntura** con datos integrados de distintos dominios macroeconómicos y financieros.

