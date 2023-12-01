FROM python:3.10.9-slim
WORKDIR /BUGBITEDT_MAIN
RUN set TF_ENABLE_ONEDNN_OPTS=0
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN pip install tensorflow tensorflow-io 
RUN install libgcc-4.4.6-4.el6.i686
# Use Ubuntu 18.04 as the base image
# Install system dependencies
# Use the official CentOS 6 base image
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        libopencv-dev \ 
        build-essential \
        libssl-dev \
        libpq-dev \
        libcurl4-gnutls-dev \
        libexpat1-dev \
        libgcc-4.4.6-4.el6.i686 \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install opencv-python-headless
RUN pip install opencv-contrib-python
RUN pip install pipenv
RUN pip install --upgrade pip
RUN pip install --upgrade pip
EXPOSE 8000
COPY . .
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
