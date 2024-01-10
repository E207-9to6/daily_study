# Domain Name
## 정의  
넓은 의미로는 네트워크상에서 컴퓨터를 식별하는 호스트 명  

좁은 의미로는 도메인 레지스트리에서 등록된 이름
- 도메인 레지스트리: 최상위 도메인에 등록된 모든 도메인 네임의 데이터베이스

## URL
도메인을 포함한 경로  
![image](https://github.com/E207-9to6/daily_study/assets/68316096/57384f91-32a6-40d2-b40a-3ce66f31c7d6)  
[데이터 분석을 위한 기초, URL 이해하기](https://www.beusable.net/blog/?p=4507)

## DNS(Domain Name System)
도메인 네임으로 IP를 찾는 시스템

### nslookup
- DNS 서버에 도메인이나 ip주소를 질의해서 DNS 서버에 있는 정보를 응답받을 때 사용하는 명령어  

- `nslookup naver.com`  
![image](https://github.com/E207-9to6/daily_study/assets/68316096/160de046-218c-4377-aace-f86e41ae2805)

## 주소창에 naver.com을 입력하면?  
![image](https://github.com/E207-9to6/daily_study/assets/68316096/93da3b34-59ab-443b-9778-373928ba58df)  

1. 브라우저에 naver.com 입력

2. URL 주소 중 도메인 네임 부분(naver.com)을 DNS 서버에서 검색  
   - 있다면 해당 도메인 네임에 해당하는 IP 주소를 찾아 사용자가 입력한 URL 정보와 함께 전달
  
3. 없다면 Root DNS 서버에 도메인 네임 확인을 요청함

4. Root DNS 서버(ISP의 DNS 서버)는www.naver.com에 대한 주소 정보를 모른다. 대신 .com으로 끝나는 도메인에 대한 DNS 정보가 담긴 서버의 IP주소를 반환

5. 반환받은 주소를 통해 .com DNS서버로 다시www.naver.com에 대한 IP주소정보를 요청

6. .com DNS서버는 www.naver.com의 IP주소 정보를 모른다. 대신 naver.com으로 끝나는 도메인에 대한 DNS 정보가 담긴 서버의 IP주소를 반환

7. 반환받은 주소를 통해 naver.com DNS서버로 다시www.naver.com에 대한 IP주소정보를 요청

8. 최종적으로 www.naver.com 웹서버의 IP주소를 획득. 다시 방문하면 IP 주소를 빠르게 찾기 위해 naver.com이라는 서버의 IP를 로컬 DNS 서버에 캐싱
