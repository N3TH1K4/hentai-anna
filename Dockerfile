FROM python:3.8

WORKDIR /hentai-anna
COPY requirements.txt /hentai-anna/
RUN pip3 install -r requirements.txt
COPY . /hentai-anna/

CMD python3 bot.py
