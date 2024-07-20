<script>

import axios from "axios";
import router from "@/router/index.js";

export default {
  props: {
    cur_time: String,
    carbohydrate: Float32Array,
    cur_sugar: Float32Array,
    id: Number
  },
  methods: {
    convertTime(time) {
      const dayNames = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
      const dateObj = new Date(time)
      return dayNames[dateObj.getUTCDay()] + ", " + dateObj.getHours() + ":" + dateObj.getMinutes() + " " + dateObj.getFullYear() + '-' + (dateObj.getMonth() + 1) + '-' + dateObj.getDate()
    },

    sugarTextColor(sugar) {
      if (sugar < 9) {
        return "text-green-500/75"
      } else if (sugar < 15) {
        return "text-orange-500/75"
      } else {
        return "text-red-500/75"
      }
    },

    deleteRecord() {
      if (localStorage.getItem("token") !== null) {
        axios.delete('http://127.0.0.1:8000/api/sugar/', {
          headers: {
            Authorization: "Token " + localStorage.getItem("token")
          },
          data: {
            id: this.id
          }
        })
            .then((resp) => {
              if (resp.data.success) {
                router.go(window.location)
              }
            })
            .catch((err) => console.error(err))
      }
    }
  }
}

</script>

<template>
  <div class="relative flex flex-row mt-6 ml-5 text-white bg-gray-800 shadow-md rounded-xl mr-5 sm:w-1/4">
    <div class="p-6">
      <div class="flex flex-row justify-items-center">
        <h5 class="block mb-2 font-sans text-xl antialiased font-semibold leading-snug tracking-normal text-blue-gray-900">
        {{ convertTime(cur_time) }}
      </h5>
      <svg @click="deleteRecord()" class="fill-current hover:rounded hover:bg-white/15 ml-10" height="25px" width="25px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 60.167 60.167" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M54.5,11.667H39.88V3.91c0-2.156-1.754-3.91-3.91-3.91H24.196c-2.156,0-3.91,1.754-3.91,3.91v7.756H5.667 c-0.552,0-1,0.448-1,1s0.448,1,1,1h2.042v40.5c0,3.309,2.691,6,6,6h32.75c3.309,0,6-2.691,6-6v-40.5H54.5c0.552,0,1-0.448,1-1 S55.052,11.667,54.5,11.667z M22.286,3.91c0-1.053,0.857-1.91,1.91-1.91H35.97c1.053,0,1.91,0.857,1.91,1.91v7.756H22.286V3.91z M50.458,54.167c0,2.206-1.794,4-4,4h-32.75c-2.206,0-4-1.794-4-4v-40.5h40.75V54.167z M38.255,46.153V22.847c0-0.552,0.448-1,1-1 s1,0.448,1,1v23.306c0,0.552-0.448,1-1,1S38.255,46.706,38.255,46.153z M29.083,46.153V22.847c0-0.552,0.448-1,1-1s1,0.448,1,1 v23.306c0,0.552-0.448,1-1,1S29.083,46.706,29.083,46.153z M19.911,46.153V22.847c0-0.552,0.448-1,1-1s1,0.448,1,1v23.306 c0,0.552-0.448,1-1,1S19.911,46.706,19.911,46.153z"></path></g></svg>
      </div>
      <div class="text-gray-500">
        Углеводы={{ carbohydrate }} / 100г
      </div>
      <div class="flex flex-row text-gray-500">
        <p>Сахар</p>
        <p>=</p>
        <p class="tracking-tight" :class="sugarTextColor(cur_sugar)">{{ cur_sugar }} ммоль/л</p>
      </div>
      <hr class="h-px w-full my-5 bg-gray-200 border-0 dark:bg-gray-700">
      <div class="text-gray-400">
        Нужно уколоть ≈ {{ Math.round(carbohydrate / 10)  }} ед.
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>