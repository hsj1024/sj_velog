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