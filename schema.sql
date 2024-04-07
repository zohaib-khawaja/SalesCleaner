-- sales_data: Core table for storing the raw sales transactions.

CREATE TABLE sales_data (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    product_name VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2),
    source_format VARCHAR(50)  -- to indicate the source file format: CSV, Excel, JSON, XML
);

-- product_details: Supplementary table for storing details about products, which can be enriched from various file formats.

CREATE TABLE product_details (
    product_name VARCHAR(255) PRIMARY KEY,
    category VARCHAR(255),
    supplier VARCHAR(255)
);

-- sales_metadata: Flexible table to store additional metadata from JSON or XML files that might not fit neatly into the standard sales data table

CREATE TABLE sales_metadata (
    sales_id INT,
    metadata_key VARCHAR(255),
    metadata_value TEXT,
    FOREIGN KEY (sales_id) REFERENCES sales_data(id)
);