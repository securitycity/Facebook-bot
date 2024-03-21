from facebook import GraphAPI
import re

access_token = ''
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

# Get comments from a post (replace 'POST_ID' with the actual post ID)
post_id = 'POST_ID'
comments = graph.get_connections(post_id, 'comments')

# Save usernames and emails to a text file
with open('user_info.txt', 'w') as file:
    for comment in comments['data']:
        username, email = extract_user_info(comment['message'])
        if username and email:
            file.write(f'Username: {username}, Email: {email}\n')
            # Send a direct message to the user
            graph.send_message(user_id=comment['from']['id'], message="Hello! We found your comment.")
