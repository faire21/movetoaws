FROM python:3.6

RUN pip install python-resize-image

WORKDIR /app
COPY app.py /app/
COPY resize.sh /app/

VOLUME ["/app/images"]


