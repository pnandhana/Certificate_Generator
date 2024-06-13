import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Function to generate a certificate
def generate_certificate(name, college, template_path, font_path, output_path):
    # Open the certificate template
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)

    # Define text positions and properties
    name_position = (250, 300)  # Adjust based on your template
    college_position = (250, 400)  # Adjust based on your template
    font_size = 36  # Adjust based on your template

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Draw the text onto the image
    draw.text(name_position, name, font=font, fill="black")
    draw.text(college_position, college, font=font, fill="black")

    # Save the generated certificate
    image.save(output_path)

# Load the participant details from the spreadsheet
df = pd.read_excel('participants.xlsx')

# Print column names to debug
print("Column names in the DataFrame:", df.columns)

# Ensure the output directory exists
output_dir = 'certificates'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each participant and generate a certificate
for index, row in df.iterrows():
    name = row['Name']
    college = row['College']
    
    # Define paths
    template_path = 'template.png'
    font_path = 'arial.ttf'
    output_path = os.path.join(output_dir, f'{name}_certificate.png')
    
    # Generate the certificate
    generate_certificate(name, college, template_path, font_path, output_path)