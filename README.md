# Email Notification Web Application

This project is a Flask-based web application that sends email notifications based on the user's selection (Approve, Hold, Reject) and summarizes order information in a table format.

## Key Features

- **Display Order Information**  
    The application reads data from CSV files (`OrderDB.csv`, `ProductDB.csv`, `UserDB.csv`), merges the information, and displays it in a table on the web page.
- **Email Notifications**  
    Based on the user's selection (Approve, Hold, Reject), the app sends an email to the designated recipient with relevant information.
- **Dynamic Table Rendering**  
    The order data is dynamically rendered into an HTML table using Pandas.

## Requirements

- Python 3.x
- Flask
- Pandas
- SMTP access (e.g., Gmail)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
2. **Install Required Python Packages**
    ```bash
    pip install flask pandas
3. **Email Setup**
    Replace the sender email and password in the Python script with your own information
    ```python
    smtp.login('your_email@gmail.com', 'your_password')

## How to Use

1. **Run the Server
    ```bash
    python your_script_name.py

    open your browser and go to 'http://127.0.0.1:5000/'

2. **Send Email**
    On the webpage, select an option ('Approve', 'Hold', 'Reject'), fill in the necessary information, and submit to send the email.

## Code Breakdown by Feature

1. **Code Breakdown by Feature**
    ```pyhon
import pandas as pd

def get_table():
    orderdb = pd.read_csv('OrderDB.csv')
    productdb = pd.read_csv('ProductDB.csv')
    userdb = pd.read_csv('UserDB.csv')

    order_product_ids = orderdb['product_id'].unique()  # product IDs from orderdb
    product_ids = productdb['product_id'].unique()  # product IDs from productdb
    order_user_ids = orderdb['user_id'].unique()  # user IDs from orderdb
    user_user_ids = userdb['user_id'].unique()  # user IDs from userdb

    order_order_id = orderdb['order_id'].unique()  # order IDs from orderdb
    order_quantity = orderdb['quantity'].unique()  # quantities from orderdb

    print_pr_name = []
    print_color = []
    print_us_name = []

    # Extract product names and colors corresponding to product IDs in orderdb
    for order_product_id in order_product_ids:
        if order_product_id in product_ids:
            pr_name = productdb[productdb['product_id'] == order_product_id]['name'].values
            color = productdb[productdb['product_id'] == order_product_id]['color'].values
            print_pr_name.append(pr_name[0])
            print_color.append(color[0])

    # Extract user names corresponding to user IDs in orderdb
    for order_user_id in order_user_ids:
        if order_user_id in user_user_ids:
            us_name = userdb[userdb['user_id'] == order_user_id]['name'].values
            print_us_name.append(us_name[0])

    # Create a new DataFrame
    df = pd.DataFrame({
        'order_id': order_order_id,
        'product_id': print_pr_name,
        'product_colors': print_color,
        'user_name': print_us_name,
        'quantity': order_quantity
    })

    # Send as HTML
    html_table = df.to_html(index=False, classes='table table-striped')
    return html_table

    *Tip: You can simplify the table generation using map functions.*

2. **Tip: You can simplify the table generation using map functions.**

    ```python
    def approve():
    msg = request.form['date']  # Get the selected date from the user
    time = request.form['time']  # Get the selected time from the user

    # Set up smtplib for sending email
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    # Login to the sending email account
    smtp.login('your_email@gmail.com', 'your_password')

    # Prepare the email content
    send_msg = MIMEText(f"Delivery Date: {msg} Delivery Time: {time}")
    send_msg['Subject'] = "Approve"  # Email subject

    # Send the email (sender email, receiver email)
    smtp.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', send_msg.as_string())

    # Close the SMTP session
    smtp.quit()

    # Generate and render the HTML table
    html_table = get_table()
    return render_template('email_test.html', table=html_table)

    *Note: The process for "Hold" and "Reject" cases is similar.


## Additional Information

The Korean README file can be found '' [README_KR](https://github.com/leedaeun31/automatic-e-mail-system/blob/min/README_KR.md) '' .
