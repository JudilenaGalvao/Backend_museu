FROM python:3.12

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev gcc python3-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get install -y wget openssl build-essential git-core libxext-dev

RUN apt-get install -f -y

COPY . ./app/

EXPOSE 8000

CMD ["python", "app/manage.py", "runserver"]

