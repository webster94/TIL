



게시글을들을 띄어 줄 것임

1. LIST.vue에가서 b- table 확인

<img src="C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207130457550.png" alt="image-20201207130457550" style="zoom: 200%;" />

bootstrap Vue >> DOC , getting start 검색

vuetify 검색! 수민누나랑 필요한거였네



아이템을 서버에서 얻어야함



 items : [] 빈배열로 형성

서버의 보드 컨트롤러가 있음. 분석하라는게 아님

게시판의 글목록 파라미터 조건이 있음.

요청을 하면 controller에서 json으로 응답해준다.

<img src="C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207131423455.png" alt="image-20201207131423455" style="zoom:200%;" />

> board
>
>  board.js , memo.js 작성!

서버 board에서 작성하고 create에서 가져올것임

create

<img src="C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207131714723.png" alt="image-20201207131714723" style="zoom:200%;" />

![image-20201207132129172](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207132129172.png)

![image-20201207132140083](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207132140083.png)

List는 listArticle을 사용할 수 있다,



List.vue에서 

life cycle

![image-20201207132515455](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207132515455.png)

성공 ,실패 시ㅣ 

![image-20201207132537206](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207132537206.png)

데이터가 들어올 것, 우린 아무것도 안썼으니 데이터가 없다.

데이터 확인!

확인 후 item에 responce를 넣는다.

![image-20201207132646601](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207132646601.png)

> 위와같이! 리스폰스 끝!![image-20201207132910497](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207132910497.png)
>
> > Register.vue! 

![image-20201207132855970](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207132855970.png)

submit이 가지고 있는 것을 고유의 값을 서버로 보내지말고 내가 적은 것만 보낼 때 사용하는 방법



보낼 때 받아내는 방법![image-20201207133042235](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133042235.png) 

![image-20201207133020763](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133020763.png)

여기에 받아짐!

![image-20201207133249772](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133249772.png)

userid 작성, vuex 에 user

![image-20201207133324398](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133324398.png)

userinfo 확인

![image-20201207133412077](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133412077.png)

vuex에서 mapstate를 가져온다

computed에 다가 

![image-20201207133520580](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133520580.png)

![image-20201207133547207](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133547207.png)

userid를 저장한다.

이걸 가지고 글을 써야한다.

board 이동

![image-20201207133617356](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133617356.png)

복사

![image-20201207133625636](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133625636.png)

![image-20201207133727949](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133727949.png)

수정 후 수출

레지스터에서 사용

![image-20201207133815181](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133815181.png)

![image-20201207133901612](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207133901612.png)

폼안에는 아이디 제목, 내용 적혀있음.

this.items = response.data를 지우고 this.$router.push(name} : 'board/')

![image-20201207134105407](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207134105407.png)



리스트 뷰로 이동해서 click을 하면 detailfh 이동..?

![image-20201207134248131](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207134248131.png)

이 페이지들어오자마자 디비에서받아서 화면에 바로 뿌리자

create() 에서 데이타를 얻어내야함

axios를 써야하니까 

![image-20201207134551027](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207134551027.png)

![image-20201207134612639](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207134612639.png)

get으로 수정.

![image-20201207134650071](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207134650071.png)

글 삭제는 getarticle과 비슷.



글 수정은 글 쓰기와 비슷

![image-20201207134736826](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207134736826.png)

패턴은 맞춰주는게 좋으니 백틱으로 사용

![image-20201207134808046](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207134808046.png)

더 이상 board로 들어올 일은 없음.



![image-20201207134911944](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207134911944.png)

![image-20201207135227710](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207135227710.png)



디테일에서 딜리트article남았따



![image-20201207135632731](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207135632731.png)

![image-20201207135644024](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207135644024.png)



이제 글 수정이 남았따

![image-20201207135835535](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207135835535.png)

![image-20201207135857561](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207135857561.png)

modify .vue로 이동

![image-20201207135921981](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207135921981.png)

import!

modify에 정보를 쫙 깔아줘야한다.

create 사용!

![image-20201207140032892](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207140032892.png)

![image-20201207140211106](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207140211106.png)

![image-20201207140234796](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207140234796.png)

![image-20201207140348436](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201207140348436.png)

수정 완료!!





---

문병로 교수님 특강



