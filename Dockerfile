FROM python:3.7.0-stretch

WORKDIR /usr/src/app

COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD ["python", "run.py"]
