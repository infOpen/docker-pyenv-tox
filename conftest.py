import pytest
import testinfra

# Get check_output from local host
check_output = testinfra.get_host("local://").check_output


# Override the host fixture
@pytest.fixture(scope='session')
def host(request):
    """
    Pytest host fixture overriden
    """

    # Build image and launch container
    image_id = check_output('docker build -q .').split(':')[1]
    container_id = check_output("docker run -d %s", image_id)

    # Manage a fixture finalizer to remove container even if exeption occurs
    def finalizer():
        """
        Finalizer used to remove container
        """
        check_output("docker rm -f %s", container_id)

    request.addfinalizer(finalizer)

    yield testinfra.get_host("docker://" + container_id)
