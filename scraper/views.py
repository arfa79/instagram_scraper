from django.shortcuts import render
from scraper.instagram_scraper import scrape_profile

def influencer_detail(request, username):
    follower_count, posts = scrape_profile(username)
    if follower_count is not None and posts:
        context = {
            'username': username,
            'follower_count': follower_count,
            'posts': posts
        }
        return render(request, 'scraper/influencer_detail.html', context)
    else:
        return render(request, 'scraper/error.html')