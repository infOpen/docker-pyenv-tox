# Docker - Python testing with pyenv and tox

## Description

This image is used to run Python3 projects tests with Tox on multiple Python
versions, managed by Pyenv.

## Managed Python version

These Python versions are managed by this image using pyenv:
* 2.7.15
* 3.4.9
* 3.5.6
* 3.6.7
* 3.7.1

## System packages installed

| Name | Version |
| ----- | ------- |
| curl | 7.47.0-1ubuntu2.7 |
| git | 1:2.7.4-0ubuntu1.6 |
| libbz2-dev | 1.0.6-8 |
| libffi-dev | 3.2.1-4 |
| libpython3.5-dev | 3.5.2-2ubuntu0~16.04.5 |
| libreadline-dev | 6.3-8ubuntu2 |
| libsqlite3-dev | 3.11.0-1ubuntu1 |
| libssl-dev | 1.0.2g-1ubuntu4.14 |
| libxml2-dev | 2.9.3+dfsg1-1ubuntu0.6 |
| libxslt1-dev | 1.1.28-2.1ubuntu0.1 |
| locales | 2.23-0ubuntu10 |
| lsb-release | 9.20160110ubuntu0.2 |
| python3 | 3.5.1-3 |
| python3-pip | 8.1.1-2ubuntu0.4 |
| python3-virtualenv | 15.0.1+ds-3ubuntu1 |
| zip | 3.0-11 |

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
