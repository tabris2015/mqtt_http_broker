FROM python:3.9-slim

ENV PORT 8000
COPY requirements.txt /
RUN pip install -q -r requirements.txt
COPY ./src /src
CMD uvicorn src.main:app --host 0.0.0.0 --port ${PORT}