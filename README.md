# Wholesale Distribution Management System

A complete Wholesale Distribution Management System built using **ERPNext and Frappe Framework** for managing purchasing, sales, inventory, suppliers, customers and accounting operations.

## Project Overview

Global Wholesale Traders uses this system to manage its end-to-end wholesale distribution business operations through a centralized ERP platform.

The project uses standard ERPNext modules along with custom configurations, workflows, scripts and reports.

## Business Requirements

- Customer and supplier management
- Product and item management
- Purchase and sales management
- Multi-warehouse inventory management
- Stock monitoring and reorder management
- Accounting and payment management
- Business reports and dashboards

## Technology Stack

| Technology | Purpose |
|---|---|
| Frappe Framework v16 | Application framework |
| ERPNext v16 | ERP solution |
| Python | Backend development |
| JavaScript | Client-side customization |
| MariaDB | Database |
| Redis | Caching and background jobs |
| Git & GitHub | Version control |

## ERPNext Architecture

The application uses ERPNext standard DocTypes and a custom Frappe application.

Core modules:

- Stock
- Buying
- Selling
- Accounts

## Features

### 1. Customer Management
Manage customer records, contact information and transactions.

### 2. Supplier Management
Maintain supplier details and purchasing history.

### 3. Purchase Management
Manage purchase orders, purchase receipts and purchase invoices.

### 4. Sales Management
Manage quotations, sales orders, delivery notes and sales invoices.

### 5. Inventory Management
- Warehouse management
- Stock balance tracking
- Stock ledger
- Minimum stock level customization

### 6. Accounting Management
- Chart of Accounts
- Accounts Receivable
- Accounts Payable
- Payment Entries
- Financial Reports

### 7. Custom Development
- Custom Fields
- Client Scripts
- Server Scripts
- Purchase Order Approval Workflow
- Sales Invoice Notifications
- Customer Wise Sales Report
- Supplier Wise Purchase Report

## Installation Instructions

Refer to [Installation Guide](docs/installation-guide.md).

## Purchase Workflow

Supplier → Purchase Order → Purchase Receipt → Purchase Invoice → Payment Entry.

See [Purchase Workflow](docs/purchase-workflow.md).

## Sales Workflow

Customer → Quotation → Sales Order → Delivery Note → Sales Invoice → Payment Entry.

See [Sales Workflow](docs/sales-workflow.md).

## Inventory Management

Inventory is managed using ERPNext Stock module, including warehouses, stock entries, stock balance and stock ledger.

See [Inventory Management](docs/inventory-management.md).

## Accounting

Financial operations are handled through ERPNext Accounts module.

See [Accounting Management](docs/accounting-management.md).

## Custom Development

Custom configurations and development details are documented in [Custom Development](docs/custom-development.md).

## Reports and Dashboard

- Customer Wise Sales Report
- Supplier Wise Purchase Report
- Stock Balance Report
- Stock Ledger Report
- Accounts Receivable
- Accounts Payable

## User Roles

The system uses role-based access control for managing business operations.

See [Roles and Permissions](docs/roles-permissions.md).

## Screenshots

Screenshots of the implemented system are available in the [screenshots](screenshots/) directory.

## Testing Instructions

Refer to [Testing Report](docs/testing-report.md) for test cases and verification details.

## Repository Structure

```text
wholesale_distribution/
├── wholesale_distribution/
│   ├── fixtures/
│   ├── report/
│   ├── hooks.py
│   └── ...
├── docs/
├── screenshots/
├── data/
├── README.md
└── LICENSE
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

---

**Project:** Wholesale Distribution Management System  
**Company:** Global Wholesale Traders  
**Framework:** Frappe / ERPNext v16
