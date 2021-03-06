FROM python:3.7
WORKDIR /pyapp
ENV PORT 80
COPY . /pyapp

RUN pip install -r requeriments.txt
CMD ["python","app.py"]
