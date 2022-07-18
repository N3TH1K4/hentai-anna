FROM python:3.8

WORKDIR /hentai-anna
COPY requirements.txt /movie-otaku-post/
RUN pip3 install -r requirements.txt
COPY . /hentai-anna/

CMD python3 bot.py
