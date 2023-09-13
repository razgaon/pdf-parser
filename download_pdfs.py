import os
import wget

def download_pdfs(pdf_urls):
    # Create a directory to store the PDFs
    output_directory = "downloaded_pdfs"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through each PDF URL to download it
    for pdf_obj in pdf_urls:
        # Construct the ArXiv PDF URL from the abstract URL
        pdf_url = pdf_obj["paper_link"].replace("/abs/", "/pdf/") + ".pdf"
        file_title = "_".join(pdf_obj['paper_title'].split(" "))
        # Download the PDF
        output_path = f"{output_directory}/{file_title}.pdf"
        wget.download(pdf_url, output_path)
        print(f"Downloaded {pdf_obj['paper_title']}")
