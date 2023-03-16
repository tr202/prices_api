FROM python:3.9
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -requirements.txt
COPY . code
WORKDIR /code
EXPOSE 8000
ENTRYPOINT ["python", "mysite/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
