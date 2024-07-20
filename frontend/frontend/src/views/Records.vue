<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";

import Card from "@/components/Card.vue"
import AddRecordModal from "@/components/modals/AddRecordModal.vue";


onMounted(() => {
  if (localStorage.getItem("token") !== null) {
    const instance = axios.create({
      baseURL: 'http://127.0.0.1:8000',
      headers: {
        "Authorization": "Token " + localStorage.getItem("token")
      }
    })

    instance.get('/api/sugar/')
        .then((resp) => {
          data.value = resp.data
        })
        .catch((err) => console.error(err));
  }
})

function checkLogged() {
  return localStorage.getItem("token") !== null;
}


const data = ref()
</script>

<template>
  <div v-if="checkLogged()" class="ml-5 mt-5 mr-5">
    <AddRecordModal/>
  </div>
  <div class="flex flex-col flex-wrap sm:flex-row " v-if="checkLogged()">
    <Card v-for="datas in data" :carbohydrate="datas.carbohydrate" :cur_sugar="datas.cur_sugar" :cur_time="datas.cur_time" :id="datas.id"/>
  </div>
</template>

<style scoped>

</style>