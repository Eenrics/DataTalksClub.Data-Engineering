python3 -m venv env    
source env/bin/activate
alias env_dbt='source /Users/mac/data-engineering/DataTalksClub.Data-Engineering/04-analytics-engineering/env/bin/activate'
 python -m pip install dbt-core dbt-postgres

 dbt init
 dbt debug