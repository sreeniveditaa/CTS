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