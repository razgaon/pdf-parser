import os
import wget
from concurrent.futures import ThreadPoolExecutor

def download_pdf(pdf_obj):
    # Create a directory to store the PDFs
    output_directory = "downloaded_pdfs"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Construct the ArXiv PDF URL from the abstract URL
    pdf_url = pdf_obj["paper_link"].replace("/abs/", "/pdf/") + ".pdf"
    file_title = "_".join(pdf_obj['paper_title'].split(" "))
    
    # Download the PDF
    output_path = f"{output_directory}/{file_title}.pdf"
    wget.download(pdf_url, output_path)
    print(f"Downloaded {pdf_obj['paper_title']}")

def download_pdfs_parallel(pdf_urls, num_threads=10):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(download_pdf, pdf_urls)
