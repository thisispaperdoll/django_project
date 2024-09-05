# 첫 번째 단계: 빌드 환경
FROM python:3.11-slim AS builder

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사 (필요한 파일만 복사)
COPY . .

# 두 번째 단계: 최종 이미지
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# 빌드 단계에서 설치된 패키지 복사
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 프로젝트 파일 복사 (필요한 파일만 복사)
COPY --from=builder /app /app

# 불필요한 파일 제거
RUN rm -rf /app/tests /app/docs

# 환경 변수 설정
ENV DJANGO_SETTINGS_MODULE=fisa_django.settings
ENV PYTHONUNBUFFERED=1

# Gunicorn을 사용하여 애플리케이션 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fisa_django.wsgi:application"]

## 3시 40분까지
## 1) docker image로 만드셔서 {본인도커허브명}/django-project:v1
## 2) 되는지 run 명령어로 확인하시고 locahost:8000 으로 접속도 해보세요
## 3) ec2 컨테이너를 하나 만들어서 {본인이름명}-django-ec2
## 4) 그 안에서 run 명령어로 띄우고
## 5) ip 주소로 접속까지 해주세요
