<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/a090b247-1b01-4d95-9b23-f606712dca74/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 &quot;w&quot;, &quot;a&quot;, &quot;s&quot;, &quot;d&quot;로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.</p>
<p>&quot;w&quot; : 수에 1을 더한다.
&quot;s&quot; : 수에 1을 뺀다.
&quot;d&quot; : 수에 10을 더한다.
&quot;a&quot; : 수에 10을 뺀다.
그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.</p>
<p>주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        diff = numLog[i] - numLog[i-1] # 두 수의 차이
        if diff == 1:
            answer+= 'w'
        elif diff == -1:
            answer+= 's'
        elif diff == 10:
            answer+= 'd'
        else:
            answer+= 'a'
    return answer</code></pre>