# Exporting the first sheet of the Excel file to CSV format
csv_file_path = '/mnt/data/Coffee_Shop_Sales.csv'

try:
    # Save the first sheet as a CSV file
    first_sheet_data.to_csv(csv_file_path, index=False)
    csv_file_path
except Exception as e:
    str(e)
