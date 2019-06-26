FROM python:3

ADD ./ /webpage/

RUN pip install bottle
# RUN chmod 777 /webpage/*

USER root

EXPOSE 8080

#ENTRYPOINT ["/usr/bin/python3", "./webpage/bottle_app.py"]

WORKDIR /webpage/

CMD [ "python" , "./bottle_app.py" ]
