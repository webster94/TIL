<template>
  <div v-if="video">
    비디오 디테일 컴포넌트
    <iframe width="560" height="315" allowfullscreen :src="videoSrc" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  name : 'VideoDetail',
  props: {
    video : [Object,String],
  },
 computed: {
    videoSrc() {
      return `https://www.youtube.com/embed/${this.video.id.videoId}?start=60`
    }
  }
}
</script>

<style>

</style>