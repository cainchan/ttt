FROM python:3.12-alpine
RUN pip install flask -i https://mirrors.aliyun.com/pypi/simple
WORKDIR /app
COPY app /app
EXPOSE 5000
CMD ["python","app.py"]
