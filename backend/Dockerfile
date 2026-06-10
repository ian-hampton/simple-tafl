FROM python:3.14.2-slim

WORKDIR /app

# prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set Flask environment
ENV FLASK_APP=run
ENV FLASK_ENV=development

# get dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy everything
COPY . .

# run
CMD ["flask", "run", "--host=0.0.0.0"]