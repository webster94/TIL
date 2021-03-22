

# React Native 초기설정 

> 설치 및 환경설정 순서
>
> - React Native CLI
> - JDK
> - Android Studio
> - SDK 설정
> - Android Studio 환경 변수 설정
> - 프로젝트 설치 및 실행

> Node.js와 python,  JDK 설치된 상태에서 시작

### 1. React Native CLI 설치

> ```
> npm install -g react-native-cli
> ```



### 2. 안드로이드 스튜디오 설치

react-native로 안드로이드 앱을 개발하려면 안드로이드 스튜디오를 설치해야 합니다. 아래의 공식홈페이지에서 다운로드 해주세요.

> 안드로이드 스튜디오 https://developer.android.com/studio

설치 프로그램을 실행 후 진행하다 보면, 아래와 같이 Choose Components 화면이 나온다. Android Virtual Device를 선택하고 Next 버튼을 눌러 다음으로 진행한다.![img](https://media.vlpt.us/images/kyo3553/post/242592ae-7eb0-4804-bff0-622f3574fda9/android_studio_choose_components.jpg)
설치 마지막 단계에서 Finish를 눌러 설치를 완료하면 다음과 같은 화면이 나온다. OK를 눌러 진행한다.![img](https://media.vlpt.us/images/kyo3553/post/fa59d4bb-1b42-43b2-b416-9fe5cb656cfe/android_studio_start.jpg)
다음 화면으로 이동하다 보면 Install Type을 설정하는 창이 등장하는데 Custom을 선택 후, 원하는 테마를 설정해준다.![img](https://media.vlpt.us/images/kyo3553/post/84537843-93e0-4ecd-bd73-6d6b12b3fb0e/configure_android_studio_install_type.jpg)
다음 화면으로 이동하면, 아래와 같이 SDK Components Setup 화면이 등장한다. Performance 와 Android Virtual Device부분을 선택하여 진행한다.
![img](https://media.vlpt.us/images/kyo3553/post/bcbf1338-df9b-4da5-8739-1eef7db03f8c/configure_android_studio_sdk_components_setup.jpg)
이 다음부터는 일반적인 프로그램 설치 과정이므로, 남은 과정을 진행해주면 설치가 완료되며, 안드로이드 스튜디오가 실행되는 것을 확인할 수 있다.

### 3. SDK 설정

안드로이드 스튜디오 오른쪽 하단의 `Configure`에서 `SDK Manager`를 실행시킨다.!![img](https://media.vlpt.us/images/kyo3553/post/493ee33b-77c4-4027-a46f-5ee2c43db037/android_studio_configure_sdk.jpg)
위의 창이 등장하면, `Show Package Details`를 선택하고 아래의 내용을 참고하여 선택해준다.

> - Android SDK Platform 28
> - Intel x86 Atom System Image
> - Google APIs Intel x86 Atom System Image
> - Google APIs Intel x86 Atom_64 System Image

### 4. 안드로이드 스튜디오 환경 변수 설정

내 PC를 우클릭하고 속성 메뉴를 클릭한다. 속성메뉴를 선택하면, 아래와 같은 설정화면이 등장한다.![img](https://media.vlpt.us/images/kyo3553/post/ac0a20f6-1308-40f0-b845-fe77d6e1dbef/android_studio_configure_environment_variable_system_setting_ko.jpg)

> 고급 시스템 설정 > 고급 tab > 환경변수

차례대로 진행하면 설정창이 하나 등장하는데, 상단에 위치한 사용자 변수 섹션의 새로 만들기를 누른다. 계속하여 아래의 이미지를 참고하자.
![img](https://media.vlpt.us/images/kyo3553/post/39ec6395-c047-4b4d-9578-efa15b675bc9/990941455E82FAEF0A.png)

변수이름에 `ANDROID_HOME`을 입력하고, 자신의 안드로이드 스튜디오 SDK위치를 변수 값에 입력한다.

> SDK 위치를 모른다면, `SDK Manager`를 실행 시켰을 때, 설정 창 상단부분의 `Android SDK Location`을 확인할 수 있다.

환경변수 추가 후, `platform-tools`를 설정해야한다. 사용자 변수 리스트에서 `Path`를 선택한다.![img](https://media.vlpt.us/images/kyo3553/post/82935ac7-b2dc-4f97-a60e-4dd7fc835858/android_studio_configure_environment_variable_edit_path_ko.jpg)
SDK가 설치된 폴더 하위에 있는 platform-tools폴더를 입력하고, 확인을 눌러 수정해준다.

> 위의 과정이 모두 완료되면, 명령 프롬프트를 실행하여 아래의 명령어를 입력한다
>
> `adb`
> 환경 변수 설정이 성공적으로 완료되었다면, 버전확인이 가능하다.

### 5. 프로젝트 생성해보기

> `npm config set save-exact=true`
> 위의 코드를 통해 npm버전을 고정시켜 사용하는 것을 권장한다.
>
> react-native는 버전에 따라, 잘 동작하던 앱이 동작을 안하거나, 빌드할 때 에러가 발생하는 등 여러 문제들을 일으킬 가능성이 높기 때문이다.

React Native CLI 명령어를 통해 react-native 프로젝트를 생성한다.

> ```
> react-native init FirstApp
> ```

프로젝트 생성 후, 프로젝트 폴더로 이동하여 실행시켜 본다.

> `cd FirstApp` 프로젝트 폴더 이동
> `npm run android` 프로젝트 실행!

![img](https://media.vlpt.us/images/kyo3553/post/ced5b011-1d0e-4557-84c7-5f12e483b5cb/993FAA335E82FAF410.png)