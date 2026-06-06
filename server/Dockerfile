FROM python:latest

WORKDIR /app

RUN pip install --no-cache-dir flask requests

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]