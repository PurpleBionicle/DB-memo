FROM python:3.9-slim-buster
WORKDIR ./
COPY * ./
RUN pip install -r requirements.txt
CMD [ "python3", "./Lite3.py"]
