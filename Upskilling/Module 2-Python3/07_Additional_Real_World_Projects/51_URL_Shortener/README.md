# Exercise 51 - URL Shortener

## Objective

Use dictionaries, hashing, classes, and modules to build a simple URL shortening service.

## Task

Create a basic URL shortener that can shorten URLs and retrieve the original URL.

## Instructions

- Import the `hashlib` module.
- Create a `URLShortener` class with dictionary storage.
- Generate a 6-character hash from the URL.
- Implement URL lookup (redirect simulation).

## Project Structure

- `Exercise_51.py` - Python source code
- `51_output.png` - Program output screenshot

## Code

```python
import hashlib

class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten_url(self, url):
        short_code = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short_code] = url
        return short_code

    def get_original_url(self, short_code):
        return self.urls.get(short_code, "URL not found.")


shortener = URLShortener()

original_url = "https://www.example.com/products/item123"

short_code = shortener.shorten_url(original_url)

print("Original URL:")
print(original_url)

print("\nShort Code:")
print(short_code)

print("\nRetrieved URL:")
print(shortener.get_original_url(short_code))
```

## Expected Output

```
Original URL:
https://www.example.com/products/item123

Short Code:
a1b2c3

Retrieved URL:
https://www.example.com/products/item123
```