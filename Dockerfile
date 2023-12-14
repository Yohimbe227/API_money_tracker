FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . .

RUN python start.py

CMD ["tail", "-f", "/dev/null"]

LABEL author='Kamanin Y.N.' version=1.0
