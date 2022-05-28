# Description
This mini project contains a python script that makes it possible to load data from GCP Bigquery to a Postgres Database.

## Libraries
- pre-commit
- yapf
- google-cloud-bigquery
- pandas
- SQLAlchemy
- pytest
- tox


## Setup
1. Clone the repository
2. Change into the project directory and run
```bash
poetry init
```
3. To activate and use the app's virtual environment, enter the command below in the terminal
```bash
poetry shell
```

4. Run the command below to load the hooks defined in `.pre-commit-config.yaml`.
```bash
pre-commit install
```

Now when changes are committed to a branch, `pre-commit` runs the defined hooks on that branch. Changes will likely not be committed the first time if code is not properly formatted or if a test fails, as specified by the hooks in this case. `pre-commit` will attempt to reformat the code using the installed `yapf` formatter, but any issues with tests has to be rectified manually. When all issues are resolved, changes will then be committed after running a `git add` command, and then a commit command.

## usage
`Usage`
