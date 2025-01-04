FROM python:3.12

WORKDIR /app

COPY ./poetry.lock .

COPY ./pyproject.toml .

COPY . .

RUN pip install poetry

RUN poetry install

CMD [ "poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]