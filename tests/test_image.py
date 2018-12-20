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


@pytest.mark.parametrize('name,version', [
    ('curl', '7.47.0-1ubuntu2.7'),
    ('git', '1:2.7.4-0ubuntu1.6'),
    ('libbz2-dev', '1.0.6-8'),
    ('libffi-dev', '3.2.1-4'),
    ('libpython3.5-dev', '3.5.2-2ubuntu0~16.04.5'),
    ('libreadline-dev', '6.3-8ubuntu2'),
    ('libsqlite3-dev', '3.11.0-1ubuntu1'),
    ('libssl-dev', '1.0.2g-1ubuntu4.14'),
    ('libxml2-dev', '2.9.3+dfsg1-1ubuntu0.6'),
    ('libxslt1-dev', '1.1.28-2.1ubuntu0.1'),
    ('locales', '2.23-0ubuntu10'),
    ('lsb-release', '9.20160110ubuntu0.2'),
    ('python3', '3.5.1-3'),
    ('python3-pip', '8.1.1-2ubuntu0.4'),
    ('python3-virtualenv', '15.0.1+ds-3ubuntu1'),
    ('zip', '3.0-11'),
])
def test_packages(host, name, version):
    """
    Ensure packages are installed
    """

    current_package = host.package(name)

    assert current_package.is_installed
    assert current_package.version == version


@pytest.mark.parametrize('name,version', [
    ('tox', '3.0.0'),
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
    ('2.7.14'),
    ('3.4.7'),
    ('3.5.4'),
    ('3.6.3'),
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
