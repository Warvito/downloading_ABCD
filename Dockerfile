FROM python:3.9-slim-buster

ARG USER_ID
ARG GROUP_ID
ARG USER
RUN addgroup --gid $GROUP_ID $USER
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER

RUN python -m pip install --upgrade pip
RUN pip3 install nda-tools
