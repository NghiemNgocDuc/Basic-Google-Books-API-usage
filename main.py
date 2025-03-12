import requests
def get_book_recommendations(query):
    api_key = 'GET https://www.googleapis.com/books/v1/volumes?q=flowers&filter=free-ebooks&key=AIzaSyB4Hd1CQSBRdEOd1r4CTlz5Sg2wwzYEjKE'  # Replace with your API key
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        books = response.json().get('items', [])
        for book in books: title = book['volumeInfo'].get('title', 'N/A')
        authors = book['volumeInfo'].get('authors', ['N/A'])
        print(f"Title: {title}, Authors: {', '.join(authors)}")
    else:
        print(f"Failed to retrieve book recommendations. Status code: {response.status_code}, Response: {response.text}")

user_book = "Fiction"
get_book_recommendations(user_book)

