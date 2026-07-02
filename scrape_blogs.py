import requests
from bs4 import BeautifulSoup
import json

url = 'https://plastroots.com/category/blog-articles/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')
blogs = []

for article in articles:
    title_tag = article.find('h2') or article.find('h3')
    title = title_tag.text.strip() if title_tag else ''
    
    link_tag = article.find('a')
    link = link_tag['href'] if link_tag else ''
    
    img_tag = article.find('img')
    img_src = img_tag['src'] if img_tag else ''
    
    excerpt_tag = article.find('div', class_='entry-content') or article.find('p')
    excerpt = excerpt_tag.text.strip() if excerpt_tag else ''
    
    if title and link:
        blogs.append({
            'title': title,
            'link': link,
            'image': img_src,
            'excerpt': excerpt
        })

with open('src/data/BlogData.js', 'w', encoding='utf-8') as f:
    f.write('export const blogsData = ')
    json.dump(blogs, f, indent=2)
    f.write(';\n')

print(f"Scraped {len(blogs)} blogs.")
