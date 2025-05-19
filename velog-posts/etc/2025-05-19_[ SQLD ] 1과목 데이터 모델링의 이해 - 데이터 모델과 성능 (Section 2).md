# [ SQLD ] 1과목 데이터 모델링의 이해 - 데이터 모델과 성능 (Section 2)

🔗 [원문 링크](https://velog.io/@tjeudeud/SQLD-1%EA%B3%BC%EB%AA%A9-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8%EB%A7%81%EC%9D%98-%EC%9D%B4%ED%95%B4-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8%EA%B3%BC-%EC%84%B1%EB%8A%A5-Section-2)

🗓 작성일: 2025-05-19 15:53:56 KST

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/848ceafd-112c-4328-8654-bbc951796cd6/image.png" /></p>
<blockquote>
<h2 id="point-1---정규화"><em>Point 1 - 정규화</em></h2>
</blockquote>
<ul>
<li><strong>정규화는 데이터의 일관성, 최소한의 데이터 중복, 최대한의 데이터 유연성을 위한 방법이며 데이터를 분해하는 과정이다.</strong></li>
<li>정규화는 데이터 중복을 제거하고 데이터모델의 독립성을 확보하기 위한 방법이다.</li>
<li>정규화를 수행하면 비즈니스에 변화가 발생하여도 데이터 모델의 변경을 최소화할 수가 있다.</li>
<li>정규화는 제 1 정규화 부터 제 5 정규화 까지 있지만, <span style="background-color: #fff5b1; color: black;">실질적으로는 제 3정규화까지만 수행한다.</span></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/1d104e7c-84e2-4c88-896b-443ca3412dda/image.jpg" /></p>
<ul>
<li>위의 테이블은 정규화를 수행하지 않은 것으로, 부서 테이블과 직원 테이블을 하나로 합쳐둔 것이다. <br /> 만약 위의 테이블에서 새로운 직원이 추가되는 경우 부서 정보가 없으면 부서코드를 임의이 값으로 넣어야한다.<br /> 즉, <span style="background-color: white; color: red;">  <strong>불필요한 정보</strong> </span>가 같이 추가되는 것이다.</li>
<li>또한 새로운 '총무부' 가 추가되어야 할 경우 사원 정보가 없기 떄문에 임의의 값으로 사원번호를 입력하거나 추가할 수 없게 된다. <br /> 이러한 문제를 <span style="background-color: #fff5b1; color: black;"><strong>이상현상(Anomarly)</strong></span> 이라고 한다.</li>
<li>위와 같은 문제를 해결하기 위해서는 테이블을 분해해야한다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/7586e255-7a20-4541-a126-29cede10b1da/image.jpg" /></p>
<ul>
<li><p>정규화된 모델은 테이블이 분해된다. 테이블이 분해되면 직원 테이블과 부서 테이블 간에 부서코드로 <strong>조인(Join)</strong>을 수행하여 하나의 합집합으로 만들 수도 있다.</p>
</li>
<li><p>정규화를 수행하면 불필요한 데이터를 입력하지 않아도 되기 때문에 중복 데이터가 제거된다.(완전히 제거는 아님)</p>
</li>
<li><h4 id="정규화-절차">정규화 절차</h4>
<table>
<thead>
<tr>
<th>정규화 절차</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>제1 정규화</strong></td>
<td align="left">- 속성(Attribute)의 원자성을 확보한다. <br /> - 기본키(Primary) 를 설정한다.</td>
</tr>
<tr>
<td><strong>제2 정규화</strong></td>
<td align="left"><strong>기본키가 2개 이상의 속성으로 이루어진 경우, 부분 함수 종속성을 제거(분해)한다.</strong></td>
</tr>
<tr>
<td><strong>제3 정규화</strong></td>
<td align="left">- 기본키를 제외한 칼럼 간에 종속성을 제거한다. <br /> - 즉, 이행 함수 종속성을 제거한다.</td>
</tr>
<tr>
<td><strong>BCNF</strong></td>
<td align="left">- <strong>기본키를 제외하고 후보키가 있는 경우, 후보키가 기본키를 종속시키면 분해한다.</strong></td>
</tr>
<tr>
<td><strong>제4 정규화</strong></td>
<td align="left">- <strong>여러 칼럼들이 하나의 칼럼을 종속시키는 경우 분해하여 다중 값 종속성을 제거한다.</strong></td>
</tr>
<tr>
<td><strong>제5 정규화</strong></td>
<td align="left">- <strong>조인에 의해서 종속성이 발생되는 경우 분해한다.</strong></td>
</tr>
</tbody></table>
</li>
</ul>
<h3 id="2️⃣-함수적-종속성functional-dependency">2️⃣ 함수적 종속성(Functional Dependency)</h3>
<h4 id="1-제-1-정규화">(1) 제 1 정규화</h4>
<ul>
<li>정규화는 함수적 종속성을 근거로 한다. 함수적 종속성이란 X-&gt; Y 이면 Y는 X에 함수적으로 종속한다고 말한다.</li>
<li>함수적 종속성은 X가 변화하면 Y도 변화하는지 확인한다. 예를 들어 회원ID가 변화하면 이름도 변경될 것이다. 이런 경우 회원ID가 기본키가 되고, 회원 ID가 이름을 함수적으로 종속한다고 한다.</li>
</ul>
<p>P 65 부터 to be continue</p>