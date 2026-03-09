# OSINT Threat Intelligence Collector

## Descripción
Este es un proyecto de **automatización OSINT** (Open Source Intelligence) desarrollado para recolectar y centralizar información sobre las últimas vulnerabilidades publicadas. La herramienta realiza un web scraping de fuentes públicas para extraer datos críticos, permitiendo un monitoreo rápido de nuevas amenazas.

## Resaltando:
* Automatización con Python.
* Recolección de inteligencia de amenazas.
* Manejo y estructuración de datos.

## Funcionalidades
* **Extracción Automática:** Obtiene los últimos IDs de CVE, descripciones y niveles de severidad.
* **Exportación de Datos:** Guarda los resultados en formato `.csv` para su posterior análisis en herramientas de gestión de vulnerabilidades.
* **Filtrado Inteligente:** Capacidad para identificar vulnerabilidades críticas de manera visual en la consola.

## Tecnologías utilizadas
* **Lenguaje:** Python 3.14.2
* **Librerías:**
    * `BeautifulSoup4` para (Parsing de HTML)
    * `Requests` para (Peticiones HTTP)
    * `Pandas` para (Estructuración de datos)

## Requisitos e Instalación
1. **Clonar el repositorio:**
   * git clone [https://github.com/FIsaimorales/OSINT.Threat.Intelligence.Collector.git](https://github.com/FIsaimorales/OSINT.Threat.Intelligence.Collector.git)

2. **Crear y activar entorno virtual**
    * python -m venv venv
    * .\venv\Scripts\activate

3. **Instalar Dependencias**
    * pip install -r requirements.txt








Developed by Frank Isai Morales