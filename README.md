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
