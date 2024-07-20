<script>

if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark')
} else {
  document.documentElement.classList.remove('dark')
}

import Header from './components/Header.vue';
export default {
  components: { Header }
}
</script>

<template>
  <Header/>
  <RouterView />
</template>

<style scoped>

</style>
