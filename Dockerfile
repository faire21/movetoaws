FROM python:3.6

RUN pip install python-resize-image
RUN pip install boto3
RUN pip install Pillow

WORKDIR /app
COPY app.py /app/

VOLUME ["/app/images"]


