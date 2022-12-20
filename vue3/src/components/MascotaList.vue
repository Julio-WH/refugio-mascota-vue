<template>
  <div>
<!--    {{list}}-->
    <h1 class="text-center mb-4">Listado de Mascotas con Vue.js</h1>
    <button class="btn btn-info m-2">Agregar</button>
    <div class="row">
      <MascotaCards
        v-for="(ele,i) in list"
        :key="i"
        :mascota="ele"
        :id="i+1"
      />
    </div>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import { Component, Vue } from 'vue-property-decorator';
import MascotaCards from './MascotaCards.vue';

@Component({
  components: {
    MascotaCards,
  },
})
export default class AsideMenu extends Vue {
  list = []

  mounted() {
    this.fetchListaMascotas();
  }

  async fetchListaMascotas() {
    const response = await axios.get('/api/apiview/');
    this.list = response.data;
  }
}
</script>
