# 백준 9776번 Max Volume - python

🔗 [원문 링크](https://velog.io/@tjeudeud/%EB%B0%B1%EC%A4%80-9776%EB%B2%88-Max-Volume-python)

🗓 작성일: 2025-05-07 16:37:43 KST

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/6c7eb082-8c16-4e04-951d-c3fc2b244182/image.png" /></p>
<blockquote>
<p>부피 계산 공식 문제 / 구현 / 실수 조심</p>
</blockquote>
<h3 id="📘-문제-설명">📘 문제 설명</h3>
<p>3차원 도형(구, 원뿔, 원기둥)의 부피를 각각 계산한 후,<br /><strong>가장 큰 부피를 소수점 셋째 자리까지 출력</strong>하는 문제이다.</p>
<h3 id="🔹-입력-형식">🔹 입력 형식</h3>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/d3402ed8-8cef-4c65-a23a-6fd000cd428d/image.png" /></p>
<ul>
<li>첫 줄: 도형의 개수 <code>n (1 ≤ n ≤ 100)</code></li>
<li>이후 <code>n</code>줄:<ul>
<li><code>S r</code> : 구 (Sphere)</li>
<li><code>C r h</code> : 원뿔 (Cone)</li>
<li><code>L r h</code> : 원기둥 (Cylinder)</li>
</ul>
</li>
</ul>
<h3 id="🔹-출력-형식">🔹 출력 형식</h3>
<ul>
<li>가장 큰 부피를 <strong>소수점 셋째 자리까지</strong> 출력</li>
</ul>
<blockquote>
<p>주의  ⚠️
 math.pi 대신 π = 3.14159 고정 사용해야 정답 처리된다.</p>
</blockquote>
<hr />
<br />
<h4>📌 도형별 부피 공식</h4>
<table style="width: 100%; text-align: left;">
  <thead>
    <tr>
      <th>도형</th>
      <th>공식</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>구 (Sphere)</td>
      <td>(4/3) × π × r³</td>
    </tr>
    <tr>
      <td>원기둥 (L)</td>
      <td>π × r² × h</td>
    </tr>
    <tr>
      <td>원뿔 (C)</td>
      <td>(1/3) × π × r² × h</td>
    </tr>
  </tbody>
</table>

<br />
<br />

<hr />
<blockquote>
<p>문제 접근 💡 </p>
</blockquote>
<ul>
<li>입력을 split()으로 받아 도형을 판별하고</li>
<li>조건문으로 부피 계산 후 max_volume에 저장</li>
<li>마지막에 소수점 셋째 자리까지 출력</li>
</ul>
<hr />
<h3 id="🧾-풀이-코드-python">🧾 풀이 코드 (Python)</h3>
<pre><code>PI = 3.14159
n = int(input())
max_volume = 0

for _ in range(n):
    data = input().split()
    shape = data[0]

    if shape == 'S':
        r = float(data[1])
        volume = (4/3) * PI * r**3
    elif shape == 'L':
        r, h = map(float, data[1:])
        volume = PI * r**2 * h
    elif shape == 'C':
        r, h = map(float, data[1:])
        volume = (1/3) * PI * r**2 * h

    max_volume = max(max_volume, volume)

print(f&quot;{max_volume:.3f}&quot;)
</code></pre>