#!/bin/bash

DIR="fixtures"

for f in $DIR/*; do
    if [ -f "$f" ]; then
        python manage.py loaddata "$f"
    fi
done