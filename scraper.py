from bs4 import BeautifulSoup
import requests


def scrape_madry_lab():
    # Initialize an empty list to store paper URLs
    paper_links = []
    main_url = "https://gradientscience.org"
    # Initialize a counter for page numbers
    page_number = 1

    while True:
        # Construct the URL based on the page number
        if page_number == 1:
            url = "https://gradientscience.org"
        else:
            url = f"https://gradientscience.org/page{page_number}"

        # Fetch the main page
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all blog post links associated with papers
        blog_links = [main_url + str(a["href"]) for a in soup.select(".post-link")]

        # Break the loop if no blog links are found, indicating that there are no more pages
        if not blog_links:
            break

        # Loop through each blog post link to find the associated paper link
        for blog_link in blog_links:
            blog_response = requests.get(blog_link)
            blog_soup = BeautifulSoup(blog_response.content, "html.parser")
            paper_title = blog_soup.select_one("h1").text
            # Get the first button with a link to arXiv, if any
            paper_link = next(
                (
                    button["href"]
                    for button in blog_soup.find_all(class_="bbutton")
                    if "arxiv.org" in button["href"]
                ),
                "",
            )

            paper_links.append(
                {
                    "paper_link": paper_link,
                    "paper_title": paper_title,
                    "blog_link": blog_link,
                }
            )

        # Increment the page number for the next iteration
        page_number += 1

    return paper_links
