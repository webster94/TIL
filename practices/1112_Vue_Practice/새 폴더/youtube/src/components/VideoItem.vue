<template>
  <div @click="selectVideo">
    <li><img :src="thumbnailUrl" alt="thumbnail" width = "300" height="300"></li>
    
    <span>{{title}}</span>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  props:{
    video:Object,
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  },
  computed:{
    thumbnailUrl() {
      return this.video.snippet.thumbnails.medium.url
    },
    title() {
      return _.unescape(this.video.snippet.title)
    }
  },
}
</script>

<style>

</style>