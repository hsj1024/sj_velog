# 프로그래머스 - 배열만들기 1 (python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%B0%EC%97%B4%EB%A7%8C%EB%93%A4%EA%B8%B0-1-python3)

🗓 작성일: Thu, 24 Apr 2025 15:42:32 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/7dae95c4-5b9e-482b-9b23-5b1332253682/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(n, k):
    result = []
    for i in range(1, n+1):
        if i % k == 0:
            result.append(i)
    return result</code></pre><hr />
<h3 id="다른-사람의-풀이">다른 사람의 풀이</h3>
<pre><code>def solution(n, k):
    return [i for i in range(k,n+1,k)]
</code></pre><p>1부터 시작 안해도 되는 걸 이 분의 풀이를 보고 깨달아버렸다.
더 분발해야지..!</p>