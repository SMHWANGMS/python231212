#네이버블로그.py
import requests
from bs4 import BeautifulSoup

def naver_blog_crawler(search_keyword):
    base_url = "https://search.naver.com/search.naver"
    params = {
        'where': 'view',
        'sm': 'tab_jum',
        'query': search_keyword,
    }

    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    blog_posts = soup.select('li.sh_blog_top')

    for post in blog_posts:
        blog_name = post.select_one('a.txt84').get_text(strip=True)
        blog_url = post.select_one('a.url').get('href')
        title = post.select_one('a.sh_blog_title').get_text(strip=True)
        date = post.select_one('span.txt_inline').get_text(strip=True)

        print(f"블로그명: {blog_name}")
        print(f"블로그주소: {blog_url}")
        print(f"제목: {title}")
        print(f"포스팅날짜: {date}")
        print("\n")

if __name__ == "__main__":
    search_keyword = input("검색어를 입력하세요: ")
    naver_blog_crawler(search_keyword)
