# 프로그래머스 - 문자열 바꿔서 찾기 (python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B0%94%EA%BF%94%EC%84%9C-%EC%B0%BE%EA%B8%B0-python3)

🗓 작성일: Mon, 28 Apr 2025 09:21:31 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/90de2cf6-ed24-4b27-9056-a051460d14b4/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>문자 &quot;A&quot;와 &quot;B&quot;로 이루어진 문자열 myString과 pat가 주어집니다. myString의 &quot;A&quot;를 &quot;B&quot;로, &quot;B&quot;를 &quot;A&quot;로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.</p>
<hr />
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(myString, pat):
    converted = ''.join('B' if ch == 'A' else 'A' for ch in myString)
    return 1 if pat in converted else 0</code></pre>