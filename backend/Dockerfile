FROM python:3.8

WORKDIR /app

COPY . /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
RUN pipenv requirements > req.txt
RUN apt-get update \
    && apt-get  install -y libpq-dev \
                           postgresql \
                           postgresql-contrib \
                           netcat \
    && pip install --upgrade pip \
    && pip install -r /app/req.txt


RUN chmod +x /app/scripts/wait_db.sh
