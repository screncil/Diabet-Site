<template>
    <div>
      <button
        type="button"
        @click="openModal"
        class="rounded-md bg-gray-800/75 px-4 py-2 w-full sm:w-auto  text-sm font-medium text-white hover:bg-gray-800/50 focus:outline-none focus-visible:ring-2 focus-visible:ring-white/75"
      >
        Добавить запись
      </button>
    </div>
    <TransitionRoot appear :show="isOpen" as="template">
      <Dialog as="div" @close="closeModal" class="relative z-10">
        <TransitionChild
          as="template"
          enter="duration-300 ease-out"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="duration-200 ease-in"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-black/25" />
        </TransitionChild>

        <div class="fixed inset-0 overflow-y-auto">
          <div
            class="flex min-h-full items-center justify-center p-4 text-center"
          >
            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
            >
              <DialogPanel
                class="w-full max-w-md transform overflow-hidden rounded-2xl bg-gray-800 p-6 text-left align-middle shadow-xl transition-all"
              >
                <DialogTitle
                  as="h3"
                  class="text-lg font-medium leading-6 text-white"
                >
                  Добавление записи
                </DialogTitle>
                <div class="w-full flex flex-col gap-5 mt-5">
                  <div class="relative">
                    <label class="flex items-center mb-2 text-gray-400 text-xs font-medium">Углеводы <svg width="7" height="7" class="ml-1" viewBox="0 0 7 7" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M3.11222 6.04545L3.20668 3.94744L1.43679 5.08594L0.894886 4.14134L2.77415 3.18182L0.894886 2.2223L1.43679 1.2777L3.20668 2.41619L3.11222 0.318182H4.19105L4.09659 2.41619L5.86648 1.2777L6.40838 2.2223L4.52912 3.18182L6.40838 4.14134L5.86648 5.08594L4.09659 3.94744L4.19105 6.04545H3.11222Z" fill="#EF4444"></path></svg>
                    </label>
                    <input aria-valuemin="1" v-model="carbohydrates" type="number" id="default-search" class="block w-full px-4 py-2 text-sm font-normal shadow-xs text-white bg-transparent border border-blue-200 rounded-lg placeholder-gray-400 focus:outline-none leading-relaxed" placeholder="Количество углеводов на 100 грамм" required="">
                  </div>
                  <div class="relative">
                    <label class="flex items-center mb-2 text-gray-400 text-xs font-medium">Текущий сахар<svg width="7" height="7" class="ml-1" viewBox="0 0 7 7" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M3.11222 6.04545L3.20668 3.94744L1.43679 5.08594L0.894886 4.14134L2.77415 3.18182L0.894886 2.2223L1.43679 1.2777L3.20668 2.41619L3.11222 0.318182H4.19105L4.09659 2.41619L5.86648 1.2777L6.40838 2.2223L4.52912 3.18182L6.40838 4.14134L5.86648 5.08594L4.09659 3.94744L4.19105 6.04545H3.11222Z" fill="#EF4444"></path></svg>
                    </label>
                    <input v-model="cur_sugar" type="number" id="default-search" class="block w-full px-4 py-2 text-sm font-normal shadow-xs text-white bg-transparent focus: border border-blue-200 rounded-lg placeholder-gray-400 focus:outline-none leading-relaxed" placeholder="Текущий сахар (ммоль/л)" required="">
                  </div>
                </div>
                <div class="mt-8">
                  <button
                      @click="addRecord()"
                    type="button"
                    class="w-full inline-flex justify-center rounded-md border border-transparent bg-blue-400 px-4 py-2 text-sm font-medium text-blue-800 hover:bg-blue-900 hover:text-blue-400 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                  >
                    Добавить
                  </button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </template>

  <script setup>
  import { ref } from 'vue'
  import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle
  } from '@headlessui/vue'

  import axios from 'axios'

  import router from "@/router/index.js";

  const isOpen = ref(false)
  const carbohydrates = ref()
  const cur_sugar = ref()

  function addRecord() {
    if (localStorage.getItem("token") !== null) {
    const instance = axios.create({
      baseURL: 'http://127.0.0.1:8000',
      headers: {
        "Authorization": "Token " + localStorage.getItem("token")
      }
    })

    instance.post('/api/sugar/', {"cur_sugar": this.cur_sugar, "carbohydrate": this.carbohydrates})
        .then((resp) => {
          console.log(resp)
          if (resp.data.success) {
            isOpen.value = false
            router.go(window.location)
          }
        })
        .catch((err) => console.error(err));
  }
  }

  function closeModal() {
    isOpen.value = false
    auth.value = true
  }

  function openModal() {
    isOpen.value = true
  }

  </script>
