import json

from download_pdfs import download_pdfs

# Read papers.json file
with open("papers.json", "r") as f:
    papers = json.load(f)
    papers = [paper for paper in papers if paper["paper_link"] != ""]

paper = [papers[0]]

download_pdfs(paper)
