from django.core.management.base import BaseCommand
from scraper.instagram_scraper import scrape_profile

class Command(BaseCommand):
    help = 'Scrape data from Instagram'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Instagram username')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        follower_count, posts = scrape_profile(username)
        if follower_count is not None and posts:
            self.stdout.write(self.style.SUCCESS(f"Followers count for {username}: {follower_count}"))
            for i, post in enumerate(posts, start=-1):
                likes = post.get('likes', 'N/A')
                views = post.get('views', 'N/A')
                comments = post.get('comments', 'N/A')
                self.stdout.write(f"Post {i}: Likes - {likes}, Views - {views}, Comments - {comments}")
        else:
            self.stdout.write(self.style.ERROR(f"Failed to fetch data for {username}"))