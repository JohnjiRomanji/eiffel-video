import csv
import os
import urllib.request

# Create the 'pictures' folder if it doesn't exist
if not os.path.exists('pictures'):
    os.makedirs('pictures')

# Open the CSV file
with open('eiffel_posts_good.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Skip the header row
    next(reader)
    
    # Loop through the rows
    for i, row in enumerate(reader):
        # Get the image URL from the second column
        url = row[1]
        
        # Generate the file name based on the index
        file_number = str(i+1).zfill(3)
        file_name = os.path.join('pictures', f'{file_number}.jpg')
        
        # Download the image and save it to the pictures folder
        urllib.request.urlretrieve(url, file_name)
