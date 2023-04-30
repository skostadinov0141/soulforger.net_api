FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

EXPOSE 8000

USER user

CMD ["uvicorn", "core:app", "--host", "0.0.0.0", "--port", "8000"]