import pytest
from app.bq_psql import engine


@pytest.fixture
def project_name():
    return "d2b-sdbx"


def test_load_bigquery_to_postgres(project_name):
    # assert "d2b-sdbx" == project_name
    assert engine == "postgresql"
