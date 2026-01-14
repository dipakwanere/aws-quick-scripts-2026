# AWS Data, ML & GenAI Services – Simple README
- This README documents all AWS services and core concepts mentioned in the last few questions and explanations.
- The goal is clarity, exam-aligned understanding, and simple spoken English — not marketing language.

#### Quick Snapshot of AWS for Machine Learning and GenAI Solutions. 

 - Files & datasets → S3
 - SQL on S3 → Athena
 - Shared storage → EFS
 - Fast disk → EBS
 - Big data → EMR
 - Workflow orchestration → Step Functions
 - Streaming → Kinesis
 - ETL → Glue
 - Batch jobs → AWS Batch
 - Archives → Glacier



Amazon EBS - Block storage volumes that allow custom disk I/O performance

AWS Storage Gateway - On-premises device to integrate legacy data with S3

AWS DataSync - Service to move data between on-prem systems and S3

AWS Batch - Managed batch processing service for data ingestion pipelines

AWS Lambda - Serverless compute to run code without managing servers 

AWS Step Functions - Service to coordinate components in data workflows

AWS Glue - Serverless ETL tool to transform and catalog S3 data

Amazon EMR - Hosts frameworks like Spark and Hadoop for distributed data processing

Amazon Kinesis - Platform to ingest, process, and analyze streaming data

AWS Lambda - Serverless compute to run code without managing servers

Hyperparameter optimization - Finding optimal model configuration settings to maximize performance.
#MLflow model tracking - Logging parameters, metrics, and output models during runs for experiment tracking.
Sagemaker kmeans++ hyperparameter optimization - Define hyperparameter ranges for the KMeans estimator

AWS Data Ingestion and Pipelines:
<img width="1314" height="676" alt="image" src="https://github.com/user-attachments/assets/a4fe60eb-cd49-42a1-9b31-29d54e36b717" />


#### Service Usages & Application:

1. Amazon S3 (Simple Storage Service)

Type: Object Storage

Amazon S3 is like a huge online hard drive.

Stores files as objects (data + metadata)

Very cheap and highly scalable

Not attached to any single server

Used for:

Datasets

ML models

Logs

Backups

Key idea:

If you hear datasets, files, storage at scale → think S3

2. Amazon S3 Infrequent Access (IA)

Type: Cheaper object storage tier

For data you don’t use often

Still available quickly when needed

Cheaper than standard S3

Used for:

Old ML models

Archived datasets that might be reused

3. Amazon S3 Glacier

Type: Archive Storage

Glacier is very cheap storage for old data.

Data is not instantly available

Retrieval can take minutes to hours

Used for:

Archived ML models

Compliance data

Long-term backups

4. Amazon Athena

Type: Serverless SQL Query Service

Athena lets you run SQL directly on data stored in S3.

No database to manage

Pay only for queries

Uses standard SQL

Used for:

Quick data analysis

Querying logs or CSV/Parquet files

5. Amazon EBS (Elastic Block Store)

Type: Block Storage

EBS is like a hard disk attached to one EC2 machine.

Very fast

Low latency

Used by only one EC2 at a time

Used for:

Databases

ML training needing fast disk access

6. Provisioned IOPS EBS

Type: High-performance EBS

Guaranteed speed (IOPS)

More expensive

Very low latency

Used for:

ML training with images

Performance-critical workloads

7. Amazon EFS (Elastic File System)

Type: Network File System

EFS is a shared folder in the cloud.

Multiple EC2 instances can access it at the same time

Acts like a Linux file system

Used for:

Shared ML training data

Multi-node training

8. AWS Snowball

Type: Offline Data Transfer Service

Snowball is a physical device AWS sends to you.

You copy data into it

Ship it back to AWS

AWS uploads data to S3

Used for:

Migrating TBs or PBs of on‑prem data

9. AWS DataSync

Type: Data Transfer Service

Moves data between on‑prem and AWS

Automated and fast

Used for:

Regular data synchronization

Hybrid environments

10. AWS Database Migration Service (DMS)

Type: Database Migration Tool

Migrates databases, not files

Keeps source DB running

Used for:

Moving MySQL, Postgres, Oracle to AWS

11. AWS Lambda

Type: Serverless Compute

Lambda lets you run code without managing servers.

Event-driven

Scales automatically

Used for:

APIs

Real-time processing

Automation

12. AWS Step Functions

Type: Workflow Orchestration

Step Functions help you connect multiple AWS services.

Define steps in order

Handles retries and failures

Used for:

ML pipelines

Data workflows

Serverless orchestration

13. Amazon Kinesis

Type: Streaming Data Service

Kinesis processes real-time data streams.

Handles continuous data

Integrates with Lambda

Used for:

Clickstream data

Logs

Real-time analytics

14. AWS Glue

Type: Managed ETL Service

Glue extracts, transforms, and loads data.

Built-in scheduler

Serverless

Used for:

Nightly ETL jobs

Data preparation

15. Amazon EMR

Type: Big Data Processing Service

EMR runs Spark, Hadoop at scale.

Handles petabytes of data

Cost-effective for big data

Used for:

Large-scale analytics

ML preprocessing

16. Amazon Redshift

Type: Data Warehouse

SQL-based analytics

Structured data

Used for:

BI dashboards

Reporting

17. Amazon DynamoDB

Type: NoSQL Database

Key-value storage

Very fast (milliseconds)

Used for:

Real-time applications

Not analytics

18. Amazon RDS

Type: Managed Relational Database

MySQL, Postgres, etc.

Transactional workloads

Used for:

Application databases

19. AWS Batch

Type: Batch Processing Service

AWS Batch runs scheduled batch jobs.

Manages servers automatically

Supports Docker

Used for:

Nightly data processing

ML training jobs

20. AWS Fargate

Type: Serverless Container Compute

Runs containers without managing servers

Works with ECS

Used for:

Long-running container workloads

21. Amazon ECS (Elastic Container Service)

Type: Container Orchestration

Manages Docker containers

Can use EC2 or Fargate

Used for:

Microservices

APIs

22. Cloud-based Development Environments

Concept (Not a single service)

Coding in the cloud

Same environment for everyone

Advantage:

Reproducible workflows

Examples:

AWS Cloud9

SageMaker Studio

23. Batch Jobs (Concept)

Batch jobs process data in chunks, not real time.

Key advantage (course-aligned):

Simplicity

24. Map-Reduce

Type: Programming Model

Map-Reduce is a programming model.

Map → process data pieces

Reduce → combine results

Used for:

Big data processing

Disk and compute bottlenecks

