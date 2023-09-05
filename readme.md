# Inventory Management Web Application

## Project Overview

This web application is designed to manage the inventory of products in various locations. It includes functionalities to manage products, locations, product movements, and generate a product balance report.

## Getting Started

Follow these steps to set up and run the project locally:

1. **Installation:**

   - Ensure you have Python installed on your computer.
   - Install Django using pip:

     ```bash
     pip install Django
     ```

2. **Running the Development Server:**

   - Open a terminal or command prompt.
   - Navigate to the project's root directory (where `manage.py` is located).
   - Start the development server:

     ```bash
     python manage.py runserver
     ```

3. **Accessing the Admin Panel:**

   - Open your web browser (e.g., Chrome).
   - Go to `http://localhost:8000/admin`.
   - Log in with the following credentials:

     - Username: shabi
     - Password: 123

4. **Managing Products:**

   - Click on "Products" in the navigation list to view the list of products.
   - To add a new product, click on "Add product."
   - To edit an existing product, click on the product name in the list.

5. **Managing Locations:**

   - Click on "Locations" in the navigation list to manage locations (similar to managing products).

6. **Managing Product Movements:**

   - Click on "Product Movements" in the navigation list to manage product movements (similar to managing products).

7. **Viewing Product Balance Report:**

   - To view the product balance report, navigate to the following URL:

     ```
     http://localhost:8000/report/product_balance/
     ```

## Project Structure

The project follows a Django project structure with multiple apps for different functionalities. Ensure that you have defined models, views, and templates as needed for products, locations, product movements, and the product balance report.


