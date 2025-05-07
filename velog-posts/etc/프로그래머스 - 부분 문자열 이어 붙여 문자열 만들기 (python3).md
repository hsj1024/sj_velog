# 프로그래머스 - 부분 문자열 이어 붙여 문자열 만들기 (python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9D%B4%EC%96%B4-%EB%B6%99%EC%97%AC-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-python3)

🗓 작성일: Thu, 24 Apr 2025 16:18:15 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/642c635a-7f65-4910-a469-8bee1b1948d8/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(my_strings, parts):
    result = ''
    for i in range(len(my_strings)):
        s,e = parts[i]
        result += my_strings[i][s:e+1]
    return result</code></pre><hr />
<h3 id="다른-풀이-1">다른 풀이 1</h3>
<pre><code>def solution(my_strings, parts):
    answer = &quot;&quot;
    for word, (s, e) in zip(my_strings, parts):
        answer += word[s:e+1]
    return answer
</code></pre><p>이 방법은 zip() 을 활용해서 푸는 방법이다.</p>
<blockquote>
<p>✅ zip()이란?</p>
</blockquote>
<ul>
<li>여러 개의 리스트(또는 반복 가능한 객체)를 '쌍'으로 묶어주는 함수.</li>
<li>zip(my_strings, parts)는 각 리스트의 같은 인덱스끼리 묶어서 튜플을 만들어 준다.</li>
</ul>
<p><strong>즉 zip 을 사용하면? (문제의 입출력 예 1번 기반)</strong></p>
<pre><code>[
  (&quot;progressive&quot;, [0, 4]),
  (&quot;hamburger&quot;, [1, 2]),
  (&quot;hammer&quot;, [3, 5]),
  (&quot;ahocorasick&quot;, [7, 7])
]
</code></pre><p>-&gt; 이런 형태로 저장이 되는 것이다. </p>
<p><em>*<em>풀어서 설명해보면
*</em></em></p>
<blockquote>
<p>word = progressive -&gt; [0,4] =&gt; word[0:4] -&gt; prog
word = hamburger   -&gt; [1,2] =&gt; word[1:2] -&gt; a
word = hammer      -&gt; [3,5] =&gt; word[3:5] -&gt; me
word = ahocorasick -&gt; [7,7] =&gt; word[7:7] -&gt; X</p>
</blockquote>
<h3 id="❗️-근데-❗️">❗️ 근데 ❗️</h3>
<p>우리는 문제에서 s 부터 e 까지니까 +1을 해서
*<em><em>answer += word[s:e+1]</em> 을 해주게 되면?
*</em></p>
<blockquote>
<p>word = progressive -&gt; [0,4] =&gt; word[0:4] -&gt; progr
word = hamburger   -&gt; [1,2] =&gt; word[1:2] -&gt; am
word = hammer      -&gt; [3,5] =&gt; word[3:5] -&gt; mer
word = ahocorasick -&gt; [7,7] =&gt; word[7:7] -&gt; s</p>
</blockquote>
<p>즉, programmers 가 나오게 됨</p>
<hr />
<h3 id="다른-풀이-2">다른 풀이 2</h3>
<h4 id="리스트-컴프리헨션--join으로도-가능">리스트 컴프리헨션 + join()으로도 가능</h4>
<pre><code>def solution(my_strings, parts):
    return ''.join(word[s:e+1] for word, (s, e) in zip(my_strings, parts))</code></pre>