import pytest
from app.bq_psql import engine
from google.cloud import bigquery
from app.bq_psql import bq_columns,sql_columns, query_job, result
from app.bq_psql import get_bigquery_data, load_location_data_to_postgres

##  CHECK CONNECTION FROM BIGQUERY

def test_connection_from_bigquery():
    assert query_job == True
    #return "d2b-sdbx"


def test_load_bigquery_to_postgres(project_name):
    # assert "d2b-sdbx" == project_name
    assert result == True
    #assert engine == "postgresql"

# assert that the data/column name are the same
def test_equalivant_data_in_both_database():
    assert bq_columns ==  sql_columns
    assert len(query_job) == result