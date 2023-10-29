"""
오픈 소스 프로젝트 참가
1. 개발 과정에서 개발 역량 향상 및 보유 스킬 능력 제시 (향상)
2. In-house 개발과 달리 수 많은 디버깅, 개선 등을 통해 신뢰성, 안정성 높은 어플리케이션 도출 가능
3. 적시에 사용 가능 (아키텍처 효용성, 고품질 보장)
4. 하지만, 문서, 개선 가능성, 지적 재산권 (라이센스) 주의 필요

오픈 소스(사이드 프로젝트) 참가 
1. 답변, 기능 추가, 사명감 (누군가에게 도움)
2. 다양한 이슈 해결을 통한 개발 역량 강화 (개발 실력 상승)
3. 코드 퀄리티, 알고리즘, 다양한 지식 향상
4. 구직시 합격 가능 매우 높음 (이미 알려짐, 인지도), 창업시 좋은 팀원 셋업 가능성 향상
5. 이슈 등재를 통해서 문제 해결 가능성 매우 높음
6. 복잡하고 다양한 기능 배재하고 처음에는 단 몇 줄이라도 오픈소스 업로드 추천
7. 효율적인 코드 작성 노하우 향상
8. 서로 공유하고 돌려주는 문화 체험

다양한 오픈소스 Licenses 종류
>>> https://www.olis.or.kr/license/compareGuide.do
ex) mit license file
>>> https://choosealicense.com/licenses/mit/

setup.py
1. pypi classifiers 검색
>>> https://pypi.org/classifiers/

필수 files
>>> https://alone-djangonaut.com/a-tour-on-python-packaging#keyring
0. __init__.py, xxxx.py
1. LICENSE
2. setup.py
3. MANIFEST.in
기본 files
1. README.md
2. requirements.txt
3. setup.cfg
    Error ; HTTPError: 401 Unauthorized from https://upload.pypi.org/legacy/
    User jadejung has two factor auth enabled, an API Token or Trusted Publisher must be used to upload in place of         password.
    >>> https://khorkeanteng.medium.com/publish-a-packaHTTPError:%20401%20Unauthorized%20from%20https://upload.pypi.org/legacy/%20User%20jadejung%20has%20two%20factor%20auth%20enabled,%20an%20API%20Token%20or%20Trusted%20Publisher%20must%20be%20used%20to%20upload%20in%20place%20of%20%20%20%20%20%20%20%20%20password.ge-on-pypi-ab6de8a0f8d3

    PS D:\2022\Python\inflearn\package\jpgTogif\upload_package> python -m twine upload dist/*
    Uploading distributions to https://upload.pypi.org/legacy/
    Enter your username: __token__
    Enter your password: ctrl + shift + v

PyPI
your projects -> view -> Download files

##### 학습법
TDD, REFACTORING, OOP 
FEEDBACK, CODE REVIEW
PLATFORM(AWS, AZURE, GCP)
TRENDY TECH., UPDATE INFORMATION OF OPEN SOURCE
DEBUGING, REFERENCE IN ENGLISH
SIDE PROJECT, HACKETHON
OPEN SOURCE -> 
"""