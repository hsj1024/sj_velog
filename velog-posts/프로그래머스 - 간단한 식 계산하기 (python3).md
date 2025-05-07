<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/efbacf13-ef7a-43f4-acca-91315a82a75d/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>문자열 binomial이 매개변수로 주어집니다. binomial은 &quot;a op b&quot; 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.</p>
<hr />
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(binomial):
    if '+' in binomial:
        parts = binomial.split('+')
        return int(parts[0].strip()) + int(parts[1].strip())
    elif '-' in binomial:
        parts = binomial.split('-')
        return int(parts[0].strip()) - int(parts[1].strip())
    elif '*' in binomial:
        parts = binomial.split('*')
        return int(parts[0].strip()) * int(parts[1].strip())</code></pre><h3 id="다른-사람의-풀이-1">다른 사람의 풀이 1</h3>
<pre><code>def solution(binomial):
    a, op, b = binomial.split()

    a = int(a)
    b = int(b)

    if op == &quot;+&quot;:
        result = a + b
    elif op == &quot;-&quot;:
        result = a - b
    elif op == &quot;*&quot;:
        result = a * b

    return result</code></pre><h3 id="다른-사람의-풀이-2">다른 사람의 풀이 2</h3>
<pre><code>def solution(binomial):
    return eval(binomial)
</code></pre>