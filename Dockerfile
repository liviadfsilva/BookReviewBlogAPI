FROM python:3.13-alpine

COPY . /book-review-blog-api

WORKDIR /book-review-blog-api

RUN pip3 install -r requirements.txt