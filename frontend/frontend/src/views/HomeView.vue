<script>



export default {
  data() {
    return {
      test: ""
    }
  },
  methods: {
    checktoken() {
      if (localStorage.getItem("token") === null) {
        return false
      } else {
        return true
      }
    }
  }
}

</script>

<template>
<p class="dark:text-white">HELOOOOOOO</p>
</template>

<style scoped>

</style>