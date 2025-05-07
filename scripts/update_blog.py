import feedparser
import os
from datetime import datetime

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@tjeudeud'

# 로컬 저장 경로
repo_path = '.'

# RSS 파싱
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    # 날짜 + 제목 기반 파일명
    pub_date = datetime(*entry.published_parsed[:3]).strftime('%Y-%m-%d')
    title = entry.title.replace('/', '-').replace('\\', '-').strip()
    file_name = f"{pub_date}_{title}.md"

    # 태그 분류
    if "프로그래머스" in title:
        tag = "Programmers"
    elif "백준" in title:
        tag = "Baekjoon"
    else:
        tag = "etc"

    # 경로 구성
    tag_dir = os.path.join(repo_path, 'velog-posts', tag)
    os.makedirs(tag_dir, exist_ok=True)
    file_path = os.path.join(tag_dir, file_name)

    # 파일이 없을 경우 저장
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {entry.title}\n\n")
            file.write(f"🔗 [원문 링크]({entry.link})\n\n")
            file.write(f"🗓 작성일: {entry.published}\n\n")
            file.write(entry.description)
        print(f"✅ 새 글 저장됨: {file_path}")
