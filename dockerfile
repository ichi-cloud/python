FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask opencv-python-headless nanoid
CMD ["python3", "server.py"]
