"""
Docker image testing
"""

import pytest


def test_app_user(host):
    """
    Ensure app user exists
    """

    app_user = host.user('pyenv-test')

    assert app_user.uid == 6000
    assert app_user.home == '/home/pyenv-test'
    assert app_user.shell == '/bin/bash'
    assert 'pyenv-test' in app_user.groups


@pytest.mark.parametrize('name', [
    ('curl'),
    ('git'),
    ('libbz2-dev'),
    ('libffi-dev'),
    ('libpython3.7-dev'),
    ('libreadline-dev'),
    ('libsqlite3-dev'),
    ('libssl-dev'),
    ('libxml2-dev'),
    ('libxslt1-dev'),
    ('locales'),
    ('lsb-release'),
    ('python3'),
    ('python3-pip'),
    ('python3-virtualenv'),
    ('zip'),
])
def test_packages(host, name):
    """
    Ensure packages are installed
    """

    current_package = host.package(name)

    assert current_package.is_installed


@pytest.mark.parametrize('name,version', [
    ('tox', '3.17.1'),
    ('tox-pyenv', '1.1.0'),
])
def test_python_packages(host, name, version):
    """
    Ensure tox packages installed
    """

    pip_packages = host.pip_package.get_packages(pip_path=u'/usr/bin/pip3')
    assert name in pip_packages.keys()
    assert pip_packages[name]['version'] == version


@pytest.mark.parametrize('version', [
    ('3.6.10'),
    ('3.7.7'),
    ('3.8.3'),
])
def test_pyenv_versions(host, version):
    """
    Ensure needed Pyenv managed versions installed
    """

    pyenv_versions = host.check_output('pyenv versions')

    assert version in pyenv_versions


@pytest.mark.parametrize('env_var', [
    ('DEBIAN_FRONTEND=noninteractive'),
    ('LANG=en_US.UTF-8'),
    ('LC_ALL=en_US.UTF-8'),
    ('PATH=/home/pyenv-test/.pyenv/bin:'),
    ('PYENV_ROOT=/home/pyenv-test/.pyenv'),
])
def test_environment_variables(host, env_var):
    """
    Ensure needed Pyenv managed versions installed
    """

    env_vars = host.check_output('env')

    assert env_var in env_vars
