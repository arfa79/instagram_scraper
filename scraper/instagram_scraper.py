import requests
from bs4 import BeautifulSoup

def parse_followers(follower_count_text):
    print("Follower count text:", follower_count_text)
    if 'k' in follower_count_text.lower():
        print("Found 'k' in follower count text")
        return int(float(follower_count_text.replace('k', '').replace('K', '')) * 1000)
    elif 'm' in follower_count_text.lower():
        print("Found 'm' in follower count text")
        return int(float(follower_count_text.replace('m', '').replace('M', '')) * 1000000)
    else:
        print("No 'k' or 'm' in follower count text")
        return int(follower_count_text.replace(',', ''))

def scrape_profile(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        follower_count_element = soup.find('meta', property='og:description')
        if follower_count_element:
            follower_count_text = follower_count_element.attrs['content']
            print("Follower count text before parsing:", follower_count_text)
            follower_count = parse_followers(follower_count_text.split()[0])
            print("Parsed follower count:", follower_count)
            posts = []
            post_elements = soup.find_all('div', class_='v1Nh3')
            for post_element in post_elements:
                post = {}
                post['likes'] = int(post_element.find('span', class_='zV_Nj').text.replace(',', ''))
                # Extract views count if available
                views_element = post_element.find('span', class_='vcOH2')
                if views_element:
                    post['views'] = int(views_element.text.replace(' views', '').replace(',', ''))
                else:
                    post['views'] = None
                # Extract comments count if available
                comments_element = post_element.find('span', class_='u_cDk')
                if comments_element:
                    post['comments'] = int(comments_element.text.replace(',', ''))
                else:
                    post['comments'] = None
                posts.append(post)
            return follower_count, posts
    return None, None