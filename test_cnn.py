import mysql.connector
from connect import DatabaseConnector  # Assuming connect.py contains the DatabaseConnector class

def summarize_database_to_html(output_file='database_summary.html'):
    """Prints a summary of the database including number of tables and their columns to an HTML file."""
    db_connector = DatabaseConnector()  # Create an instance of DatabaseConnector

    # Connect to the database
    db_connector.connect_db()

    # Get the database connection
    connection = db_connector.get_connection()

    # If connection is not established, return
    if connection is None:
        print("No connection available to summarize the database.")
        return
    
    cursor = connection.cursor()

    try:
        # Get the database name
        cursor.execute("SELECT DATABASE()")
        database_name = cursor.fetchone()[0]

        # Initialize HTML content
        html_content = f"""
        <html>
        <head>
            <title>Database Summary</title>
            <style>
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                table, th, td {{
                    border: 1px solid black;
                }}
                th, td {{
                    padding: 10px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
            </style>
        </head>
        <body>
            <h1>Summary of Database: {database_name}</h1>
        """

        # Get list of tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        html_content += f"<p>Number of tables: {len(tables)}</p>"
        
        # Loop through each table and get column details
        for table in tables:
            table_name = table[0]
            html_content += f"<h2>Table: {table_name}</h2>"
            html_content += """
            <table>
                <tr>
                    <th>Column</th>
                    <th>Type</th>
                </tr>
            """
            
            cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = cursor.fetchall()
            for column in columns:
                html_content += f"""
                <tr>
                    <td>{column[0]}</td>
                    <td>{column[1]}</td>
                </tr>
                """
            html_content += "</table>"
        
        # Close HTML content
        html_content += """
        </body>
        </html>
        """
        
        # Write HTML content to file
        with open(output_file, 'w') as file:
            file.write(html_content)
        
        print(f"Database summary written to {output_file}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        # Close cursor and connection
        cursor.close()
        db_connector.close_connection()

# Example Usage:
# Replace with your actual database name
summarize_database_to_html('database_summary.html')
