# [ SQLD ] 1과목 데이터 모델링의 이해 - 데이터 모델링 (Section 1)

🔗 [원문 링크](https://velog.io/@tjeudeud/SQLD-1%EA%B3%BC%EB%AA%A9-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8%EB%A7%81%EC%9D%98-%EC%9D%B4%ED%95%B4-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%AA%A8%EB%8D%B8%EB%A7%81-Section-1)

🗓 작성일: 2025-05-15 19:58:25 KST

<blockquote>
<h2 id="point-1---데이터-모델링의-이해"><em>Point 1 - 데이터 모델링의 이해</em></h2>
</blockquote>
<h3 id="데이터-모델링">데이터 모델링</h3>
<ul>
<li>정보시스템을 구축하기 위한 데이터 관점의 업무 분석 기법</li>
<li>현실 세계의 데이터(what)를 약속된 표기법으로 표현하는 과정</li>
<li>데이터 베이스를 구축하기 위한 분석 및 설계의 과정</li>
</ul>
<h3 id="데이터-모델링-유의점">데이터 모델링 유의점</h3>
<ul>
<li><p><em>중복(Duplication)</em></p>
<ul>
<li>같은 데이터를 사용하는 사람, 시간 장소를 파악하는데 도움을 준다. 여러 장소의 데이터베이스에 같은 정보를 저장하지 않도록 중복성을 최소화한다.</li>
</ul>
</li>
<li><p><em>비유연성(Inflexibility)</em></p>
<ul>
<li>사소한 업무변화에 데이터 모델이 수시로 변경되면 안된다. <strong>데이터의 정의</strong>를 <strong>데이터의 사용 프로세스</strong>와 <strong>분리</strong>하여 유연성을 높인다.</li>
</ul>
</li>
<li><p><em>비일관성(Inconsistency)</em>
  데이터간의 상호 연관관계를 명확하게 정의하여 일관성 있게 데이터가 유지되도록 한다.</p>
</li>
</ul>
<h3 id="데이터-모델링의-특징">데이터 모델링의 특징</h3>
<ul>
<li>데이터 모델링은 <strong>추상화</strong> 해야 한다. → 추상화는 공통적인 특징을 찾고 간략하게 표현한다.</li>
<li>데이터 모델링은 <strong>단순화</strong> 해야 한다. → 복잡한 문제를 피하고 누구나 이해할 수 있게 표현한다.  </li>
<li>데이터 모델링은 <strong>명확</strong>해야 한다. → 의미적 해석이 모호하지 않고 명확하게 해석되어야 한다.</li>
</ul>
<table>
<thead>
<tr>
<th>특징</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td>추상화(Abstraction)</td>
<td align="left">현실 세계를 간략하게 표현한다.</td>
</tr>
<tr>
<td>단순화(Simple)</td>
<td align="left">누구나 쉽게 이해할 수 있도록 표현한다.</td>
</tr>
<tr>
<td>명확성(Clarity)</td>
<td align="left">명확하게 의미가 해석되어야 하고 한 가지 의미를 가져야한다.</td>
</tr>
</tbody></table>
<h3 id="데이터-모델링의-단계">데이터 모델링의 단계</h3>
<ul>
<li>데이터 모델링은 개념적 모델링, 논리적 모델링, 물리적 모델링 단계로 이루어 진다. </li>
</ul>
<h4 id="1-개념적-모델링-conceptual-data-modeling">(1) 개념적 모델링 (Conceptual Data Modeling)</h4>
<ul>
<li>기업의 비즈니스 프로세스를 분석하고 기업 전체에 대해서 데이터 모델링을 수행한다. </li>
<li>복잡하게 표현하지 않고 <u><strong>중요한 부분을 위주</strong></u>로 모델링 하는 단계이다.</li>
<li>업무 관점에서 모델링 하며 <strong>기술적인 용어</strong>는 <u>가급적 사용하지 않는다</u>.</li>
<li><strong>엔터티(Entity)</strong>와 <strong>속성(Attribute)</strong>을 도출하고 <strong>개념적 ERD(Entity Relationship Diagram)</strong> 를 작성한다.</li>
</ul>
<h4 id="2-논리적-모델링logical-data-modeling">(2) 논리적 모델링(Logical Data Modeling)</h4>
<ul>
<li>개념적 모델링을 논리적 모델링으로 변환하는 작업이다.</li>
<li>식별자를 도출하고 필요한 모든 릴레이션을 정의한다.</li>
<li>정규화를 수행해서 데이터 모델의 독립성을 확보한다.</li>
</ul>
<h4 id="3-물리적-모델링physical-modeling">(3) 물리적 모델링(Physical Modeling)</h4>
<ul>
<li><p>데이터 베이스를 실제 구축한다. 즉, 테이블, 인덱스, 함수 등을 생성한다.</p>
</li>
<li><p>성능, 보안, 가용성을 고려해서 구축한다.</p>
</li>
<li><h4 id="데이터-모델링-단계">데이터 모델링 단계</h4>
<table>
<thead>
<tr>
<th>데이터 모델링 단계</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td>개념적 모델링</td>
<td align="left">- <strong>전사적 관점</strong>에서 기업의 데이터를 모델링한다.<br /> - <strong>추상화 수준</strong>이 <strong>가장 높은 수준의 모델링</strong>이다. <br /> - 계층형 데이터 모델, 네트워크 모델, 관계형 모델에 관계없이 <strong>업무 측면에서 모델링을 한다</strong>.</td>
</tr>
<tr>
<td>논리적 모델링</td>
<td align="left">- 특정 데이터 베이스 모델에 종속한다. <br /> - 식별자를 정의하고 관계, 속성 등을 모두 표현한다. <br /> - 정규화를 통해서 <strong>재사용성을 높인다</strong>.</td>
</tr>
<tr>
<td>물리적 모델링</td>
<td align="left">- 구축할 데이터베이스 관리 시스템에 테이블, 인덱스 등을 생성하는 단계이다. <br /> - <strong>성능, 보안, 가용성 등을 고려하여 데이터 베이스를 구축</strong>한다.</td>
</tr>
</tbody></table>
</li>
<li><h4 id="데이터-모델링-관점">데이터 모델링 관점</h4>
<table>
<thead>
<tr>
<th>관점(View)</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td>데이터</td>
<td align="left">- 비즈니스 프로세스에서 사용되는 데이터를 의미한다. <br /> - 구조 분석, 정적 분석</td>
</tr>
<tr>
<td>프로세스</td>
<td align="left">- 비즈니스 프로세스에서 수행하는 작업을 의미한다. <br /> - 시나리오 분석, 도메인 분석, 동적 분석</td>
</tr>
<tr>
<td>데이터와 프로세스</td>
<td align="left">- 프로세스와 데이터 간의 관계를 의미한다. <br /> - CRUD(Create Read Update Delete) 분석</td>
</tr>
</tbody></table>
</li>
</ul>
<h3 id="데이터-모델링을-위한-erdentity-relationship-diagram">데이터 모델링을 위한 ERD(Entity Relationship Diagram)</h3>
<ul>
<li>1976년 <u><strong>피터첸(Peter Chen)</strong></u>이 Entity Relationship Model 표기법을 만들었으며, 사실상 데이터 모델링의 표준으
 로 사용되고있다.<ul>
<li>엔터티와 엔터티 간의 관계를 정의하는 모델링 방법이다.</li>
<li>가장 중요한 엔터티를 왼쪽 상단에 배치. </li>
</ul>
</li>
</ul>
<h4 id="1-erd-작성-절차">(1) ERD 작성 절차</h4>
<p>① 엔터티를 도출하고 그린다.</p>
<ul>
<li>업무에서 관리해야 하는 집합을 도출</li>
</ul>
<p>② 엔터티를 배치한다.</p>
<ul>
<li>엔터티를 도출한 후 엔터티를 배치. 중요한 엔터티를 왼쪽 상단에 배치</li>
</ul>
<p>③ 엔터티 간의 관계를 설정한다.</p>
<p>④ 관계명을 서술한다.</p>
<ul>
<li>엔터티 간에 어떤 행위나 존재가 있는지 표현한다.</li>
</ul>
<p>⑤ 관계 참여도를 표현한다.</p>
<ul>
<li>관계 참여도는 한 개의 엔티티와 다른 엔터티 간의 참여하는 관계 수를 의미한다.</li>
<li>즉, ' 고객이 여러 개의 계좌를 개설할 수 있다 ' 와 같은 의미를 표현한다.</li>
</ul>
<p>⑥ 관계의 필수 여부를 표현한다.</p>
<ul>
<li>필수는 반드시 존재해야하는 것이다.</li>
<li>예를 들어 ' 모든 고객은 반드시 하나의 계좌는 개설해야한다. '와 같은 의미를 표현한다.</li>
</ul>
<blockquote>
<p>보기에서, 
<strong>일반적으로 ERD를 작성할 때 엔터티 도출 -&gt; 엔터티 배치 -&gt; 관계 설정 -&gt; 관계명 기술의 흐름으로 작업을 진행한다.</strong> 라고 되어있다면, <strong>알맞는</strong> 보기.</p>
</blockquote>
<h4 id="2-erd-작성시-고려사항">(2) ERD 작성시 고려사항</h4>
<ul>
<li>중요한 엔터티를 가급적 왼쪽 상단에 배치한다.</li>
<li>ERD 는 이해가 쉬워야 하고 너무 복잡하지 않아야한다.</li>
</ul>
<h3 id="데이터-모델링-고려사항">데이터 모델링 고려사항</h3>
<h4 id="1-데이터-모델의-독립성">(1) 데이터 모델의 독립성</h4>
<ul>
<li>독립성이 확보된 모델은 고객의 업무 변화에 능동적으로 대응할 수 있다.</li>
<li>독립성 확보하기 위해서는 <u><strong>중복된 데이터를 제거해야한다</strong></u>.</li>
<li>데이터 중복을 제거하는 방법이 바로 <u><strong>정규화</strong></u> 이다. </li>
</ul>
<h4 id="2-고객-요구사항의-표현">(2) 고객 요구사항의 표현</h4>
<ul>
<li>고객의 요구사항을 너무 복잡하지 않게 표현해야한다. 왜? 데이터 모델링으로 고객과 데이터 모델러 간에 의사소통을 할 수 있어야해서.</li>
<li>요구사항을 간결하고 명확하게 표현</li>
</ul>
<h4 id="3-데이터-품질-확보">(3) 데이터 품질 확보</h4>
<ul>
<li>데이터베이스 구축 시에 데이터 표준을 정의하고 표준 준수율을 관리해야한다.</li>
<li>데이터 표준을 확보해야 데이터 품질을 향상시킬 수 있다.</li>
</ul>
<h3 id="좋은-데이터-모델의-요소">좋은 데이터 모델의 요소</h3>
<p>① 완전성 : 업무에 필요한 모든 데이터가 모델에 정의
② 중복배제 : 하나의 DB내에 동일한 사실은 한번만
③ 업무 규칙 : 많은 규칙을 사용자가 공유하도록 제공
④ 데이터 재사용 : 데이터가 독립적으로 설계돼야 함
⑤ 의사소통 : 업무 규칙은 엔터티, 서브타입, 속성, 관계 등의 형태로 최대한 자세히 표현
⑥ 통합성 : 동일한 데이터는 한번만 정의, 참조 활용</p>
<h3 id="데이터-모델링의-중요-개념">데이터 모델링의 중요 개념</h3>
<p>① 업무가 관여하는 어떤 것(Things)
② 업무가 관여하는 어떤 것의 성격(Attributes)
③ 업무가 관여하는 어떤 것의 관계(Relationships)</p>
<hr />
<blockquote>
<h2 id="point-2---3층-스키마3-level-schema"><em>Point 2 - 3층 스키마(3-Level Schema)</em></h2>
</blockquote>
<h3 id="1️⃣-3층-스키마">1️⃣ 3층 스키마</h3>
<ul>
<li><p>사용자, 설계자, 개발자가 데이터베이스를 보는 관점에 따라 데이터 베이스를 기술하고 이들 간의 관계를 정의한 ANSI 표준이다.</p>
</li>
<li><p>3층 스키마는 데이터베이스의 독립성을 확보하기 위한 방법</p>
</li>
<li><p>데이터의 독립성을 확보하면 데이터 복잡도 증가, 데이터 중복 제거, 사용자 요구사항 변경에 따른 대응력 향상, 관리 및 유지보수 비용 절감 등의 장점이 있다.</p>
</li>
<li><p>3단계 계층으로 분리해서 독립성을 확보하는 방법으로 각 계층을 View 라고도 한다.</p>
</li>
<li><h4 id="3층-스키마의-독립성">3층 스키마의 독립성</h4>
<table>
<thead>
<tr>
<th>독립성</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td>논리적 독립성</td>
<td align="left">저장구조가 변경되어도 응용 프로그램 및 개념 스키마에 영향이 없다.</td>
</tr>
<tr>
<td>물리적 독립성</td>
<td align="left">데이터베이스 논리적 구조가 변경되어도 응용프로그램에 변화가 없다.</td>
</tr>
</tbody></table>
</li>
</ul>
<h3 id="2️⃣-3층-스키마-구조">2️⃣ 3층 스키마 구조</h3>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/99e8a832-e2db-4fa5-a817-f2c49e2742a2/image.png" /></p>
<figcaption style="text-align: center; font-size: 15px; color: #808080; margin-top: 40px;">3층 스키마 구조</figcaption>

<ul>
<li><h4 id="3층-스키마의-구조">3층 스키마의 구조</h4>
<table>
<thead>
<tr>
<th>구조</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>외부 스키마(External Schema)</strong></td>
<td align="left">- 사용자 관점, 업무상 관련이 있는 데이터 접근이다. <br /> - 관련 데이터베이스의 뷰(View)를 표시한다. <br /> - <strong>응용 프로그램이 접근하는 데이터베이스</strong>를 정의한다.</td>
</tr>
<tr>
<td><strong>개념 스키마 (Conceptual Schema)</strong></td>
<td align="left">- 설계자 관점, 사용자 전체 집단의 데이터베이스 구조이다. <br /> - 전체 데이터 베이스 내의 규칙과 구조를 표현한다. <br /> - 통합 데이터 베이스 구조이다.</td>
</tr>
<tr>
<td><strong>내부 스키마 (Internal Schema)</strong></td>
<td align="left">- 개발자 관점, 데이터베이스의 물리적 저장구조이다. <br /> - 데이터 저장구조, 레코드 구조, 필드 정의, 인덱스 등을 의미한다.</td>
</tr>
</tbody></table>
</li>
</ul>
<hr />
<blockquote>
<h2 id="point-3---엔터티entity"><em>Point 3 - 엔터티(Entity)</em></h2>
</blockquote>
<h3 id="1️⃣-엔터티entity">1️⃣ 엔터티(Entity)</h3>
<ul>
<li>엔터티는 업무에서 관리해야 하는 데이터 집합을 의미하고 엔터티는 저장되고 관리되어야하는 데이터이다. </li>
<li>엔터티는 <u><strong>개념, 사전, 장소</strong></u> 등의 명사이다.</li>
<li><h4 id="엔터티의-의미">엔터티의 의미</h4>
<table>
<thead>
<tr>
<th>인물</th>
<th align="left">엔터티의 의미</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Peter Chen</strong></td>
<td align="left">- 엔터티를 변별할 수 있는 사물이다.</td>
</tr>
<tr>
<td><strong>James Martin</strong></td>
<td align="left">- 정보를 저장할 수 있는 어떤 것이다.</td>
</tr>
<tr>
<td><strong>C.J Date</strong></td>
<td align="left">- 데이터 베이스 내부에서 변별 가능한 객체이다.</td>
</tr>
<tr>
<td><strong>Thomas Bruce</strong></td>
<td align="left">- 정보가 저장될 수 있는 장소, 사람, 사건, 개념, 물건 등이다.</td>
</tr>
</tbody></table>
</li>
</ul>
<h3 id="2️⃣-엔터티entity-도출">2️⃣ 엔터티(Entity) 도출</h3>
<ul>
<li>엔터티는 고객의 비즈니스 프로세스에서 관리되어야 하는 정보를 추출해야한다.</li>
</ul>
<h3 id="3️⃣-엔터티entity-특징">3️⃣ 엔터티(Entity) 특징</h3>
<ul>
<li>엔터티는 다음과 같은 특징을 가지고 있다.</li>
<li><h4 id="엔터티의-특징">엔터티의 특징</h4>
<table>
<thead>
<tr>
<th>엔터티 특징</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>식별자</strong></td>
<td align="left">- 엔터티는 유일한 식별자가 있어야한다. <br /> - 예) 회원 ID, 계좌번호</td>
</tr>
<tr>
<td><strong>인스턴스 집합</strong></td>
<td align="left">- 2개 이상의 인스턴스가 있어야 한다. <br /> - 즉, 고객 정보는 2명 이상 있어야 한다.</td>
</tr>
<tr>
<td><strong>속성</strong></td>
<td align="left">- 엔터티는 반드시 속성을 가지고 있다. <br /> - 예) 고객 엔터티에 회원 ID, 패스워드, 이름, 주소, 전화번호</td>
</tr>
<tr>
<td><strong>관계</strong></td>
<td align="left">- 엔터티는 다른 엔터티와 최소 한 개 이상 관계가 있어야 한다. <br /> - 예) 고객은 계좌를 개설한다.</td>
</tr>
<tr>
<td><strong>업무</strong></td>
<td align="left">- 엔터티는 업무에서 관리되어야 하는 집합이다. <br /> - 예) 고객, 계좌</td>
</tr>
</tbody></table>
</li>
</ul>
<h3 id="4️⃣-엔터티entity-종류">4️⃣ 엔터티(Entity) 종류</h3>
<ul>
<li>엔터티의 종류는 유형과 무형에 따른 종류, 엔터티가 발생하는 시점에 따른 종류로 나누어 진다.</li>
</ul>
<h4 id="1-유형과-무형-엔터티">(1) 유형과 무형 엔터티</h4>
<ul>
<li>엔터티를 유형과 무형으로 분류하는 기준은 물리적 형태의 존재 여부이다.</li>
<li><h4 id="유형과-무형에-따른-엔터티-종류">유형과 무형에 따른 엔터티 종류</h4>
<table>
<thead>
<tr>
<th>종류</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>유형 엔터티</strong></td>
<td align="left">- 업무에서 도출되며 지속적으로 사용되는 엔터티이다. <br /> 예) 고객, 강사, 사원 등</td>
</tr>
<tr>
<td><strong>개념 엔터티</strong></td>
<td align="left">- 유형 엔터티는 물리적 형태가 있지만, 개념 엔터티는 물리적 형태가 없다. <br /> - 개념적으로 사용되는 엔터티이다. <br /> - 예) 거래소 종목, 코스닥 종목, 생명보험 상품</td>
</tr>
<tr>
<td><strong>사건 엔터티</strong></td>
<td align="left">- 비즈니스 프로세스를 실행하면서 생성되는 엔터티이다. <br /> - 예) 주문, 체결, 취소주문, 수수료 청구 등</td>
</tr>
</tbody></table>
</li>
</ul>
<h4 id="2-발생-시점에-따른-엔터티의-종류">(2) 발생 시점에 따른 엔터티의 종류</h4>
<ul>
<li><h4 id="발생-시점에-따른-엔터티-종류-기-중-행">발생 시점에 따른 엔터티 종류 (<strong>기 중 행)</strong></h4>
<table>
<thead>
<tr>
<th>종류</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>기본 엔터티(Basic Entity)</strong></td>
<td align="left">- 키 엔터티 라고도 한다. <br /> - 다른 엔터티로부터 영향을 받지 않고 독립적으로 생성되는 엔터티이다. <br />- 예) 고객, 상품, 부서 등</td>
</tr>
<tr>
<td><strong>중심 엔터티(Main Entity)</strong></td>
<td align="left">- 유기본 엔터티와 행위 엔터티 간의 중간에 있는 것이다. <br /> - 즉, 기본 엔터티로부터 발생되고 행위 엔터티를 생성하는 것이다. <br /> - 예) 계좌, 주문, 취소, 체결 등</td>
</tr>
<tr>
<td><strong>행위 엔터티(Active Entity)</strong></td>
<td align="left">- 2개 이상의 엔터티로부터 발생된다. <br /> - 예) 주문 이력, 체결 이력 등</td>
</tr>
</tbody></table>
</li>
</ul>
<h3 id="엔터티에-이름-부여하는-방법">엔터티에 이름 부여하는 방법</h3>
<ol>
<li>가능한 현업 업무에서 사용하는 용어를 사용한다.</li>
<li>가능하면 약어를 사용하지 않는다.</li>
<li>단수명사를 사용한다.</li>
<li>모든 엔터티를 통틀어서 유일하게 이름이 부여되어야 한다.</li>
<li>엔터티 생성 의미대로 이름을 부여한다.</li>
</ol>