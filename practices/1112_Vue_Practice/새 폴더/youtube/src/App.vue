<template>
  <div id="app">
    <SearchBar :userInput ='userInput'
    @changeUserInput="onChangeUserInput"/>
    <VideoList :videos="videos" @select-video="onVideoSelect"/>
    <VideoDetail :video="selectedVideo"/>
    
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'
export default {
  name: 'App',
  components:{
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data(){
    return {
      userInput: '',
      videos: [],
      selectedVideo: '',
    }
  },
  methods: {
    onChangeUserInput(input){
      this.userInput = input
      // 유튜브 영상 검색하는 api를 사용!
      const API_URL='https://www.googleapis.com/youtube/v3/search'
      const API_KEY='AIzaSyAz7vGBiiYvHa_6aKtd1f3mxl-Fz2Oh6EY'
      if(this.userInput===''){
        return
      }
      axios({
        url:API_URL,
        method:'GET',
        params:{
          key:API_KEY,
          part: 'snippet',
          type: 'video',
          q:this.userInput
        }
      }).then(res=>{
        this.videos = res.data.items
        console.log(res)
      }).catch(err=>{
        console.error(err)
      })
    },
    onVideoSelect: function(video) {
      this.selectedVideo = video
    }
  },
  watch: {
    userInput(value) {
      if (value === 'bad') {
        alert('말조심')
        this.userInput = ''
      }
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
