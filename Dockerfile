FROM python:3.6.4-slim-jessie

LABEL image for displaying complete list of products

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app

WORKDIR /app

ENTRYPOINT [ "python" ]

CMD [ "product_list.py" ]