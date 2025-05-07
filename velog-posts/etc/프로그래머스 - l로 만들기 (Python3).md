# 프로그래머스 - l로 만들기 (Python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-l%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python3)

🗓 작성일: Mon, 28 Apr 2025 09:14:22 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/9794006b-a510-410b-ad67-7bf7bed0fa00/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 알파벳 순서에서 &quot;l&quot;보다 앞서는 모든 문자를 &quot;l&quot;로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.</p>
<hr />
<h3 id="내코드">내코드</h3>
<pre><code>def solution(myString):
    answer = ''
    for ch in myString:
        if ch &lt; 'l':
            answer += 'l'
        else:
            answer += ch
    return answer</code></pre>