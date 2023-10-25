[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/fnZ3vxy8)
### 1. 프로젝트 소개

프로젝트 명 : 드론을 이용한 교내 Wi-Fi 음영 확인 및 해결 제안 시스템

프로젝트 개요 : 부산대학교 부지내에서 사용하는 PNU Wi-Fi의 음영지역을 쉽게 파악하여 해결할 수 있는 기술을 개발한다

프로젝트 목표
* Wi-Fi 신호 강도 탐지
  - Wi-Fi 모듈을 장착한 임베디드 보드와 드론을 이용하여 해당 지역의 신호 강도를 측정한다

* 신호 강도의 가시화를 통한 음영지역 확인
  - 신호 강도에 따라 다른 색으로 표현하여 신호 강도 데이터에 따른 신호 세기 분포도, Wi-Fi heatmap을 생성한다
  - 완성한 신호 세기 분포도, 즉 Wi-Fi heatmap을 출력하여 사용자가 음영 지역이 현재 어떤 곳에 나타나는지 확인할 수 있게 한다

* heatmap 분석을 통한 AP 배치 지점 특정
  - 세기 분포도를 AP 배치 위치 특정 알고리즘을 통해 분석하여 AP를 배치 할 지점을 특정한다

* 음영 지역 해결을 확인
  - 음영 지역 해결을 위한 AP 배치 위치를 알고리즘의 결과를 통해 확인하고 이를 AP를 실제로 설치하여 음영지역이 해결되었는지 확인한다

### 2. 팀소개

박동한, qkrehdgks11@naver.com, 신호 탐지 기술 개발, 서버와 보드간 통신 개발, 데이터 시각화 개발, 확장기 설치 지점 선택 알고리즘 개발

김동혜, swhyny@naver.com, 서버 환경 구축 및 개발, 드론 운용, 데이터 시각화 개발 및 웹페이지 출력, 확장기 설치 지점 선택 및 알고리즘 개발

### 3. 시스템 구성도

시스템 구성도는 전체 시스템 구성도와 임베디드 보드의 구성도로 나뉩니다

![시스템 구성도](https://github.com/pnucse-capstone/capstone-2023-1-33/assets/80632806/d328a263-32cd-4a14-a8d1-172b23b93f39)

![보드 구성도](https://github.com/pnucse-capstone/capstone-2023-1-33/assets/80632806/d4509617-0d7a-457f-95e1-1f776b23fe1e)

### 4. 소개 및 시연 영상

[![부산대학교 정보컴퓨터공학부 소개](http://img.youtube.com/vi/zh_gQ_lmLqE/0.jpg)](https://youtu.be/zh_gQ_lmLqE)

### 5. 설치 및 사용법

본 프로젝트는 Ubuntu 20.04 버전에서 개발되었으며 함께 포함된 다음의 스크립트를 수행하여 
관련 패키지들의 설치와 빌드를 수행할 수 있습니다.
```
$ ./install_and_build.sh
```
