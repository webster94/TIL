<template>
  <div>
    <input type="text" :value ='userInput'
    @change='onChange'>
  </div>
</template>

<script>
export default {
  props:{
  userInput: String,
  },
  methods:{
    onChange(event) {
      this.$emit('changeUserInput',event.target.value)
      // 발생하면 앱이 캐치해서
    }
  }
}
</script>

<style>

</style>