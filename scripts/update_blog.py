import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@tjeudeud'

# 깃허브 레포지토리 경로
repo_path = '.'

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거
    file_name = entry.title.replace('/', '-').replace('\\', '-')
    file_name += '.md'

    # 태그 목록 가져오기 (없으면 'etc'로 저장)
    if 'tags' in entry and entry.tags:
        tag = entry.tags[0]['term']  # 첫 번째 태그만 사용
    else:
        tag = 'etc'

    # 태그 기반 폴더 생성
    tag_dir = os.path.join(repo_path, 'velog-posts', tag)
    os.makedirs(tag_dir, exist_ok=True)

    # 파일 경로 결정
    file_path = os.path.join(tag_dir, file_name)

    # 새 파일일 경우에만 생성하고 커밋
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {entry.title}\n\n")
            file.write(f"🔗 [원문 링크]({entry.link})\n\n")
            file.write(f"🗓 작성일: {entry.published}\n\n"            file.write(entry.description)

        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title} [tag: {tag}]')

# 변경 사항 푸시
repo.git.push()
