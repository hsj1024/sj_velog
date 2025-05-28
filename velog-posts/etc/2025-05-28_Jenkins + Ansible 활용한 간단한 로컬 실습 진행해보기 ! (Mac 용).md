# Jenkins + Ansible 활용한 간단한 로컬 실습 진행해보기 ! (Mac 용)

🔗 [원문 링크](https://velog.io/@tjeudeud/Jenkins-Ansible-%EB%A1%9C%EC%BB%AC-%EC%8B%A4%EC%8A%B5-%EC%A7%84%ED%96%89%ED%95%B4%EB%B3%B4%EA%B8%B0-Mac-%EC%9A%A9)

🗓 작성일: 2025-05-28 19:45:23 KST

<p>이 실습은 macOS에서 Homebrew를 활용해 Jenkins와 Ansible을 설치하고, Jenkins에서 Ansible 플레이북을 실행하는 과정을 다룬다 !</p>
<hr />
<h2 id="✅-1단계-jenkins-설치">✅ 1단계: Jenkins 설치</h2>
<h3 id="1-1-homebrew-설치-여부-확인">1-1. Homebrew 설치 여부 확인</h3>
<p>터미널에서 다음 명령어 입력:</p>
<pre><code class="language-bash">brew --version</code></pre>
<p>설치되어 있지 않다면 Homebrew 설치:</p>
<pre><code class="language-bash">/bin/bash -c &quot;$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)&quot;</code></pre>
<h3 id="1-2-jenkins-설치">1-2. Jenkins 설치</h3>
<pre><code class="language-bash">brew install jenkins-lts</code></pre>
<p>설치 후 Jenkins 실행:</p>
<pre><code class="language-bash">brew services start jenkins-lts</code></pre>
<p>Jenkins 실행 확인:</p>
<ul>
<li>브라우저에서 <a href="http://localhost:8080">http://localhost:8080</a> 접속
<img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/d3001160-bf83-4ba9-aa4c-10c99b6d6c9c/image.png" /></li>
</ul>
<h3 id="1-3-관리자-초기-비밀번호-확인">1-3. 관리자 초기 비밀번호 확인</h3>
<pre><code class="language-bash">cat /Users/$(whoami)/.jenkins/secrets/initialAdminPassword</code></pre>
<p>이 비밀번호로 Jenkins 초기 설정 진행, 아래 사진 처럼 비밀번호가 뜬다.
<img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/362e388e-4c0f-4cf8-84af-26482c42f69d/image.png" /></p>
<h3 id="1-4-install-suggested-plugins">1-4 Install suggested plugins</h3>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/1cef77a1-790d-42c4-a0ef-5fe66ff6c7c7/image.png" />
왼쪽 선택지를 선택하여 plugin 들을 설치해준다.</p>
<p>그렇게 되면 설치가 바로 시작된다. 시간이 조금 소요된다.
<img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/f49ba61a-53ad-4df2-8f8c-88d4d103fb62/image.png" /></p>
<p>이후 하라는대로 한 뒤에 화면을 확인해보면 </p>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/4138a23f-9ebc-4254-831e-ae0210ebfb14/image.png" /></p>
<p>이렇게 실행된 것을 확인할 수 있다.</p>
<hr />
<h2 id="✅-2단계-ansible-설치">✅ 2단계: Ansible 설치</h2>
<pre><code class="language-bash">brew install ansible</code></pre>
<p>설치 확인:</p>
<pre><code class="language-bash">ansible --version</code></pre>
<hr />
<h2 id="✅-3단계-간단한-ansible-플레이북-작성">✅ 3단계: 간단한 Ansible 플레이북 작성</h2>
<h3 id="3-1-플레이북-작성">3-1. 플레이북 작성</h3>
<p>파일을 만들 디렉토리에 <code>playbook.yml</code> 파일 생성:</p>
<p>필자는 <code>ansible-jenkins-test</code> 라는 이름으로 폴더 생성 후 안에 생성했다.</p>
<pre><code class="language-yaml">- hosts: localhost
  connection: local
  tasks:
    - name: 테스트 파일 생성
      file:
        path: ~/jenkins_test_file.txt # txt 파일을 생성할 위치 지정해주기
        state: touch</code></pre>
<h3 id="3-2-플레이북-실행">3-2. 플레이북 실행</h3>
<pre><code class="language-bash">ansible-playbook ~/playbook.yml</code></pre>
<p>정상 실행되면 <code>jenkins_test_file.txt</code> 파일이 생성된다.
미리 <code>echo &quot;jenkins_test_file.txt&quot; &gt; .gitignore</code> 명령어를 통해 git ignore 생성해준다.</p>
<hr />
<h2 id="✅-4단계-jenkins에서-ansible-실행-연동">✅ 4단계: Jenkins에서 Ansible 실행 연동</h2>
<h3 id="4-1-jenkins에서-ansible-플러그인-설치">4-1. Jenkins에서 Ansible 플러그인 설치</h3>
<ul>
<li>Jenkins 대시보드 → <code>Manage Jenkins</code> → <code>Manage Plugins</code> → <code>Available</code></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/13daf4aa-6526-41a1-afb8-357699dac7fa/image.png" />
<img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/3e681af8-f118-4f06-8d3e-ca46f7f5e567/image.png" /></p>
<ul>
<li>'Ansible' 검색 후 설치 및 Jenkins 재시작
<img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/f410d52d-f467-45af-9ab7-eee9f2e7c14f/image.png" /></li>
</ul>
<h3 id="4-2-jenkins-job-설정">4-2. Jenkins Job 설정</h3>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/98b2803c-e4d5-4bee-aab4-7ca30a12e828/image.png" /></p>
<ol>
<li>Jenkins 대시보드 → <code>새로운 Item</code> 클릭 → Freestyle 프로젝트 생성</li>
<li><code>Build</code> 섹션에서 <code>Execute shell</code> 추가</li>
<li>다음 명령어 입력:</li>
</ol>
<pre><code class="language-bash">/opt/homebrew/bin/ansible-playbook /Users/seojeong/Documents/GitHub/ansible-jenkins-test/playbook.yml</code></pre>
<ol start="4">
<li>빌드 실행 → 성공 시 <code>jenkins_test_file.txt</code> 생성됨</li>
</ol>
<hr />
<h2 id="🎯-마무리">🎯 마무리</h2>
<ul>
<li>Jenkins를 통해 Ansible을 실행하는 흐름을 익힐 수 있는 기본 실습이다.</li>
<li>Jenkins 파이프라인 스크립트나 다른 서버 대상 실행 등으로 확장할 수 있다.</li>
</ul>