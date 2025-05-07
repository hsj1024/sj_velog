<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/7ce7f16e-62ad-46a0-bfb1-3e8c544dfe5d/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 n과 문자열 control이 주어집니다. control은 &quot;w&quot;, &quot;a&quot;, &quot;s&quot;, &quot;d&quot;의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.</p>
<p>&quot;w&quot; : n이 1 커집니다.
&quot;s&quot; : n이 1 작아집니다.
&quot;d&quot; : n이 10 커집니다.
&quot;a&quot; : n이 10 작아집니다.
위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(n, control):
    for ch in control:
        if ch == 'w': n+= 1
        elif ch == 's': n-= 1
        elif ch == 'd': n+= 10
        elif ch == 'a': n-=10
    return n</code></pre>