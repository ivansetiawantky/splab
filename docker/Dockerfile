FROM ubuntu:24.04

#
# Timezone must be set before starting cron etc.
#
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV TZ="Asia/Tokyo"

# https://dev.to/0xbf/set-timezone-in-your-docker-image-d22
# https://qiita.com/jerrywdlee/items/d4468f076bdea236bf3b
# Must add below to correctly do cron at the specified timezone.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3-venv \
    python3-dev \
    python3-pip \
    build-essential \
    libsamplerate0 \
    libsndfile1 \
    cmake \
    vim \
    less \
    tree \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# It is better to use non privileged user "spluser" to work.
RUN useradd --create-home --shell /bin/bash spluser
USER spluser
WORKDIR /home/spluser
COPY ./spluser/dot.bashrc /tmp
RUN cat /tmp/dot.bashrc >> /home/spluser/.bashrc

# venv directory must be owned by spluser, so create venv with user spluser (i.e., after USER spluser layer)
ENV VIRTUAL_ENV=/home/spluser/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Until here: BUILD AND TEST PYTHON3
# docker build [--no-cache] -t splab -f Dockerfile . [2>&1 | tee build.log]
# docker run --rm -ti splab:latest cat /etc/lsb-release
# docker run --rm -ti splab whoami
# docker run --rm -ti splab bash -c 'which python3 && python3 --version && which pip3 && pip3 --version'
# docker run --rm -ti splab bash -c 'which python && python --version && which pip && pip --version'

# do pip3 install inside spluser's venv (i.e. after ENV PATH="$VIRTUAL_ENV/bin:$PATH" layer)
COPY ./resources/requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# docker run --rm -ti splab bash -c 'pip3 freeze'

# Run the ubuntu system:
# docker run --rm -it --name splcont -v `dirname $PWD`:/home/spluser/work splab
# Inside splcont container, execute `source /home/spluser/venv/bin/activate`
#
# To execute another /bin/bash at the currently running container "splcont":
# docker exec -it splcont /bin/bash

# To execute another /bin/bash at the currently running container "splcont", as root (for example to do `apt-get update`):
# docker exec -u root -it splcont /bin/bash
