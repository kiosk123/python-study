# 파이썬 공부

## 개발 환경
* 이클립스 pydev - 설정 [참고](https://we-always-fight-with-code.tistory.com/35)
* 파이썬 3.7.4 - [다운로드](https://www.python.org/downloads/)
* 리눅스에서 파이썬 설치 (Centos8 기준)

```
$ sudo yum install -y python

# 직접 소스로 부터 파이썬 패키지 설치
$ tar -zxvf Python-3.7.4.tgz
$ cd Python-3.7.4/
$ ./configure

$ make
$ sudo make install

# 파이썬3 실행 - putty같은 원격 클라이언트로 접속시 재접속해야 반영됨
$ python3

```

* 설치 중 오류 해결

```
# ./configure 실행시 
# configure: error: no acceptable C compiler found in $PATH 발생할경우
$ sudo yum install -y gcc

# 설치중 zipimport.ZipImportError: can't decompress data; zlib not available 발생시
$ sudo yum -y install zlib*

# 다음과 같은 RPM 오류 발생시
# RPM: 오류: db5 error(-30969) from dbenv->open: BDB0091 DB_VERSION_MISMATCH: Database environment version mismatch
# RPM: 오류: cannot open Packages index using db5 -  (-30969)
# RPM: 오류: /var/lib/rpm 안의 패키지 데이터베이스를 열 수 없습니다
# 다운로드 된 패키지는 다음 번 성공적인 트랜잭션까지 캐시에 저장되었습니다.
$ sudo mkdir /tmp/bak
$ sudo mv /var/lib/rpm/__db* /tmp/bak/
$ sudo rpmdb --rebuilddb

# ModuleNotFoundError: No module named '_ctypes' 발생시
# 참고 : https://growingsaja.tistory.com/244
$ sudo yum install -y libffi-devel
```

## 환경변수 설정

윈도우는 시스템 속성 - 고급 - 환경 변수를 통해 설정  
리눅스는 .bash_profile 또는 .bashrc를 통해 설정 할 것을 권장 - [참고](https://somjang.tistory.com/entry/PythonUbuntu%EC%97%90%EC%84%9C-Python37-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0bashrc%ED%8C%8C%EC%9D%BC%EC%88%98%EC%A0%95)
전체 사용자에게 동일하게 적용할 경우 /etc/environment 파일을 이용하여 설정할 것  

* PATH  
실행 파일을 찾는 경로의 모음 python.exe가 있는 폴더 추가 
리눅스는 /usr/local/bin/python3 경로 설정  
리눅스에서 PATH 설정 잘못할 경우 초기화 방법은 다음 [링크](https://somjang.tistory.com/entry/Ubuntu-PATH%EA%B0%92-%EC%B4%88%EA%B8%B0%ED%99%94-%ED%95%98%EA%B8%B0) 참고

* PYTHONPATH
파이썬에서 import 키워드를 이용한 파이썬 모듈을 찾는 추가 경로의 모음

* PYTHONSTARTUP
파이썬 인터프리터를 실행할 때 자동으로 실행되는 파이썬 스크립트 파일  
매번 사용해야 할 모듈이 있으면 이 변수를 활용하는 것을 권장 - (**대화식 모드에서 만 동작**)

 - 챕터
     - ch01. 파이썬 기본
