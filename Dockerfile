FROM phusion/baseimage:18.04-1.0.0
LABEL maintainer="Alexandre Chaussier <a.chaussier@infopen.pro>"

# Setting for packages installation
ENV DEBIAN_FRONTEND noninteractive

# Settings about Docker group management
ARG USER_UID=6000
ARG USER_NAME=pyenv-test

# Settings about pyenv management
ENV PYENV_ROOT /home/${USER_NAME}/.pyenv
ENV PATH ${PYENV_ROOT}/bin:/home/${USER_NAME}/.local/bin:$PATH

# Create user for pyenv
RUN useradd -m -s /bin/bash -u "${USER_UID}" "${USER_NAME}"

# Manage testing folder
RUN mkdir -p /srv \
    && mkdir /srv/app \
    && mkdir /srv/build \
    && mkdir /srv/src \
    && chown -R "${USER_NAME}":"${USER_NAME}" /srv
WORKDIR /srv/app

# Install openssh, lsb-release and python basics
RUN apt-get update && \
    apt-get -o Dpkg::Options::="--force-overwrite" install -y \
        curl \
        git \
        libbz2-dev \
        libffi-dev \
        libpython3.7-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        locales \
        lsb-release \
        python3 \
        python3-pip \
        python3-virtualenv \
        zip

# Locale management
RUN locale-gen en_US.UTF-8
RUN echo 'LC_ALL=en_US.UTF-8' > /etc/default/locale
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Tox and Pyenv management
RUN pip3 install tox==3.17.1 tox-pyenv==1.1.0
USER ${USER_NAME}
RUN git clone --depth 1 --branch v1.2.19 https://github.com/pyenv/pyenv.git ~/.pyenv \
  && echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc \
  && pyenv install 3.6.10 \
  && pyenv install 3.7.7 \
  && pyenv install 3.8.3

# Default command management
USER root
CMD ["/sbin/my_init"]
