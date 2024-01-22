#### MSA (Micro Service Architecture)
- 작은 기능별로 서비스를 잘게 쪼개어 개발하는 형태
- Agile 방법론 적용
- CI 적용으로 MSA 환경에서 기능 충돌 방지 

## CI (Continuous Integration): 지속적인 통합
고객의 요구사항에 빠르게 대응하기 위해 나온 XP의 실천방안 중 한가지
새로운 코드 변경 사항이 **정기적으로** 빌드 및 테스트 되어 공유 레포지토리에 통합
여러 명이 하나의 코드에 대해 수정을 진행해도 지속적으로 통합하면서 관리
![Alt text](cicd/image.png)

## CD
빌드의 결과물을 Production으로 지속적으로 배포 
![Alt text](cicd/image-1.png)

#### 지속적 제공 (Continuous Delivery)
Production으로 release하는 Deploy 작업이 수동
#### 지속적 배포 (Continuous Deployment)
Production으로 release하는 Deploy 작업까지 모두 자동화


### CI/CD Tools
Jenkins  
Travis CI  
Bamboo  

## 무중단 배포 
![Alt text](cicd/image-3.png)
