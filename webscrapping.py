import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and print article titles (modify the selector as needed)
        titles = soup.find_all('h2')  # Change tag as per website structure
        
        print("Article Titles:")
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title.get_text(strip=True)}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
url = "https://example.com"  # Replace with the target website
scrape_website(url)

