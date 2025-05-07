# 프로그래머스 - 문자열 돌리기 (python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0-python3)

🗓 작성일: Mon, 28 Apr 2025 08:27:30 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/e32f1b55-d747-49e1-a5c8-9da4821e2565/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>문자열 str이 주어집니다.
문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>str = input()
for i in range(len(str)):
    print(str[i])</code></pre>