FROM python:3-bullseye
ARG PORT=8080

ENV PORT=$PORT
RUN mkdir /app
WORKDIR /app
RUN pip3 install --default-timeout=100 nltk keras tensorflow numpy flask
COPY . /app/

CMD [ "python3", "/app/app.py" ]