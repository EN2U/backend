import pytest
from django.core.management import BaseCommand


@pytest.mark.unit_test
def test_true():
    true_value: bool = True
    assert true_value


@pytest.mark.integration_test
@pytest.mark.django_db
def test_system_check():
    base_command: BaseCommand = BaseCommand()
    system_check_errors = base_command.check()

    assert not system_check_errors
