FROM python:3.9-slim-buster

RUN ln -sf /usr/share/zoneinfo/America/Mexico_City /etc/localtime

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    locales \
    tzdata \
    ca-certificates \
    && echo "America/Mexico_City" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && echo 'LANG="en_US.UTF-8"'>/etc/default/locale \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ["requirements.txt", "/app/"]

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000", "--workers=1"]