<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/c823a474-ad67-4772-b099-6b30ad9e8ce0/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(start_num, end_num):
    result = []
    for i in range(end_num,start_num+1):
        result.append(i)
        result.sort(reverse=True)
    return result</code></pre><hr />
<h3 id="다른사람의-풀이-1">다른사람의 풀이 1</h3>
<pre><code>
def solution(start, end):
    return list(range(start,end-1,-1))</code></pre><h3 id="다른사람의-풀이-2">다른사람의 풀이 2</h3>
<pre><code>
def solution(start, end):
    return [i for i in range(start,end-1,-1)]</code></pre>