# 프로그래머스 - 순서바꾸기 (python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%84%9C%EB%B0%94%EA%BE%B8%EA%B8%B0)

🗓 작성일: Thu, 24 Apr 2025 15:06:00 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/b0dfb1f6-ee3f-4513-9bc6-db920587a99d/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 리스트 num_list와 정수 n이 주어질 때, num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(num_list, n):
    return num_list[n:] + num_list[:n]
</code></pre><blockquote>
</blockquote>
<p>num_list[n:] → n번째 이후
num_list[:n] → 앞부분
리스트 붙이기만 하면 끝!</p>