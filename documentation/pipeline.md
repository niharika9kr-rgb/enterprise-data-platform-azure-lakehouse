# Pipeline Design

## Source Data

The source layer contains generated datasets representing:

- Website customers
- Mobile customers
- CRM customers
- Store customers
- Products
- Orders
- Payments
- Exchange rates

## ADF Ingestion

The `pl_ingest_file` pipeline uses parameters rather than separate pipelines for every file.

### Parameters

| Parameter | Description |
|---|---|
| `sourceContainer` | Input ADLS container |
| `sourceFolder` | Input folder |
| `sourceFile` | Input filename |
| `sinkContainer` | Destination container |
| `sinkFolder` | Destination folder |

The same pipeline copies all source datasets into their corresponding Bronze folders.

## Bronze-to-Silver Processing

Databricks notebooks:

1. Read raw CSV files from Bronze.
2. Apply data-quality checks.
3. Standardize customer fields.
4. Remove duplicate records.
5. Separate invalid records into Quarantine.
6. Write cleaned records as Delta tables.
7. Register tables in Unity Catalog.

## Incremental Loading

Delta Lake `MERGE` is used to:

- Update existing customer records
- Insert new customer records
- Avoid duplicate business keys
- Reduce unnecessary full-table rewrites

## Gold Processing

Gold datasets support reporting and analytics:

| Gold table | Purpose |
|---|---|
| `customer_country_summary` | Customer distribution by country |
| `fact_sales` | Completed sales converted into EUR |
| `monthly_revenue` | Revenue and order trends by month |
| `channel_performance` | Website, Mobile and Store performance |
| `product_performance` | Units, orders and revenue by product |