# 프로그래머스 - 배열 만들기 3 (python3)

🔗 [원문 링크](https://velog.io/@tjeudeud/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%B0%EC%97%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-3)

🗓 작성일: Thu, 24 Apr 2025 15:15:36 GMT

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/c509df30-8ce1-49e0-942b-d4a74015ba64/image.png" /></p>
<h3 id="문제-설명">문제 설명</h3>
<p>정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.</p>
<p>intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.</p>
<p>이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.</p>
<h3 id="내-코드">내 코드</h3>
<pre><code>def solution(arr, intervals):
    result = []
    for start, end in intervals:
        result += arr[start:end+1] 
    return result</code></pre>