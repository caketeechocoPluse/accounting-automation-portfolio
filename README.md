# accounting-automation-portfolio
# 회계 업무 자동화 포트폴리오
> Python을 활용한 재무/회계 데이터 처리 및 보고서 자동화

## 👨‍💼 소개
회계 실무 경험을 바탕으로 반복적인 업무를 자동화하는 솔루션을 개발했습니다.

**핵심 역량**
- 📊 pandas를 활용한 재무 데이터 분석
- 📑 openpyxl을 통한 엑셀 보고서 자동 생성
- 🗄️ SQL 기반 회계 데이터베이스 설계 및 쿼리 최적화

## 🚀 주요 프로젝트

### 1. 월말 결산 보고서 자동화
**문제**: 매월 말 수작업으로 5시간 소요되는 재무제표 작성  
**해결**: Python 스크립트로 자동화하여 **10분으로 단축** (95% 시간 절감)

**기술 스택**: `pandas` `openpyxl` `pymysql`

[📂 프로젝트 보기](./04-integrated-project/)

**주요 기능**
- DB에서 당월 거래 데이터 자동 추출
- 계정과목별 자동 집계 및 검증
- 재무상태표/손익계산서 엑셀 자동 생성
- 전년 동월 대비 증감률 자동 계산

**실행 결과**
![결과 이미지](./images/result_sample.png)

---

### 2. 재무비율 분석 대시보드
**목적**: 5개 경쟁사 재무 건전성 비교 분석

**기술 스택**: `pandas` `matplotlib` `seaborn`

[📂 프로젝트 보기](./01-pandas-financial-analysis/)

**분석 지표**
- 유동비율, 부채비율, ROE, ROA
- 3개년 추이 분석
- 산업 평균 대비 포지셔닝

---

### 3. 회계 데이터베이스 설계
**목적**: 중소기업용 복식부기 회계 시스템 DB 설계

**기술 스택**: `MySQL` `Python` `ERD`

[📂 프로젝트 보기](./03-sql-database-design/)

**특징**
- 정규화된 테이블 설계 (거래, 계정과목, 거래처)
- 분개 자동 검증 쿼리 (차변=대변)
- 월별/분기별 집계 최적화 인덱스

---

## 🛠️ 기술 스택

| 분야 | 기술 | 숙련도 |
|-----|------|--------|
| 데이터 처리 | pandas, numpy | ⭐⭐⭐⭐ |
| 엑셀 자동화 | openpyxl, xlwings | ⭐⭐⭐⭐ |
| 데이터베이스 | MySQL, SQLite | ⭐⭐⭐ |
| 시각화 | matplotlib, seaborn | ⭐⭐⭐ |
| 버전 관리 | Git, GitHub | ⭐⭐⭐ |

## 📫 연락처
- Email: your.email@example.com
- LinkedIn: linkedin.com/in/yourprofile
- Blog: yourblog.com (선택)

## 📜 라이선스
MIT License - 자유롭게 사용 가능합니다.
