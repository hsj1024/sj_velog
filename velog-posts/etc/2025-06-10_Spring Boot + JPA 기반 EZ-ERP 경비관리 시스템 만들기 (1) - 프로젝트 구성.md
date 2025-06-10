# Spring Boot + JPA 기반 EZ-ERP 경비관리 시스템 만들기 (1) - 프로젝트 구성

🔗 [원문 링크](https://velog.io/@tjeudeud/Spring-Boot-JPA-%EA%B8%B0%EB%B0%98-EZ-ERP-%EA%B2%BD%EB%B9%84%EA%B4%80%EB%A6%AC-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%84%B1)

🗓 작성일: 2025-06-10 15:37:11 KST

<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/aaec77f9-8660-458d-96ce-38e4055f18e1/image.png" /></p>
<h3 id="✨-1-프로젝트-개요">✨ 1. 프로젝트 개요</h3>
<blockquote>
<p>EZ-ERP는 Easy + ERP의 합성어로, 중소 규모 조직의 지출·경비 처리를 단순화한 백엔드 중심 학습형 ERP 시스템입니다.
이 프로젝트는 Spring Boot, JPA, Swagger(OpenAPI), H2 DB를 기반으로 RESTful API를 설계하고 구현한 개인 프로젝트입니다.</p>
</blockquote>
<hr />
<h2 id="spring-initializr에서-프로젝트-생성">Spring Initializr에서 프로젝트 생성</h2>
<h3 id="📍-사이트-주소-httpsstartspringio">📍 사이트 주소: <a href="https://start.spring.io">https://start.spring.io</a></h3>
<p>Spring Boot 프로젝트를 생성하기 위해 Spring Initializr 웹사이트를 이용합니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/226efad6-7622-417c-b15e-37ad090e0a31/image.png" /></p>
<h3 id="①-설정-예시">① 설정 예시</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>값 예시</th>
</tr>
</thead>
<tbody><tr>
<td>Project</td>
<td>Gradle - Groovy 또는 Maven</td>
</tr>
<tr>
<td>Language</td>
<td>Java</td>
</tr>
<tr>
<td>Spring Boot</td>
<td>3.5.0 (또는 최신 안정 버전)</td>
</tr>
<tr>
<td>Group</td>
<td><code>com.ez.erp</code></td>
</tr>
<tr>
<td>Artifact</td>
<td><code>ez-erp</code></td>
</tr>
<tr>
<td>Name</td>
<td><code>ez-erp</code></td>
</tr>
<tr>
<td>Description</td>
<td>EZ ERP Expense System</td>
</tr>
<tr>
<td>Package Name</td>
<td><code>com.ez.erp</code></td>
</tr>
<tr>
<td>Packaging</td>
<td>Jar</td>
</tr>
<tr>
<td>Java Version</td>
<td>21</td>
</tr>
</tbody></table>
<h3 id="②-dependencies-의존성-추가">② Dependencies (의존성 추가)</h3>
<ul>
<li><strong>Spring Web</strong> (REST API 구현)</li>
<li><strong>Spring Data JPA</strong> (데이터베이스 연동)</li>
<li><strong>H2 Database</strong> (간편 테스트용 인메모리 DB)</li>
<li><strong>Lombok</strong> (코드 간소화)</li>
<li><strong>Validation</strong> (입력 유효성 검증)</li>
<li><strong>Spring Boot DevTools</strong> (개발 편의)</li>
</ul>
<p><code>Generate</code> 버튼을 클릭하면 <code>.zip</code> 파일이 다운로드됩니다. 이를 압축 해제하고 IDE(IntelliJ 등)로 열면 프로젝트 준비 완료입니다.</p>
<hr />
<h2 id="github-업로드-가이드">GitHub 업로드 가이드</h2>
<h3 id="📁-github에-올릴-디렉토리-구조">📁 GitHub에 올릴 디렉토리 구조</h3>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/801c6abb-b3f8-4ba2-b727-b54d4339ba34/image.png" /></p>
<pre><code>ez-erp/
├── build.gradle
├── settings.gradle
├── gradlew
├── gradlew.bat
├── .gitignore
├── README.md
├── src/</code></pre><h3 id="📄-gitignore-gradle--intellij-기준">📄 .gitignore (Gradle + IntelliJ 기준)</h3>
<pre><code class="language-gitignore">HELP.md
.gradle
build/
!gradle/wrapper/gradle-wrapper.jar
!**/src/main/**/build/
!**/src/test/**/build/

### STS ###
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache
bin/
!**/src/main/**/bin/
!**/src/test/**/bin/

### IntelliJ IDEA ###
.idea
*.iws
*.iml
*.ipr
out/
!**/src/main/**/out/
!**/src/test/**/out/

### NetBeans ###
/nbproject/private/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/

### VS Code ###
.vscode/

# OS
.DS_Store
Thumbs.db

# Logs
*.log</code></pre>
<h3 id="📄-readmemd-예시">📄 README.md 예시</h3>
<pre><code class="language-markdown"># EZ-ERP

EZ-ERP는 기업의 경비와 지출 관리를 단순화하여 구현한 학습용 ERP 백엔드 프로젝트입니다.

## 사용 기술
- Java 21, Spring Boot 3.5.0
- Spring Data JPA, H2 DB
- Swagger (Springdoc OpenAPI)
- Lombok, Validation

## 주요 기능
- 사원 등록 / 조회
- 지출 등록 / 승인 / 반려
- 월별 지출 통계 API

## 실행 방법

./gradlew bootRun


Swagger 문서: [http://localhost:8080/swagger-ui/index.html](http://localhost:8080/swagger-ui/index.html)</code></pre>
<hr />
<h2 id="초기-도메인-설계-및-api-구성">초기 도메인 설계 및 API 구성</h2>
<h3 id="📌-기본-기능-사원employee-관리">📌 기본 기능: 사원(Employee) 관리</h3>
<p><strong>도메인 설명:</strong> 사원의 이름, 부서, 직책, 이메일 정보를 저장하며 등록 및 전체 조회 API를 제공합니다.</p>
<h3 id="📁-패키지-구조">📁 패키지 구조</h3>
<pre><code>com.ez.erp
├── controller
│   └── EmployeeController.java
├── domain
│   └── Employee.java
├── repository
│   └── EmployeeRepository.java
└── service
    └── EmployeeService.java</code></pre><h3 id="📄-employeejava">📄 Employee.java</h3>
<pre><code class="language-java">package com.ez.erp.domain;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Employee {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String department;
    private String position;
    private String email;
}</code></pre>
<h3 id="📄-employeerepositoryjava">📄 EmployeeRepository.java</h3>
<pre><code class="language-java">package com.ez.erp.repository;

import com.ez.erp.domain.Employee;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeRepository extends JpaRepository&lt;Employee, Long&gt; {
}</code></pre>
<h3 id="📄-employeeservicejava">📄 EmployeeService.java</h3>
<pre><code class="language-java">package com.ez.erp.service;

import com.ez.erp.domain.Employee;
import com.ez.erp.repository.EmployeeRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class EmployeeService {
    private final EmployeeRepository repository;
    public Employee save(Employee employee) {
        return repository.save(employee);
    }
    public List&lt;Employee&gt; findAll() {
        return repository.findAll();
    }
}</code></pre>
<h3 id="📄-employeecontrollerjava">📄 EmployeeController.java</h3>
<pre><code class="language-java">package com.ez.erp.controller;

import com.ez.erp.domain.Employee;
import com.ez.erp.service.EmployeeService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(&quot;/api/employees&quot;)
@RequiredArgsConstructor
public class EmployeeController {
    private final EmployeeService employeeService;

    @PostMapping
    public Employee save(@RequestBody Employee employee) {
        return employeeService.save(employee);
    }

    @GetMapping
    public List&lt;Employee&gt; findAll() {
        return employeeService.findAll();
    }
}</code></pre>
<hr />
<h2 id="✅-다음-계획">✅ 다음 계획</h2>
<ul>
<li>지출(Expense) 도메인 설계 및 승인 프로세스 구현</li>
<li>월별 지출 통계 API 개발</li>
<li>Springdoc Swagger 연동으로 자동 문서화 구성</li>
<li>Dockerfile 및 CI/CD 구성</li>
</ul>
<blockquote>
<p>다음 글에서는 지출(Expense) 도메인을 설계하고, 
지출 등록과 승인 처리를 위한 API를 구현해보겠습니다.</p>
</blockquote>