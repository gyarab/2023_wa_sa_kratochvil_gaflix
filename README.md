# GAFlix

<img src="gaflix.png" alt="Logo" width="200" height="200" />

## Instalace

1. **Venv:**

```bash
python -3 -m venv venv
source ./venv/Scripts/activate
```

2. **Instalace Knihoven:**
```bash
pip install -r requirements.txt
```

3. **Inicializace Databáze:**
```bash
python manage.py migrate
```

4. **Aplikování Fixtures:**
```bash
python manage.py loaddata fixtures/*.json
```

5. **Spuštění:**
```bash
python manage.py runserver
```


