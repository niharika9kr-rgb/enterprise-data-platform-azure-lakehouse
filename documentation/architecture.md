# Solution Architecture

## Overview

RetailMart uses multiple independent operational systems for customers, products, orders and payments. This project consolidates those sources into an Azure Lakehouse using the Medallion Architecture.

## Data Flow

```text
Python-Generated Source Systems
              |
              v
ADLS Gen2 Source Container
              |
              v
Azure Data Factory
Reusable Parameterized Pipeline
              |
              v
ADLS Gen2 Bronze
Raw CSV Files
              |
              v
Azure Databricks + PySpark
              |
       +------+------+
       |             |
       v             v
ADLS Silver     Quarantine
Clean Delta     Invalid Records
Tables
       |
       v
ADLS Gold
Business Aggregations
       |
       v
Analytics Consumers
Power BI planned as a future enhancement