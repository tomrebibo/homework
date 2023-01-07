FROM ubuntu
USER root
WORKDIR /tmp
COPY ./ ./
RUN  apt-get update && \
     apt-get install python3 -y && \
     apt-get install python3-pip -y && \
     pip3 install flask  && \
     pip3 install gunicorn


CMD  gunicorn -b 0.0.0.0:8000 app:app