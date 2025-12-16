# LangChain Study - Day 1

🔗 [원문 링크](https://velog.io/@tjeudeud/LangChain-Study)

🗓 작성일: 2025-12-16 11:11:25 KST

<h3 id="day-1-독학-시작">Day 1 독학 시작!</h3>
<p><strong>LangChain 설치하기</strong></p>
<pre><code>pip install langchain langchain-community transformers torch
</code></pre><p><strong>Code</strong></p>
<pre><code>from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

hf_pipe = pipeline(
    &quot;text-generation&quot;,
    model=&quot;google/flan-t5-base&quot;,
    max_new_tokens=128
)

llm = HuggingFacePipeline(pipeline=hf_pipe)

print(llm(&quot;Explain LangChain in one sentence.&quot;))</code></pre><p>이렇게 하면
API 키 0개로 LangChain 구조 그대로 학습 가능하다.</p>
<p><em>회사망에 막혔다.. 다른 방법으로 우회</em></p>
<h4 id="fake-llm-사용해보자">Fake LLM 사용해보자.</h4>
<pre><code>from langchain_community.llms.fake import FakeListLLM

llm = FakeListLLM(
    responses=[&quot;Hello LangChain&quot;]
)

print(llm.invoke(&quot;test&quot;))</code></pre><p>이후 실행해보면,</p>
<pre><code>python Fake_LLM.py</code></pre><p>&quot;Hello LangChain&quot; 이라는 문구가 나오면 성공이다.
즉 LangChain 설치 OK 실행 환경 OK &quot;LLM 객체”가 동작함을 확인</p>
<hr />
<h4 id="prompttemplate로-langchain답게-써보기">PromptTemplate로 LangChain답게 써보기</h4>
<p>Fake LLM으로 LangChain이 정상 동작하는 것을 확인했으니,
이제 LangChain의 핵심 개념 중 하나인 PromptTemplate을 사용해본다.</p>
<p>PromptTemplate은 단순 문자열 프롬프트가 아니라,
입력 변수를 명시적으로 관리하고 재사용할 수 있는 프롬프트 객체다.</p>
<pre><code>from langchain_core.prompts import PromptTemplate
from langchain_community.llms.fake import FakeListLLM

prompt = PromptTemplate.from_template(
    &quot;Answer in one sentence: {question}&quot;
)

llm = FakeListLLM(
    responses=[&quot;LangChain connects LLMs with tools.&quot;]
)

chain = prompt | llm
print(chain.invoke({&quot;question&quot;: &quot;What is LangChain?&quot;}))
</code></pre><blockquote>
<p><strong>prompt | llm</strong> 은 프롬프트의 출력이 LLM의 입력으로 전달되는 파이프라인을 의미한다.</p>
</blockquote>
<p>실행 결과:</p>
<pre><code>LangChain connects LLMs with tools.</code></pre><h4 id="이-단계의-의미">이 단계의 의미</h4>
<ul>
<li>PromptTemplate 사용 ✔️  </li>
<li>Prompt와 LLM을 체인(chain)으로 연결 ✔️  </li>
<li>LangChain의 Runnable 파이프라인 구조를 직접 사용 ✔️  </li>
</ul>
<p><strong>즉 정리하면,</strong> </p>
<ul>
<li>Hello LangChain 출력 → 환경 및 LLM 객체 동작 확인</li>
<li>PromptTemplate + Chain → LangChain을 LangChain 답게 사용할 수 있다.</li>
</ul>