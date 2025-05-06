#!/bin/bash

echo "🚀 Iniciando configuración del entorno virtual..."

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Entorno virtual creado."
else
    echo "ℹ️ El entorno virtual ya existe."
fi

# Activar entorno virtual
source venv/bin/activate
echo "📦 Entorno virtual activado."

# Instalar dependencias
echo "🔧 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Ejecutar proyecto
echo "🏃 Ejecutando el proyecto..."
python main.py

