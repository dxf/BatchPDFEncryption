
# import required modules
import os
from pypdf import PdfReader, PdfWriter
# assign directory
directory = 'files'
password = input('Type in password: ')
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    # checking if it is a file
    if os.path.isfile(f):
        if f.endswith(".pdf"):
            reader = PdfReader(f)
            writer = PdfWriter()

            # Add all pages to the writer
            for page in reader.pages:
                writer.add_page(page)

            # Add a password to the new PDF
            writer.encrypt(password)

            # Save the new PDF to a file
            with open(f"encrypted_files/encrypted-{filename}", "wb") as f:
                writer.write(f)