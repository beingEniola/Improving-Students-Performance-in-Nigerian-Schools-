## Improving Students Performance in Nigerian Schools
This project focuses on using data analytics to improve student performance developing a comprehensive data pipeline, predictive models, and actionable insights.

### - Problem Definition
 
In many Nigerian schools, student performance in key examinations remains subpar, as seen in recent results where a significant percentage of students scored below average in the JAMB UTME. This project seeks to address the underlying causes of poor student performance by collecting and analyzing data on factors that influence academic success. Our goal is to use data to identify at-risk students and provide recommendations for interventions that can improve their exam outcomes.

### - Data Collection

Since many schools lack a data infrastructure and we could not get real data, we simulated all data used taking into account the realities of Nigerian schools.

Simulated Data Includes: 

1. Survey Data : This data has information on demographic, behavioral, Socio-economic, and social engagement data which allows us to capture non-academic factors influencing performance.
2. Assessment Data:  This data has details of student performance on each subject in their last internal exam.
3. student Data: It contains information of the students (name, number, address...)
4. Subjects Data: Information on the subjects taken in the school
5. Teachers Data: Teachers information.

### - Database Building
This pipeline is designed to manage student and school-related data, storing CSV files in AWS S3, and loading them into Snowflake for centralized management and analysis. The pipeline is orchestrated using Apache Airflow to automate the data ingestion process and ensure efficient handling of daily operations such as exam results, attendance, and performance tracking.

Data Sources

* CSV File Structure: The pipeline ingests data from CSV files containing student records, exam results, and other school-related data.
* Frequency: CSV files are generated daily/weekly.
* Naming Convention: Files are named using the pattern school_{date}.csv.
   
S3 Setup
*  S3 Bucket: school-db-bucket
* Folder Structure: Files are organized based on year and month for easier retrieval. Example: students/{year}/{month}/
*  Retention Policy: Files are retained for 1 year before they are archived or deleted based on school policies.

 Snowflake Setup
* Destination Table: Data from the CSV files will be loaded into its respective Snowflake table
  
Airflow Orchestration
*  Airflow DAG: The pipeline is orchestrated by an Airflow DAG which automates the process of data extraction, transformation, and loading (ETL).
   Tasks:
    * Extract Task: Fetch CSV files containing student data from the source.
    * Upload Task: Upload the CSV files to the designated S3 bucket.
    * Load Task: Load data from S3 to Snowflake using the COPY INTO command.
    *  Schedule: The pipeline is to be run at the end of each term
      
Monitoring and Logging
* Monitoring: The pipeline is monitored using Airflow's UI and logging system.
    *All task executions and failures are logged for troubleshooting.
* Alerting: Alerts are set up via email to notify the admin of any failures or delays in the pipeline.
* Data Quality Checks: Row count checks and validation rules are run before loading data into Snowflake to ensure integrity.

 Security and Permissions
AWS IAM Policy: Proper IAM policy isset to control access to the S3 bucket, ensuring that only authorized users and systems can read or write data.



### - Exploratory Data Analysis 

In the EDA phase, we explored relationships between different variables to uncover patterns, correlations, and key insights. By performing descriptive statistics and visualizations, we aimed to understand how various factors impact student performance.

Insights gotten from the analysis are : 
1. Students who partake actively in class have high performance than students who rarely participate in class activities
2. Students who take private lessons tend to perform better, on average, than those who do not
3. Higher levels of parental education do not necessarily lead to improved academic outcomes for their children.
4. Students without internet access perform better on average than those with internet access
5. Students who participated in extracurricular activities perform better academically, with a higher average score than those who don't.


### - Model Building 
### - Model Evaluation

### - Model Interpretation 

### - Model Deployment 

