# 프로그래머스 - 배열의 원소 삭제하기 (python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%B0%EC%97%B4%EC%9D%98-%EC%9B%90%EC%86%8C-%EC%82%AD%EC%A0%9C%ED%95%98%EA%B8%B0-python3)

🗓 작성일: Mon, 28 Apr 2025 09:31:52 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/68669929-a9f8-48fc-a3f3-94a1e50ab4c9/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 배열 arr과 delete_list가 있습니다. arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.</p>
<hr />
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(arr, delete_list):
    return [ch for ch in arr if ch not in delete_list]</code></pre>