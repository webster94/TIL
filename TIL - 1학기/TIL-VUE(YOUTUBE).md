유튜부를 만들어보고 자자

![image-20201113220540166](C:%5CUsers%5CMinho%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20201113220540166.png)

순서



searchBar에서 input에 데이터를 받고

부모 컨포넌트인 app에 $emit을 통해 보내준다.



app은 searchBar에서 온 데이터를 저장할 데이터(return)의 변수를 설정하고 Axios 요청을 할 준비를 한다.

params에 key, q, part, type을 정리한다. 다음은 methods 함수를 통해 searchbar로 온 inputText를 변수에 기입한다 (이 때, 잘 왔는지 1차 확인 필요)

잘 왔다면 axios.get(API_URL)과 {params}를 실시 하고 Promise를 통해 .then,  catch로 설정한다.

.then(res)에서 res.data.items 를 변수 videos에 기입하고 리스트로 보낼 준비를한다.





부모에서 자손으로 보낼 때 필요한 것 3가지

1. 불등보
2.  자손 옆에 : (바인딩을 넣고) 바인딩 옆에 자손이 받을 데이터 명 , 다음은 현재폴더에서 내려보낼 파일을 = " "안에 적어준다.
3. 자손에 props를 설정하여 파일의 형태로 받아준다.



VideoList에서 video를 한개씩 보내기 위해 v-for를 사용할 때 key값을 보내야하는데 이때 고유의 값인 id를 활용한다. 

v-for = "(video,idx) in videos" :key="idx" :video="video"



VideoListItem에서 img의 src에 변하는 값을 함수를 통해 넣어준다

computed : { VideoItemImageSrc: function() { return this.video.snippet.thumbnails.defalt.url}} 

특수문자 재정리법

filter를 활용한다

import _ from 'lodash'

StringUnescape : function(rawtext) { return _.unescape(rowtext)} 



template에는

{{video.snippet.title | stringUnescape }}

여기까지가 app에서 videoItem까지 내려오는방법이다.



이제 videodetail로 video 한개를 올려주자

올릴 때 는 this.$emit을 상위 콤포넌트에서 사용할 함수이름과 올려보낼 데이터를 함께 보낸다

selectedvideo : function(){ this.$emit("select-video", this.video)}

template에선 li가 video 한개 니깐 li 에 @click = "selectedvideo"를 넣어준다.

Videolist에선  @select-video를 받고 = " onselectVideo"함수를 실행하게한다

onselectVideo는 = function(video) { this.$emit('select-video',video)}를 통해 한번더 상위 컴포넌트로 올려준다.

이때 devtool에서 비디오를 클릭하면 이벤트가 2개가 발생하는 것을 확인한다.

app에서는 @selet-video= "ONselecVideo"를 실행하고

OnselectVideo에서는 selectedVideo란 빈 변수에 video를 저장한다.

저장을 완료하면 다시 detail로 내리자

내릴 때 필요한 3가지

1. 불등보

2. :자식이 받을 이름(video) = "내가 보낼 파일 (selectdVideo)"

3. props {

   video : [Object,String]

   }

   4. @select-video = "VideoURL"

   

  

유부브 영상 출력

div에 v-if="video"

Iframe :src="videoURL"

VideoURL =function(){

const VideoId = this.video.id.videoId

return `http://wwww.youtunbe.com/embed/${VideoId}`}