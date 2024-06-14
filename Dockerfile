FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED 1

RUN python manage.py migrate

COPY fixtures/*.json /app/fixtures/
RUN python manage.py loaddata /app/fixtures/*.json

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
