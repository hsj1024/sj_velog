# scripts/update_blog.py
import feedparser
import os
import re
from datetime import datetime, timedelta, timezone

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@tjeudeud'

# 로컬 저장 경로
repo_path = '.'

# KST (UTC+9) 시간대 정의
kst = timezone(timedelta(hours=9))

# RSS 파싱
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    # 날짜 + 제목 기반 파일명 (KST 기준)
    pub_date = datetime(*entry.published_parsed[:3], tzinfo=timezone.utc).astimezone(kst).strftime('%Y-%m-%d')
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
        published_kst = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc).astimezone(kst).strftime('%Y-%m-%d %H:%M:%S KST')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {entry.title}\n\n")
            file.write(f"🔗 [원문 링크]({entry.link})\n\n")
            file.write(f"🗓 작성일: {published_kst}\n\n")
            file.write(entry.description)
        print(f"✅ 새 글 저장됨: {file_path}")

# timestamp 저장 (KST)
timestamp = datetime.now(kst).strftime("📌 최근 실행 시간: <!--LAST_UPDATED-->%Y-%m-%d %H:%M:%S KST<!--/LAST_UPDATED-->")
timestamp_path = os.path.join(repo_path, 'velog-posts', 'last_updated.txt')
with open(timestamp_path, 'w') as f:
    f.write(timestamp)

# README 자동 시간 반영
readme_path = os.path.join(repo_path, 'README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as file:
        readme = file.read()
    updated_readme = re.sub(r"📌 최근 실행 시간: <!--LAST_UPDATED-->.*?<!--/LAST_UPDATED-->", timestamp, readme)
    if updated_readme != readme:
        with open(readme_path, 'w', encoding='utf-8') as file:
            file.write(updated_readme)
        print("📝 README.md 실행 시간 업데이트됨.")
