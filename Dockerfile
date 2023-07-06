FROM python:3.10


# RUN adduser --system --no-create-home user

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update  \
    && apt-get -y install \
    bash \
    curl \
    jq

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN chmod +x /code/ip_update.sh

COPY . /code/

EXPOSE 8000

# USER user

# ENTRYPOINT [ "./ip_update.sh" ]

ENTRYPOINT [ "./ip_update.sh", "uvicorn", "core:app", "--host", "0.0.0.0", "--port", "8000" ]