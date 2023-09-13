import json
import os

from download_pdfs import download_pdfs_parallel


def dedup_papers(paper_list):
    deduped_papers = {}

    for paper in paper_list:
        paper_link = paper.get("paper_link", None)

        if paper_link:
            deduped_papers[paper_link] = paper

    deduped_list = list(deduped_papers.values())

    return deduped_list


def get_existing_papers(output_directory):
    all_files = os.listdir(output_directory)
    pdf_files = [
        file.split(".pdf")[0].replace("_", " ")
        for file in all_files
        if file.endswith(".pdf")
    ]
    return pdf_files


def main():
    existing_papers = get_existing_papers("downloaded_pdfs")
    with open("papers.json", "r") as f:
        papers = json.load(f)
        papers = dedup_papers(papers)
        papers = [
            paper
            for paper in papers
            if paper["paper_link"] != "" and paper["paper_title"] not in existing_papers
        ]
    print(f"Downloading {len(papers)} papers")
    download_pdfs_parallel(papers)


if __name__ == "__main__":
    main()
