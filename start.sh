#!/usr/bin/env bash
set -e

if [ ! -f "links_data_base.db" ] || [ $(stat -c%s "links_data_base.db") -lt 1000000 ]; then
    echo "Descargando links_data_base.db (3.32 GB) con huggingface_hub..."
    rm -f links_data_base.db
    python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='DarkNull68/factoriobin-links-db', filename='links_data_base.db', repo_type='dataset', local_dir='.')"
    echo "Descarga completada."
fi

exec gunicorn app:app
