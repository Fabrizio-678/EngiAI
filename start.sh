#!/usr/bin/env bash
set -e

if [ ! -f "links_data_base.db" ]; then
    echo "Descargando links_data_base.db (3.32 GB) desde Hugging Face..."
    curl -fL "https://huggingface.co" -o links_data_base.db
    echo "Descarga completada."
fi

exec gunicorn app:app
