# Installation Guide

## Prerequisites

- Ubuntu 22.04 or later
- Python
- Node.js
- MariaDB
- Redis
- Frappe Bench

## Step 1: Create Bench

bench init wholesale-bench --frappe-branch version-16

cd wholesale-bench

## Step 2: Get ERPNext

bench get-app erpnext --branch version-16

## Step 3: Install ERPNext

bench new-site wholesale.local

bench --site wholesale.local install-app erpnext

## Step 4: Get Custom App

bench get-app wholesale_distribution
  https://github.com/YOUR_USERNAME/wholesale-distribution-management.git

## Step 5: Install Custom App

bench --site wholesale.local install-app wholesale_distribution

## Step 6: Run Migration

bench --site wholesale.local migrate

## Step 7: Start Server

bench start
