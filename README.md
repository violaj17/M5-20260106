# M5-20260106
Repository for QA Module 5  
Owner: Viola Joel 

## Project Introduction

### Background

The library currently performs data quality checks and reporting manually. This process is time-consuming, prone to human error, and difficult to scale as data volumes increase. There is also limited automation, which prevents stakeholders, librarians, and users from accessing up-to-date information.

### Project Aim

The aim of this project is to design and implement an automated data processing pipeline using Python, GitHub, and Azure DevOps. The solution will clean, validate, and transform library data, producing a presentation-ready dataset for reporting in Power BI.

### Objectives

- Reduce manual effort through automation  
- Improve data quality, consistency, and reliability  
- Enable repeatable and auditable data transformations  
- Provide timely insights for operational and strategic decision-making   

### Architecture Diagram

Initial Architecture Diagram (2026/01/05):  
![Architecture Diagram](./Architecture%20Diagram.png "Architecture Diagram")  

Updated Architecture Diagram (2026/01/08):   
![New Architecture Diagram](./Architecture%20Diagram%20New.png "New Architecture Diagram")

### Project Plan

1. Planning and Exploration
2. Data Storage and Cleaning
3. Development and Testing
4. Deployment
5. Automation
6. Reporting and Visualisation
7. Documentation

### Example User Stories

1. As a stakeholder, I want to reduce manual work and automate our process.
2. As a library user, I want an up-to-date status of our account/books.
3. As a librarian, I want to know how many books are to be returned for planning purposes.
4. As a librarian, I want to see an upt-to-date status of books for late fees, borrowed time, reserved status, etc.
5. As a data engineer, I want a dashboard to see pipeline metrics and trends.

## Scripts

- **scripts/app_refactored.py**  
    Refactored verion of the main application script. This script improves code structure, readability, and maintainability, and writes the cleaned data into SSMS.

- **scripts/data_clean.py**  
    Contains functions for cleaning and enriching library book and customer data.
    - 'clean_book_data': Cleans book records, removes duplicates, fixes date formats, and calculates loan durations.
    - 'clean_customer_data': Cleans customer records and ensures valid customer IDs.
    - 'dataEnrich': Calculates the duration between book checkout and return dates.

- **scripts/data_clean.ipynb**  
    Jupyter notebook for interactive data cleaning and exploration.

## Testing

- **testing/test_data_enrich.py**  
    Unit tests for the 'dataEnrich' function, verifying correct calculation of loan durations from sample data.

## Docker 

Docker is used to containerize the application, making it easy to build, run, and deploy in any environmet.

### Building the Docker Image

To build the Docker image, run:  
'''  
docker build -f docker/Dockerfile -t <image_name> .  
'''  
Replace '<image_name>' with your preferred image name. E.g. docker build -f docker/Dockerfile -t data-clean-app .

### Building the Docker Container

To run the container:  
'''  
docker run <image_name>  
'''  
Replace '<image_name>' with the image name. E.g. docker run data-clean-app

### Docker Mounting Commands

docker build -t hello-mount .  
docker run -v "$(pwd)/outputs:/data" hello-mount  
docker images  

### Docker Volume Commands

docker build -t hello-volume .  
docker volume create container-data  
docker volume ls  
docker run --mount type=volume,source=container-data,target=/data hello-volume  

### Notes

- Ensure your data files and any required configuration are accessible to the container. To see the project structure, check what Docker has copied:
    - Run an interactive shell: docker run -it --entrypoint sh <image-name>
    - Then inside the container run: ls -R /app
- Update the Dockerfile as necessary to include all dependences, and include packages in the 'requirements.txt' file.
- For database connectivity, make sure the container can access your SQL Server instance. (WIP)

## Archive

Folder containing draft files and notes for initial learning and experimenting.  

## Power BI Metrics Dashboard

A Power BI dashboard was created to visualise the data cleaning pipeline performance using metrics from ght cleaning_metrics.csv log file. The dashboard displays key pperformance indicators (total rows processed, retention rates, pipeline runs), data quality trends over time, and filters for dataset selection. This provides stakeholders with insights into the effectiveness of the pipeline and helps identify areas requiring attention or improvement.  
  
![Power BI Metrics Dashboard](./Metrics%20Dashboard.png "Metrics Dashboard")


