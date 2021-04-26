[
MYDSPACE](https://velog.io/@dear_sopi9211)

로그인

[MYDSPACE](https://velog.io/@dear_sopi9211)

로그인

# [react-native] 안드로이드 APK(AAB) 파일 생성하기📱

**[dear_sopi9211](https://velog.io/@dear_sopi9211)**·2020년 8월 18일

[android](https://velog.io/tags/android)[app](https://velog.io/tags/app)[google](https://velog.io/tags/google)[google play console](https://velog.io/tags/google-play-console)[reactnative](https://velog.io/tags/reactnative)[release](https://velog.io/tags/release)



2





![image-20210414171117168](C:\Users\multicampus\Desktop\TIL\21-04-14.assets\image-20210414171117168.png)



[1. key store 생성](https://velog.io/@dear_sopi9211/react-native-안드로이드-APKAAB-파일-생성하기#1-key-store-생성)

[2. 프로젝트에 키 저장소 추가](https://velog.io/@dear_sopi9211/react-native-안드로이드-APKAAB-파일-생성하기#2-프로젝트에-키-저장소-추가)

[3. Gradle 전역 변수 설정](https://velog.io/@dear_sopi9211/react-native-안드로이드-APKAAB-파일-생성하기#3-gradle-전역-변수-설정)

[4. 앱의 Gradle config에 signing release 설정 추가](https://velog.io/@dear_sopi9211/react-native-안드로이드-APKAAB-파일-생성하기#4-앱의-gradle-config에-signing-release-설정-추가)

[5. release APK 생성 (AAB)](https://velog.io/@dear_sopi9211/react-native-안드로이드-APKAAB-파일-생성하기#5-release-apk-생성-aab)

[⭐️ 참고한 사이트](https://velog.io/@dear_sopi9211/react-native-안드로이드-APKAAB-파일-생성하기#️-참고한-사이트)

## [react-native](https://velog.io/@dear_sopi9211/series/react-native)



목록 보기

1/3



![img](C:\Users\multicampus\Desktop\TIL\21-04-14.assets\안드로이드사진.png)

> Production test build 하기 전에 먼저 해당 프로젝트 에뮬레이터 또는 Android device에서 성공적으로 컴파일이 되고 실행이 되고 오류는 없는지 확인한 후 진행하여야 합니다.



## 1. key store 생성

Android 용 React Native 실행 바이너리를 생성하는 데 사용되는 key store file 인 Java 생성 서명 키가 필요합니다. 다음 명령을 사용 하여 터미널 에서 keytool 을 사용하여 만들 수 있습니다.

```null
keytool -genkey -v -keystore your_key_name.keystore -alias your_key_alias -keyalg RSA -keysize 2048 -validity 10000
```

여기서 **your_key_name**과 **your_key_alias**을 원하는 이름으로 작성을 해줍니다.
your_key_alias 은 나중에 앱에 서명 할 때 사용할 이름으로 따로 기록해두시는게 좋습니다.
또 해당 키는 보안성이 좋아야 하기때문에 기본값 1024 대신 탈취하기 보다 어려운 2048로 변경하였습니다.

해당 명령어는 해당 키 저장소의 정보 필드값을 입력하라는 문구가 나오게 됩니다.

```null
Enter your keystore password: password123 
// 원하는 키 비밀번호 여기서 저는 대문자, 소문자, 숫자, 특수기호를 모두 넣은 최소 8자리 이상의 비밀번호를 사용하였습니다.
Re-enter new password: password123
What is your first and last name? [unknown]: Dani Williams // 개발자 이름
What is the name of your organizational unit? [unknown]: Sample Company // 회사 개발팀 
What is the name of your organization? [unknown]: Sample // 회사이름
What is the name of your city or Locality? [unknown]: XYZ // 대한민국
What is the name of your State or Province? [unknown]: ABC // 서울
What is the two-letter country code for this unit? [unknown]: XX // 국가코드 알파벳 KR
```

다 작성하게 되면 해당 문구가 나오는 경우가 있으나 저에게는 따로 나오지않았습니다.
해당 문구가 나오지 않는 경우 **your_key_alias 비밀번호는 keystore 비밀번호와 동일합니다.**
나온다고 한다면 만약 새로운 비밀번호가 필요할때 작성하면 됩니다.

```null
 Enter key password for <your_key_alias> 
```

다 완료하고 나면 결과적으로 10000일 동안 유효한 해당 your_key_name.keystore 라는 프로젝트 디렉토리에 키저장소 파일이 생성되게 됩니다.

> Google play console 에 한번 업로드된 key store file은 변경되지 않으니 잘 보관할 수 있도록 합니다.
> 백업 필수 🔥🔥🔥
> 만약 분실하였거나 도용된 경우 해당 사이트로 가서 지침을 따라야합니다.
> https://support.google.com/googleplay/android-developer/answer/7384423#reset





## 2. 프로젝트에 키 저장소 추가

your_key_name.keystore 파일을 복사한 후 나의 React Native 프로젝트 폴더 안에 android/app 디렉토리 안에 붙여 넣기 해줍니다.

```null
mv my-release-key.keystore / android / app
```

![img](C:\Users\multicampus\Desktop\TIL\21-04-14.assets\안드로이드.png)





## 3. Gradle 전역 변수 설정

파일 ~/.gradle/gradle.properties 또는 android/gradle.properties을 편집하고 다음을 추가합니다 ( *****올바른 키 저장소 암호, 별칭 및 키 암호로 대체 ).

```null
MYAPP_UPLOAD_STORE_FILE=my-upload-key.keystore
MYAPP_UPLOAD_KEY_ALIAS=my-key-alias
MYAPP_UPLOAD_STORE_PASSWORD=*****
MYAPP_UPLOAD_KEY_PASSWORD=*****
```

이 변수는 전역 Gradle 변수가 될 것이며 나중에 앱에 서명하기 위해 Gradle 구성에서 사용할 수 있습니다.

> 만약 보안상의 이유로 해당 암호를 텍스트로 저장하지 않고 OSX를 실행하여 해당 앱에 비밀번호를 저장 할 수도 있습니다.
> https://pilloxa.gitlab.io/posts/safer-passwords-in-gradle/
> 그렇게 되면 마지막 두 행을 건너뛸수 있습니다.





## 4. 앱의 Gradle config에 signing release 설정 추가

프로젝트 폴더의 **android/app/build.gradle** 파일에서 해당 release를 추가합니다

```null
...
android {
    ...
    defaultConfig { ... }
    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_UPLOAD_STORE_FILE')) {
                storeFile file(MYAPP_UPLOAD_STORE_FILE)
                storePassword MYAPP_UPLOAD_STORE_PASSWORD
                keyAlias MYAPP_UPLOAD_KEY_ALIAS
                keyPassword MYAPP_UPLOAD_KEY_PASSWORD
            }
        }
    }
    buildTypes {
        release {
            ...
            signingConfig signingConfigs.release
        }
    }
}
...
```





## 5. release APK 생성 (AAB)

> 보통 APK 파일을 업로드를 하게 되면 해당 google play console에서 해당 앱의 용량을 압축하여 업로드 하라고 안내문구를 띄웁니다.
> 그래서 google play 에서 제공해주는 Android App Bundle 을 사용하여 앱의 모든 컴파일된 코드 및 리소스를 포함하며 APK 생성 및 서명을 Google Play에 맡기고 각 기기 설정에 맞게 최적화된 APK를 생성합니다.

터미널에서 해당 명령어를 실행합니다.

```null
cd android
./gradlew bundleRelease
```

Gradle bundleRelease 는 앱을 실행하는데에 필요한 모든 자바스크립트를 AAB 번들로 제공합니다.

성공하면 **android/app/build/outputs/bundle/release** 폴더 안에 .aab 파일이 생성됩니다.

짜잔!!!😎 🎶

만약 APK 파일로 생성하고 싶다고 한다면 해당 명령어를 실행합니다.

```null
cd android
./gradlew app:assembleRelease
```

### ⭐️ 참고한 사이트

1. https://www.instamobile.io/android-development/generate-react-native-release-build-android/
2. https://reactnative.dev/docs/signed-apk-android

[![profile](C:\Users\multicampus\Desktop\TIL\21-04-14.assets\Image from iOS (1).jpg)](https://velog.io/@dear_sopi9211)

[sophia](https://velog.io/@dear_sopi9211)

front-end developer



[다음 포스트[react-native\] Android release Trouble Shooting 💥☄️](https://velog.io/@dear_sopi9211/react-native-Android-release-Trouble-Shooting)

#### 0개의 댓글

댓글 작성