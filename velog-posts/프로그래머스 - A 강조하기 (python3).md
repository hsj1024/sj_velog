<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/8da1ba85-895e-4c16-aad3-c518a158f259/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>문자열 myString이 주어집니다. myString에서 알파벳 &quot;a&quot;가 등장하면 전부 &quot;A&quot;로 변환하고, &quot;A&quot;가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.</p>
<hr />
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(myString):
    result = &quot;&quot;
    for ch in myString:
        if ch == 'a':
            result += 'A'
        elif ch.isupper() and ch != 'A':
            result += ch.lower()
        else:
            result += ch
    return result</code></pre><h3 id="다른사람의-코드">다른사람의 코드</h3>
<pre><code>def solution(myString):
    return myString.lower().replace('a','A')</code></pre>