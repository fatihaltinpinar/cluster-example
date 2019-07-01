from python:3

ADD ./ /web/

RUN pip install bottle

user root

EXPOSE 8080

WORKDIR /web/

CMD [ "python", "./bottle_app.py" ]
