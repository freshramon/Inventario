# 🧾 Sistema de Gestión de Inventario en Python

## 📌 Descripción

Este proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar un inventario de productos.

El sistema permite agregar, buscar, actualizar, eliminar productos, calcular estadísticas y guardar/cargar la información en archivos CSV.

---

## 🚀 Funcionalidades

* ➕ Agregar productos
* 📋 Mostrar inventario
* 🔍 Buscar producto por nombre
* ✏️ Actualizar producto
* ❌ Eliminar producto
* 📊 Calcular estadísticas:

  * Unidades totales
  * Valor total del inventario
  * Producto más caro
  * Producto con mayor stock
* 💾 Guardar inventario en archivo CSV
* 📂 Cargar inventario desde archivo CSV

---

## 🧱 Estructura del proyecto

```
/proyecto
│
├── app.py          # Programa principal (menú)
├── servicios.py    # Lógica del inventario
└── archivos.py     # Manejo de archivos CSV
```

---

## 📦 Estructura de los datos

El inventario se maneja como una lista de diccionarios:

```python
inventario = [
    {"nombre": "pan", "precio": 2000.0, "cantidad": 10},
    {"nombre": "soda", "precio": 3000.0, "cantidad": 5}
]
```

---

## 📁 Formato CSV

El archivo CSV debe tener la siguiente estructura:

```
nombre,precio,cantidad
pan,2000,10
soda,3000,5
```

---

## ▶️ Cómo ejecutar el programa

1. Asegúrate de tener Python instalado
2. Abre la terminal en la carpeta del proyecto
3. Ejecuta:

```
python app.py
```

---

## 🎮 Uso del programa

El sistema muestra un menú interactivo:

```
1. Agregar
2. Mostrar
3. Buscar
4. Actualizar
5. Eliminar
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
```

Solo debes ingresar el número de la opción deseada.

---

## ⚠️ Validaciones implementadas

* Entrada numérica obligatoria en el menú
* Precio y cantidad no pueden ser negativos
* Validación de estructura del archivo CSV
* Manejo de errores al leer y escribir archivos
* Filas inválidas en CSV son ignoradas

---

## 🔄 Política de carga de datos

Al cargar un archivo CSV, el usuario puede:

* **Sobrescribir** el inventario actual
* **Fusionar** los datos:

  * Si el producto existe → suma cantidades
  * Si el precio cambia → se actualiza al nuevo
  * Si no existe → se agrega

---

## 🛠️ Tecnologías utilizadas

* Python 3
* Módulo estándar `csv`

---

## 🧠 Conceptos aplicados

* Estructuras de datos (listas y diccionarios)
* Modularización
* Manejo de archivos
* Manejo de errores (`try/except`)
* Funciones y parámetros
* Expresiones lambda

---

## 📌 Posibles mejoras

* Interfaz gráfica (GUI)
* Uso de base de datos (SQLite)
* Exportar a Excel
* Validaciones más avanzadas
* Interfaz web

---

## 👨‍💻 Autor

Proyecto desarrollado por Ramón como práctica de programación en Python.

---

## 📄 Licencia

Uso educativo y libre.

