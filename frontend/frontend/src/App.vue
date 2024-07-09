<script>
import Header from './components/Header.vue'
import { initFlowbite } from 'flowbite'
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
} else {
    document.documentElement.classList.remove('dark')
}
export default {
  mounted() {
    initFlowbite();
  },
  data(){
    return {}
  },
  components: { Header }
}
</script>

<template>
  <Header />
  <RouterView />
</template>

<style scoped>

</style>
