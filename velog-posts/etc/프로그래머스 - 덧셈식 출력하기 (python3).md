# 프로그래머스 - 덧셈식 출력하기 (python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8D%A7%EC%85%88%EC%8B%9D-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0-python3)

🗓 작성일: Mon, 28 Apr 2025 08:29:57 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/955ac803-50ce-44a0-8e64-4c25d2cbf0da/image.png" /></p>
<p>문제 설명
두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.</p>
<blockquote>
<p>a + b = c</p>
</blockquote>
<hr />
<h3 id="내-코드">내 코드</h3>
<pre><code>a, b = map(int, input().strip().split(' '))
print(f&quot;{a} + {b} = {a + b}&quot;)</code></pre>