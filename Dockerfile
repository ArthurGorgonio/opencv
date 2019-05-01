FROM python:3.7.2-alpine

LABEL maintainer="Arthur Gorgonio"

RUN echo -e '@edgunity http://nl.alpinelinux.org/alpine/edge/community\n\
  @edge http://nl.alpinelinux.org/alpine/edge/main\n\
  @testing http://nl.alpinelinux.org/alpine/edge/testing\n\
  @community http://dl-cdn.alpinelinux.org/alpine/edge/community'\
  >> /etc/apk/repositories && \
  apk upgrade && \
  apk add --update --no-cache \
  build-base \
  freetype-dev \
  gcc \
  musl-dev \
  openblas-dev


WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --no-cache -r requirements.txt

COPY start.sh /

RUN chmod +x /start.sh

COPY src/ .

CMD ["/bin/sh", "/start.sh"]
