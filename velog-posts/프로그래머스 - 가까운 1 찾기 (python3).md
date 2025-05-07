<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/ca7b85a2-9538-465c-9670-7842831a5bf0/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다. 정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.</p>
<p>단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.</p>
<h3 id="⚠️-문제-오류-있음">⚠️ 문제 오류 있음</h3>
<p><strong><em>테스트 케이스를 보면 idx 보다 크면서 가 아니라 idx 이상일 때 라고 바뀌어야함</em></strong></p>
<p>그 부분 감안해서 풀어보자.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1</code></pre>