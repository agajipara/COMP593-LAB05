import requests

def create_paste(title, body_text, expiration='30D', public=True):
    """
    Creates a new PasteBin paste.

    Args:
        title (str): The title of the paste.
        body_text (str): The body text of the paste.
        expiration (str): Expiration period for the paste (e.g., '10M', '1H', '1D').
        public (bool): Whether the paste is publicly listed.

    Returns:
        str: The URL of the newly created paste if successful, None otherwise.
    """
    pastebin_url = "https://pastebin.com/api/api_post.php"
    api_dev_key = 'dUkt5TOypZRohNMSfFrM3aFhs82MVyxz' 

    data = {
        'api_dev_key': api_dev_key,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': '0' if public else '1'
    }

    print(f"Creating new paste with title '{title}'...")
    response = requests.post(pastebin_url, data=data)

    if response.status_code == 200:
        print("Paste created successfully!")
        return response.text
    else:
        print(f"Failed to create paste. Response code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# Test the function
if __name__ == "__main__":
    paste_title = "Test Paste"
    paste_body_text = "This is a test paste."
    paste_expiration = "10M"
    paste_public = True

    paste_url = create_paste(
        title=paste_title,
        body_text=paste_body_text,
        expiration=paste_expiration,
        public=paste_public
    )

    if paste_url:
        print(f"Paste URL: {paste_url}")
    else:
        print("Failed to create paste.")