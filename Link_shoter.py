from urllib.parse import urlparse, urlunparse

def change_url_path(url, new_path):
    parsed_url = urlparse(url)
    # Replace the path with the new path
    modified_url = parsed_url._replace(path=new_path)
    # Construct the modified URL
    final_url = urlunparse(modified_url)
    return final_url

# Example usage:
original_url = "https://4zygbmwzrnj7rgbg7w3elg.on.drv.tw/www.shreyasw.com/"
new_path = "shreyas"
modified_url = change_url_path(original_url, new_path)
print(f"Modified URL: {modified_url}")
