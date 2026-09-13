import csv
import os
from docxtpl import DocxTemplate

def generate_certificates():
    # Define folder for output files
    output_folder = "Generated_Certificates"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the Word letterhead template
    template_path = "template.docx"
    if not os.path.exists(template_path):
        print("Error: template.docx not found! Please create it.")
        return

    # Read student data from the Google Forms CSV
    try:
        with open("students_data.csv", mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                doc = DocxTemplate(template_path)
                
                # Map CSV column headers to the template tags
                context = {
                    "Name": row.get("Name", "Unknown"),
                    "Enrollment": row.get("Enrollment", "Unknown"),
                    "Amount": row.get("Amount", "0"),
                    "Marks": row.get("Marks", "0")
                }
                
                # Render and save the individual document
                doc.render(context)
                output_filename = f"{output_folder}/{row.get('Enrollment')}_{row.get('Name')}.docx"
                doc.save(output_filename)
                
                print(f"✅ Generated: {output_filename}")
                
    except FileNotFoundError:
        print("Error: students_data.csv not found! Please place it in the same directory.")

if __name__ == "__main__":
    print("Starting certificate generation...")
    generate_certificates()
    print("Process complete!")