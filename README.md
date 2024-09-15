# BlueMartin Website

Welcome to **BlueMartin**, your one-stop online marketplace for buying and selling products and services. This repository contains the codebase for the BlueMartin website, built using Django, a high-level Python web framework.

## Project Overview

BlueMartin is an e-commerce platform that allows users to:
- Browse a wide variety of products and services 🛍️
- Vendors can register, upload, and manage their products or services 🎉
- Buyers can browse, add items to the cart, and make purchases 🛒
  
This project was developed with the goal of providing an easy-to-use platform for both buyers and sellers to interact in a secure and efficient way.

## Features

- **Vendor Registration and Management**: Vendors can sign up, verify their accounts, and upload products for sale.
- **Customer Shopping Experience**: Customers can easily browse categories, view products, and purchase items online.
- **Secure Authentication**: Built-in authentication system with support for both vendors and buyers.
- **Product Search**: Users can search for products and filter based on categories.
- **Responsive Design**: The website is fully responsive, ensuring a great experience on mobile and desktop devices.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (Development), can be configured to use PostgreSQL or MySQL in production
- **Hosting**: WhoGoHost

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- Virtualenv (optional, but recommended)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/bluemartin-website.git
    cd bluemartin-website
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional but recommended):

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

The website will now be accessible at `http://127.0.0.1:8000/`.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit and push to your branch
5. Submit a Pull Request

## Contact


## License
