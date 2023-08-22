
FROM python:311..4

WORKDIR /Portfolio

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Install gunicorn package
RUN pip install gunicorn

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Portfolio.wsgi"]
