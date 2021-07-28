# Description
* The **etl-pipeline** is a universal pipeline to extract, transform, and load data.
* The pipeline is a **Data Lake** for any format (Apache Avro, Apache ORC, JSON, CSV, etc...), a script (**job**) for transforming data into an optimal format for storing data and queries (**parquet**), as well as a visual tool for orchestrating the entire **ETL workflow**.

# Technological stack
* Analytics: AWS Glue (Crawler, Job, Bookmark, Data Catalog)
* Application Integration (Orchestration): AWS Step Functions
* Compute: AWS Lambda
* Storage: AWS S3  
* Language: Python
* IaC: Serverless Framework / Serverless.com 
* Package manager: npm

# Prerequisites
* Node.js

# Deploy
*
    ```
    npm i
    ```
*
    ```
    npm run deploy
    ```
