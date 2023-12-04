import os
import shutil

def extract_pdfs(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_file_path = os.path.join(root, file)
                shutil.copy(pdf_file_path, destination_folder)

# Example usage
source_folder = r'C:\Users\m.doi\Desktop\Projects\SDS\SHOFU_FTP'
destination_folder = r'C:\Users\m.doi\Desktop\Projects\SDS\pdf'
extract_pdfs(source_folder, destination_folder)
