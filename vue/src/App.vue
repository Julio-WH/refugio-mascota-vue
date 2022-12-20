<template>
  <div id="app">
<!--    <HelloWorld msg="Momento xD"/>-->
    {{list}}
    <MascotaCards
        v-for="(ele,i) in list"
        :key="i"
        :mascota="ele"
        :id="i+1"

    />
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { Component, Vue } from 'vue-property-decorator';
import MascotaCards from './components/MascotaCards.vue'

@Component({
  components: {
    MascotaCards,
  },
})
export default class AsideMenu extends Vue {
  petition=this.fetchListaMascotas()
  list=[]

  async fetchListaMascotas(){
    const response = await axios.get('/api/apiview/')
    const data = response.data;
    console.log(data)
    this.list=data
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
