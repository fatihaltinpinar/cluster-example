FROM python:3

USER root

ENV AP /data/app
ENV SCPATH /etc/supervisor/conf.d

RUN apt-get -y update && mkdir -p /var/log/supervisor

ADD ./supervisord/conf.d/* $SCPATH/

ADD * $AP/

WORKDIR $AP

CMD ["supervisord", "-n"]
