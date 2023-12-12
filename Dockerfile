FROM python:3.11-slim

RUN mkdir /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip

RUN apt-get update

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /app

WORKDIR /app

ENTRYPOINT ["python", "start.py"]

CMD ["tail", "-f", "/dev/null"]

LABEL author='Kamanin Y.N.' version=1.0
