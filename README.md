# Gutenberg-Scraper

This Python script scrapes book details from Project Gutenberg's website based on different options and checks for the presence of tables and non-UTF-8/ASCII characters in each book's content.

## Requirements

- Python 3.x
- Libraries: requests, BeautifulSoup

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Buddhadip/Gutenberg-Scraper.git
cd Gutenberg-Scraper
```
2. Install the required libraries
```bash
pip install -r requirements.txt
```

## Usage
- Run the script scraper.py.
- The script will fetch data from Gutenberg's website and create a JSON file (books_info.json) containing book details and links.
- Check the console output for any books containing tables or non-UTF-8/ASCII characters.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License
- This project is licensed under the MIT License
