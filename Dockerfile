FROM python:3.6.4-alpine3.7

RUN apk update && apk add build-base

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install numpy


