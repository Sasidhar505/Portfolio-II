
FROM python:3.11.4
# Fixed typo in Python version

WORKDIR /Portfolio

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update
# Update package lists using apt-get

RUN apt-get install -y gunicorn
# Install gunicorn package

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Portfolio.wsgi"]
# Run the gunicorn command to start the server
