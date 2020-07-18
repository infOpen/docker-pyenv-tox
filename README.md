# Docker - Python testing with pyenv and tox

## Description

This image is used to run Python3 projects tests with Tox on multiple Python
versions, managed by Pyenv.

## Managed Python version

These Python versions are managed by this image using pyenv:
* 3.6.10
* 3.7.7
* 3.8.3

## System packages installed

* curl
* git
* libbz2-dev
* libffi-dev
* libpython3.5-dev
* libreadline-dev
* libsqlite3-dev
* libssl-dev
* libxml2-dev
* libxslt1-dev
* locales
* lsb-release
* python3
* python3-pip
* python3-virtualenv
* zip

## Arguments

| Name      | Default value  |
| --------- | -------------- |
| USER_NAME | pyenv-test     |
| USER_UID  | 6000           |


## Tests

Tests are done using [Testinfra](https://github.com/philpep/testinfra).
You must have pip installed to run tests

1. Install dependencies
    ```
    pip install -r requirements.txt
    ```

2. Run tests
    ```
    pytest
    ```
