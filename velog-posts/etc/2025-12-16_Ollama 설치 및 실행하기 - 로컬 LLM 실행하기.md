# Ollama 설치 및 실행하기 - 로컬 LLM 실행하기

🔗 [원문 링크](https://velog.io/@tjeudeud/Ollama)

🗓 작성일: 2025-12-16 16:43:37 KST

<p>Ollama 설치하기</p>
<p>내 환경 : Windows</p>
<ol>
<li><p>공식 사이트에서 다운로드
<a href="https://www.googleadservices.com/pagead/aclk?nis=4&amp;sa=L&amp;ai=C7V3lWQJBafXENcKRpt8P4-jPmQvsmMmPhAHAvvT45xSqwcTy4A8QASCF6ocuYJuj6YS4KaABiZHcwALIAQGpAsUWnL8sTwc-qAMByAPLBKoEjQJP0A8mBbxpusQQHUDU3bV6XMpvBjjoQUpqi-USPhzVUuQvIwPqAXDR9clRduUl4dl5tc9GdBsy_5l4xbl9-Fi6A0Q2rVS5icJprWl9KW-liPd8nqCOU5_p0zNWdS7MPbu0AFVRdurc16rfN6d9Hy5n6TqaI0NUPzTOUibN_xTS6KWUVeQT9W-mWYzKsz9KYEN__DHchWgbGULG9amLWSwSqvIPnL_Nbo5fFBGyp8HKybWdFgev-alrOG-gWNqyGP_WDzm98vu4l7JfsVQuj3xNWB_6MTO-TZk56xqn59X9OLv_BJOb6rfxttm6b_jMRIyYo7L5nofKFCk2-4xig4bLy4ofkVv8hK8U21MwosAEr9LrkMMFiAX74LqJUJAGAaAGLoAH3-6jvwGIBwGQBwKoB6fMsQKoB-LYsQKoB6a-G6gHzM6xAqgH89EbqAeW2BuoB6qbsQKoB47OG6gHk9gbqAfw4BuoB-6WsQKoB_6esQKoB6--sQKoB9XJG6gH2baxAqgHmgaoB_-esQKoB9-fsQKoB8qpsQKoB-ulsQKoB-qxsQKoB5m1sQKoB763sQKoB_jCsQKoB_vCsQLYBwHSCDMIABACGJoDMgiAgICAgICACDoSn9CAgICABJDAgICAoKiAAqgBSL39wTpYlKz_sMPBkQOxCUzaS0PU-AR3gAoBmAsByAsBogwLKgYKBNbasQKQAQHaDBAKChDg-f64qfOf4z4SAgEDqg0CS1LIDQHqDRMIxuiLscPBkQMVwojpBR1j9DOz8A0CiA4J2BMNiBQC0BUBmBYByhYCCgD4FgGAFwGyFwIYAboXAjgBshgJEgLoWBguIgEA0BgBwhkCCAE&amp;ae=1&amp;ase=2&amp;gclid=Cj0KCQiAgP_JBhD-ARIsANpEMxzwhAIyFJwD6eRiCE3WOLLAH2oeGW8fhochaflmEdxcToWsdgjFL2UaAiTPEALw_wcB&amp;num=1&amp;cid=CAQSpgEAwksa0cnHJTzRqtqoZJi5EAjaT4JbxIAlEjlM_DbiG3dQ1O1OS4ra_B3UqSH-UmhOv98QN381DGIOL1ydwbYpzJIkn1_QOF37IkRbVwPPNiZL4xAw5OtpHE8ZV4nAmhoEsHG2EwTCiHM5byHYRv-EoqfwXGWBb9K5AxKb1VbTOmhA5EaB2TEf4hUM0KFiN9x-ZCuGB25OBrRrpNEXBheInMYcgLpRGAE&amp;sig=AOD64_3EA11eHpHEHRIc6RaEwXnG4DkROw&amp;client=ca-pub-6164889535561655&amp;rf=1&amp;nb=9&amp;adurl=https://www.adobe.com/kr/creativecloud/buy/students.html%3Fsdid%3DKVGRTR8G%26mv%3Ddisplay%26mv2%3Ddisplay%26gad_source%3D5%26gad_campaignid%3D21494673531%26gclid%3DCj0KCQiAgP_JBhD-ARIsANpEMxzwhAIyFJwD6eRiCE3WOLLAH2oeGW8fhochaflmEdxcToWsdgjFL2UaAiTPEALw_wcB">공식 사이트에서 Ollama 다운로드 하기
</a></p>
</li>
<li><p>OllamaSetup.exe 실행 후 설치
<img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/a593340b-b0ac-4ae3-8254-7020379539c6/image.png" /></p>
</li>
<li><p>재부팅 필요하면 재부팅</p>
</li>
<li><p>모델 다운로드 하기
<a href="https://ollama.com/search">모델 찾기 페이지</a></p>
</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/1e6ff509-c3ef-4c2c-af54-81955672f49e/image.png" />
    나는 Gemma3 모델을 선정했다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/6b917875-bdbe-46a3-9869-44b7c67c2b28/image.png" />
위와 같이 모델 다운로드를 한다.</p>
<p>다운로드가 끝나면 </p>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/a6a1b49e-0994-4bf8-af47-a93312f42fa6/image.png" /></p>
<p>이런식으로 GUI 환경에서도 대화를 할 수 있고, CLI 환경에서도 대화가 가능하다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/tjeudeud/post/b0659d95-80da-4d84-b716-b28ddf974df1/image.png" /></p>
<p>설치 및 실행 성공하였당</p>