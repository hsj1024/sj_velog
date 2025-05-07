import feedparser
import git
import os
from bs4 import BeautifulSoup
from datetime import datetime

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@tjeudeud'

# 깃허브 레포지토리 경로
repo_path = '.'
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    # 작성일 파싱 및 파일명용 포맷
    pub_date = datetime(*entry.published_parsed[:3]).strftime('%Y-%m-%d')

    # 제목 정리
    title = entry.title.replace('/', '-').replace('\\', '-').strip()
    file_name = f"{pub_date}_{title}.md"

    # 본문에서 태그 추출
    soup = BeautifulSoup(entry.description, 'html.parser')
    tags = [tag.text.strip() for tag in soup.find_all('a', class_='tag')]
    tag = tags[0] if tags else 'etc'

    # 폴더 경로 구성
    tag_dir = os.path.join(repo_path, 'velog-posts', tag)
    os.makedirs(tag_dir, exist_ok=True)

    file_path = os.path.join(tag_dir, file_name)

    # 파일이 없으면 저장 및 커밋
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {entry.title}\n\n")
            file.write(f"🔗 [원문 링크]({entry.link})\n\n")
            file.write(f"🗓 작성일: {entry.published}\n\n")
            file.write(entry.description)

        print(f"✅ 새 글 저장됨: {file_path}")
        repo.git.add(file_path)
        repo.git.commit('-m', f"Add post: {entry.title} [tag: {tag}]")

# 변경사항이 있을 경우에만 푸시
if repo.is_dirty(untracked_files=True):
    print("🚀 변경사항 감지됨 → 푸시 중...")
    repo.git.push()
else:
    print("✅ 변경 없음 → 푸시 생략")
