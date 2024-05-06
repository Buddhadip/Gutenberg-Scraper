import requests
from bs4 import BeautifulSoup
import re 
import json

def contains_table(html_content):
    """Check if the HTML content contains tables."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.find('table') is not None

def contains_non_ascii(content):
    """Check if the content contains non-ASCII characters."""
    try:
        content.encode('ascii')
    except UnicodeEncodeError:
        return True
    else:
        return False

# Fetch the HTML content of the Gutenberg eBooks webpage
ebooks_url = "https://www.gutenberg.org/ebooks/"
ebooks_response = requests.get(ebooks_url)
ebooks_html_content = ebooks_response.text

# Parse the HTML content using BeautifulSoup
ebooks_soup = BeautifulSoup(ebooks_html_content, "html.parser")

# Find the select field containing location options
location_select_field = ebooks_soup.find("select", {"id": "locc"})

# Extract the location values from the options
location_values = [option["value"] for option in location_select_field.find_all("option") if "value" in option.attrs]

print(location_values)

books_info = []
book_id = 1

for location in location_values:
    # Construct the URL to fetch books based on location
    location_url = f"https://www.gutenberg.org/ebooks/results/?author=&title=&subject=&lang=en&category=&locc={location}&filetype=html.images&submit_search=Search"
    location_response = requests.get(location_url)
    location_html_content = location_response.text
    location_soup = BeautifulSoup(location_html_content, 'html.parser')
    even_rows = location_soup.find_all(class_="evenrow")
    odd_rows = location_soup.find_all(class_="oddrow")
    for row in even_rows + odd_rows:
        # Extract book details from each row
        pattern = r'href="/ebooks/([^"]+)"'
        matches = re.findall(pattern, str(row))
        book_id_str = matches[0]  # store book ID as string
        book_url = f"https://www.gutenberg.org/cache/epub/{book_id_str}/pg{book_id_str}-images.html"
        td_list = row.find_all('td')
        book_title = td_list[3].find('a').text
        print(f"{book_id_str}: {book_title} : {book_url}")

        # Fetching book content
        book_response = requests.get(book_url)
        book_html_content = book_response.text

        # Check if content contains tables
        if contains_table(book_html_content):
            print("This book contains tables.")

        # Check for non-UTF-8/ASCII characters
        if contains_non_ascii(book_html_content):
            print("This book contains non-UTF-8/ASCII characters.")

        # Store book information
        book_info = {"id": book_id_str, "title": book_title, "url": book_url}
        books_info.append(book_info)
        book_id += 1  # increment book_id for the next book

# Write book information to a JSON file
with open("books_info.json", "w") as json_file:
    json.dump(books_info, json_file)
