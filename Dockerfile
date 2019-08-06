from python:3.6-alpine

ENV FLASK_APP manager.py

RUN adduser -D blog

WORKDIR /home/blog

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY manager.py config.py boot.sh ./

RUN chown -R blog.blog ./
RUN chmod +x boot.sh
USER blog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
