from facebook import GraphAPI
import re
import requests

# Proxy configuration
proxy = {
    'http': 'http://81.91.139.76:8080',
    'http': 'http://79.110.201.235:8081'
}

access_token = '1075145793594113|5TKgEe3R_YuZkz8KWGeZ-oFOOP0'
graph = GraphAPI(access_token)

# Function to extract usernames and emails from comments
def extract_user_info(comment):
    pattern = r'(\w+)@(\w+\.\w+)'
    match = re.search(pattern, comment)
    if match:
        username = match.group(1)
        email = match.group(0)
        return username, email
    else:
        return None, None


def main():
    ##defining the main function
    # Get comments from a post (replace 'POST_ID' with the actual post ID)
    post_id = 'dddvsyebhee'

    # Using a proxy with requests
    session = requests.Session()
    session.proxies.update(proxy)
    comments = session.get(f'https://graph.facebook.com/v12.0/{post_id}/comments', params={'access_token': access_token}).json()
    # Save usernames and emails to a text file
    with open('user_info.txt', 'w') as file:
        for comment in comments['data']:
            username, email = extract_user_info(comment['message'])
            if username and email:
                file.write(f'Username: {username}, Email: {email}\n')
                # Send a direct message to the user
                graph.send_message(user_id=comment['from']['id'], message="Hello! We found your comment.")

main()
