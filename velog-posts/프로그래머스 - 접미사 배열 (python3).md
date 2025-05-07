<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/3ff4da4b-8534-40e8-9f97-deb790e66aea/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, &quot;banana&quot;의 모든 접미사는 &quot;banana&quot;, &quot;anana&quot;, &quot;nana&quot;, &quot;ana&quot;, &quot;na&quot;, &quot;a&quot;입니다.
문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.</p>
<h3 id="❗️-접근-방법">❗️ 접근 방법</h3>
<blockquote>
<p>❓ 접미사란?
= 뒤에서부터 잘라낸 문자열</p>
</blockquote>
<p>즉, 접미사들을 전부 뽑아서
사전순으로 정렬된 배열을 리턴하라는 뜻</p>
<p>슬라이싱을 이용하면 간단 !</p>
<p>알파벳 정렬은 sorted 를 활용하자.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(my_string):
    return sorted([my_string[i:] for i in range(len(my_string))])
</code></pre>