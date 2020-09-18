# git

> Git은 분산버전관리시스템이다.

## 준비하기

윈도우에서 git을 활용하기 위해서 [git bash](https://git-scm.com/downloads)를 설치합니다.

초기 설치를 완료한 이후에, 계정설정을 진행합니다.

```sh
$ git config --global user.email{이메일 주소}
$ git config --global user.name webster94
```

## 로컬 저장소 활용하기

### 1. 저장소 초기화

> 이제부터 이 디렉토리를 git으로 관리하겠다!(변경 이력을 감시하겠다)

```sh
$git init
```

- `.git` 디렉토리가 생성되며, 여기에 git과 관련된 모든 정보가 저장됩니다.
- 초기화를 하고나면 gitbash에 `(master)` 라고 표시가 되는데, 이는 이 디렉토리는 이미 git이 관리하고 있다는 뜻으로 생각할 수 있습니다.
- 이미 초기화 한 repo에서는 다시 git init을 하지않습니다.

### 2. add

> working directory 작업 공간에서 변경된 사항을 이력으로 관리하기 위해서는 반드시 staging area를 거쳐야 한다.



```sh
$git add {staging 할 파일 . 사용}
```

### 3.commit

> 이력을 확정 짓는, 즉 기록을 남기는 명령어이다.
>
> ```sk
> $git commit - m '커밋 메세지'
> ```

커밋 기록을 확인하고 싶다면 아래의 명령어를 참고하세요.

```sk
$ git log
```

### 4.status

> git을 쓰면서 가장 많이 사용해야 하는 명령어, 현재 상황을 확인할 수 있다.



```sk
$git statuS
```

## 원격저장소 활용하기

여러 서비스 중, github을 기준으로 설명합니다.

### 1. 준비사항

- github에 회원가입 후 빈repo를 만들어둔다.

### 2.원격 저장소 등록

- 로컬저장소와 원격 저장소를 연결하는 일입니다.

```sk
$ git remote add orgin{github repo url}
```

- 원격 저장소(remote)를 등록할건데, `origin`이라는 이름으로 원격 저장소를 등록하겠다라는 의미입니다.
- 원격 저장소 등록 현황을 확인하려면 아래의 명령어를 참고하세요.

```sh
$git remote -v
```



```git
$git push origin master
```





# 4. 원격저장소에서 로컬로 가져오기

> github이나  gitlab의  repo주소를 복사해둔 뒤,

```sh
$ git clone {가져오고자 하는 repo url}
```



# 5. 자리 변경 시 해야할 일들



1.  자격 증명 제거

2. git clone

3. 계정 이름/메일 변경

    

> 

![image-20200919011946430](C:\Users\Minho\AppData\Roaming\Typora\typora-user-images\image-20200919011946430.png)