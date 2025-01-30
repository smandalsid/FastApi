FROM python:3.12

WORKDIR /expensemgr

COPY poetry.lock ./

COPY pyproject.toml ./

COPY . .

RUN pip install poetry

RUN poetry install

CMD [ "poetry", "run", "uvicorn", "expensemgr.main:app", "--host", "0.0.0.0", "--port", "8000" ]