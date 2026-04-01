#!/bin/bash

sed -i 's/pydantic==2.5.0/pydantic==1.10.13/' /app/requirements.txt

export PORT=8000

pip install --no-cache-dir -r /app/requirements.txt