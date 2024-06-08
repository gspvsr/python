FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -no-cache-dir requirements.txt
COPY . .
CMD ["Python","app.py" ]