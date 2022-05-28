from google.cloud import bigquery
from variable import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER, HOST_NAME, PORT
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import time


green_color = "\033[92m%s\033[0m"
####################################################################
#        GETTING DATA FROM GCP BIGQUERY
####################################################################


def get_bigquery_data(gcp_project: str, bq_dataset: str, bq_table: str,
                      columns: list):
    client = bigquery.Client()
    print(green_color % "retrieving data from bigquery...")
    query = """
        SELECT {3}
        FROM `{0}.{1}.{2}`
    """.format(
        gcp_project, bq_dataset, bq_table, ",".join(columns.split(','))
    )
    print("QUERY: ", query)
    query_job = client.query(query)
    print(green_color % "data loaded from bigquery")
    return query_job

####################################################################
#        LOADING DATA TO POSTGRESQL
####################################################################


def load_location_data_to_postgres(engine, table, s_columns: list,
                                   source: pd.DataFrame):
    start = time.perf_counter()

    print(green_color % "connecting to postgres database...")
    url = f"{engine}://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOST_NAME}:{PORT}/{DATABASE_NAME}"
    engine = create_engine(url)

    print(green_color % "connected")
    source.columns = "".join(s_columns).split(",")

    print(green_color % f"Loading data to {table} table")
    source.to_sql(table, engine, if_exists="replace", index_label="id")
    print(green_color % "Data loaded successfully")

    end = time.perf_counter()
    print(f"Data loaded in {round(end - start, 1)} seconds")
    print(green_color % "connection closed")

if __name__ == "__main__":
    ####################################################################
    #               INPUTS PARAMETERS
    ####################################################################


    project = input("GCP bigquery project name: ")
    dataset = input("GCP bigquery dataset name: ")
    table = input("GCP bigquery table name: ")
    target_table = input("Postgresql table name: ")
    engine = "postgresql"
    bq_columns = input("GCP bigquery table columns name in a list format: ")
    sql_columns = input("Postgresql table columns name in a list format: ")
    print(green_color % "inputs entered successful")

    ####################################################################
    #            EXECUTIONS OF FUNCTIONS
    ####################################################################

    try:
        bq_query_job = get_bigquery_data(
            project, dataset, table, bq_columns)
        bq_source_df = bq_query_job.to_dataframe()

        bq_col_len = len((bq_columns).split(","))
        sql_col_len = len((sql_columns).split(","))

        if (bq_col_len) != (sql_col_len):
            if "created_at" and "updated_at" in "".join(sql_columns).split(","):
                bq_source_df = bq_source_df.assign(
                    created_at=datetime.now(), updated_at=datetime.now())
        print(bq_source_df.head())
        load_location_data_to_postgres(
            engine,
            target_table,
            sql_columns,
            bq_source_df,
        )
    except Exception as e:
        print(e)
