FROM python:3.10.5-slim-buster

# install needed packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /fusion

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

