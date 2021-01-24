세팅열기 컨트롤 + , 



https://github.com/prettier/eslint-plugin-prettier#options

prettier 설정

> https://uxgjs.tistory.com/150



오늘 할일

1. prettier, Eslint 배포
2.  readme 작성
3. 이불정리 OKAY
4. 



```
1.리액트 프로젝트 생성
	> create-react-app 프로젝트이름 --use-npm
	(CRA )
2. Prettier 설치
	> npm i prettier -D -E
	(-D는 --save-dev의 축약법,-E는 --save-exac의 축약법이다. 위 ESLint 모듈을 설치할때와 다르게 Prettier에서는 이 옵션을 붙이는 것을 권장하는데, 버전이 달라지면서 생길 스타일 변화를 막기 위해서라고 한다.)
3. 추가 모듈 설치
	> npm i eslint-plugin-prettier eslint-config-prettier -D
	[eslint-config-prettier
ESLint의 formatting 관련 설정 중 Prettier와 충돌하는 부분을 비활성화 한다.
eslint-plugin-prettier
Prettier를 ESLint 플러그인으로 추가한다. 즉, Prettier에서 인식하는 코드상의 포맷 오류를 ESLint 오류로 출력해준다.]

4. 프로젝트 루트 경로에 .eslintrc.json 파일 생성 후 아래내용 추가
{
  "plugins": ["prettier"],
  "extends": ["eslint:recommended", "plugin:prettier/recommended"],
  "rules": {
    "prettier/prettier": "error"
  }
}

5. ESLint, Prettier 익스텐션 설치
```

5. VS code 설정

-  VSCode 설정(윈도우, 리눅스에서는 Ctrl + , 으로 들어간다. .vscode/settings.json 을 연다(사진 참고).

```
{
  // Set the default
  "editor.formatOnSave": false,
  // Enable per-language
  "[javascript]": {
    "editor.formatOnSave": true
  },
  "editor.codeActionsOnSave": {
    // For ESLint
    "source.fixAll.eslint": true
  }
}
```

위 내용 복붙 후 저장

6. ESLint 설정(여기선 Airbnb를 적용해 보겠다.)

   >npm i -D eslint-config-airbnb

7. 그리고 `.eslintrc.json`파일의 `"extends"`속성에 `"airbnb"`를 추가 해준다.

```
{
  "plugins": ["prettier"],
  "extends": ["eslint:recommended", "plugin:prettier/recommended", "airbnb"],
  "rules": {
    "prettier/prettier": "error"
  }
}
```

8. Prettier 설정

> ESLint 설정 파일과 마찬가지로 루트 경로에 `.prettierrc.json`을 만들어 준다. [Prettier의 옵션 문서](https://prettier.io/docs/en/options.html)에서 필요한 옵션을 골라 설정해 주면 된다. 아래는 간단한 예시이다.

```
{
  "trailingComma": "es5",
  "tabWidth": 2,
  "semi": true,
  "singleQuote": true
}
```

> 콤마가 자동텝 2번, 새미콜론 추가가 될 것이다 



화면 정의서는웹디자인과 기술  포함해야함

 와이어프로그램(웹디자인) 꼭 필수작성

간트차트 깃랩에 리드미에 꼭 작성하기

모메이드 엔진, 간트 차트 작성 문법 확인하기.



