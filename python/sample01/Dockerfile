FROM python:3.8.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# --host=0.0.0.0 外部からのアクセスを可能に。わすれがち。。
CMD [ "flask", "run", "--host=0.0.0.0" ]