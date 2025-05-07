<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/68669929-a9f8-48fc-a3f3-94a1e50ab4c9/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 배열 arr과 delete_list가 있습니다. arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.</p>
<hr />
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(arr, delete_list):
    return [ch for ch in arr if ch not in delete_list]</code></pre>