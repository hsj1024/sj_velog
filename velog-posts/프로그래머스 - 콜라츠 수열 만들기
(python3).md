<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/a8dd8359-1ece-4197-acf4-76effce1424d/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.</p>
<p>그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.</p>
<p>계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.</p>
<p>임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 초기값이 n인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(n):
    if n == 1: return [1]
    if n % 2 == 0: return [n] + solution(n // 2)
    else: return [n] + solution(n * 3 + 1)</code></pre><p>재귀를 활용해서 코드를 작성해봤다.</p>