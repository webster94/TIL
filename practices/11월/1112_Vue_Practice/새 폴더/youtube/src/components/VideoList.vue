<template>
  <li>
    <VideoItem v-for="video in videos" 
    @select-video='selectVideo'
    :video="video" :key="video.id.videoId"/>
    <!-- <iframe src="videoSrc" frameborder="0"></iframe> -->
  </li>
 
</template>

<script>
import VideoItem from './VideoItem.vue'
export default {
  components: {
    VideoItem,
  },
  methods: {
    selectVideo: function(video) {
      this.$emit('select-video', video)
    }
  },
  props: {
    videos: Array,
  },
  // computed: {
  //   videoSrc() {
  //     return "https://www.youtube.com/embed/${this.videos[0].id.videoId}"
  //   }
  // }
}
</script>

<style>

</style>