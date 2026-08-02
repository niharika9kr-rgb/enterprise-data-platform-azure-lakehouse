# Enterprise Data Platform – Azure Lakehouse

## Project Overview

This project demonstrates the design and implementation of an enterprise-scale Azure Lakehouse using the Medallion Architecture (Bronze, Silver, Gold).

The platform simulates how a retail company ingests data from multiple operational systems, stores raw data in Azure Data Lake Storage Gen2, transforms it using Azure Databricks with PySpark, and delivers analytics-ready datasets for reporting in Power BI.

Rather than building separate pipelines for every data source, the solution uses a reusable, parameterized Azure Data Factory pipeline that can ingest multiple datasets into the Bronze layer.

---

## Business Problem

Retail companies receive data from many independent systems such as:

- Website
- Mobile application
- Physical stores
- CRM
- Payments
- Product catalog
- Reference data

These systems produce data in different formats and at different times.

Without a centralized platform, businesses face:

- Duplicate customer records
- Inconsistent product information
- Poor data quality
- Slow reporting
- Difficult cross-system analytics

The objective of this project is to build a scalable Azure-based data platform that consolidates data from multiple systems into a single analytics platform.

---

## Project Goals

- Build a reusable Azure Data Factory ingestion framework
- Implement the Medallion Architecture
- Store raw data in Azure Data Lake Storage Gen2
- Clean and standardize data using Azure Databricks
- Build analytics-ready Gold datasets
- Create Power BI dashboards
- Demonstrate enterprise Data Engineering best practices
