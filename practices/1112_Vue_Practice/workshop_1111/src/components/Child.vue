<template>
  <div>
    <h1>Child</h1>
    <input type="text" @keyup="onChildDataChange">
    <p>appData: 123</p>
    <p>ParentData: 234</p>
    <p>childData: {{childData}}</p>
  </div>
</template>

<script>
export default {
  methods: {
    onChildDataChange(event){
      this.$emit('onChildDataChange',event.target.value)
    }
  }
}
</script>

<style>

</style>