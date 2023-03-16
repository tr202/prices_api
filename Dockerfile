FROM python:3.9.16-bullseye
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . prices_api
WORKDIR /prices_api/prices_api
RUN python3 manage.py migrate
RUN python3 manage.py load_listings_data
EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
