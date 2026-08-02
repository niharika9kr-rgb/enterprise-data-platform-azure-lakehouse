# Enterprise Data Platform – Azure Lakehouse

![Azure](https://img.shields.io/badge/Azure-Cloud-blue)
![Azure Data Factory](https://img.shields.io/badge/Azure%20Data%20Factory-Orchestration-orange)
![Azure Databricks](https://img.shields.io/badge/Databricks-Spark-red)
![PySpark](https://img.shields.io/badge/PySpark-Data%20Processing-yellow)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-green)
![Power BI](https://img.shields.io/badge/Power%20BI-Visualization-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![GitHub](https://img.shields.io/badge/Git-Version%20Control-black)

## Project Summary

This project simulates an enterprise retail data platform built on Microsoft Azure.

The solution ingests data from multiple operational systems using a reusable Azure Data Factory pipeline, stores raw data in Azure Data Lake Storage Gen2, transforms it using Azure Databricks with PySpark, and prepares analytics-ready datasets following the Medallion Architecture (Bronze, Silver and Gold).

The project is designed to demonstrate production-style Azure Data Engineering practices including reusable pipelines, scalable data ingestion, data quality validation, Delta Lake transformations and business reporting.

## Project Statistics

| Metric | Value |
|--------|------:|
| Source systems | 8 |
| Datasets | 8 |
| Records generated | 115,000+ |
| Azure services | 4 |
| Data pipeline | Generic parameterized pipeline |
| Architecture | Medallion (Bronze / Silver / Gold) |
| Programming language | Python |
| Processing engine | PySpark |

## Current Architecture

```text
Source Systems
      │
      ▼
Azure Data Factory
      │
      ▼
Azure Data Lake Storage Gen2
      │
      ▼
Bronze Layer
      │
      ▼
Azure Databricks (Next Phase)
      │
      ▼
Silver Layer
      │
      ▼
Gold Layer
      │
      ▼
Power BI
```



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

---

## Solution Architecture

The platform follows a modern Azure Lakehouse architecture using the Medallion pattern.

```text
Source Systems
    |
    |-- Website Customers
    |-- Mobile Customers
    |-- CRM Customers
    |-- Store Customers
    |-- Products
    |-- Orders
    |-- Payments
    |-- Exchange Rates
    |
    v
Azure Data Factory
    |
    v
Azure Data Lake Storage Gen2
    |
    |-- Source
    |-- Bronze
    |-- Silver
    |-- Gold
    |
    v
Azure Databricks
    |
    |-- PySpark transformations
    |-- Data quality checks
    |-- Customer standardization
    |-- Currency conversion
    |-- Delta Lake tables
    |
    v
Power BI
    |
    |-- Revenue analysis
    |-- Customer analytics
    |-- Product performance
    |-- Payment monitoring

## Project Roadmap

### Completed

- [x] Generate enterprise datasets
- [x] Azure Data Lake Storage Gen2
- [x] Azure Data Factory
- [x] Generic ingestion pipeline
- [x] Bronze layer

### In Progress

- [ ] Azure Databricks
- [ ] Bronze → Silver transformations

### Planned

- [ ] Gold layer
- [ ] Power BI dashboards
- [ ] CI/CD
- [ ] Automated data quality testing

## Future Improvements

- Implement incremental data loading
- Add Change Data Capture (CDC)
- Integrate Azure Key Vault
- Implement Azure Monitor alerts
- Add Azure DevOps CI/CD pipelines
- Introduce unit and integration testing
- Support Parquet and JSON ingestion
- Add metadata-driven pipeline configuration