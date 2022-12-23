<template>
  <div>
    <div class="m-4">
      <h1 class="text-center mb-4">Listado de Mascotas con Vue.js</h1>
   <router-link to="/mascota/" class="btn btn-info m-2">Agregar</router-link>
    </div>

    <div class="row m-4">
      <div v-for="(ele,i) in list"
        :key="i"
        :id="i+1"
      class="col-sm-3">
      <MascotaCards
        :mascota="ele"
      />
        <div class="text-center mb-4">
          <button  @click="submit_delete(ele.id)" type="button" class="btn btn-outline-danger m-2">
            Eliminar
          </button>
          <router-link type="button" :to="{name:'mascota_editar', params:{id:ele.id}}"
                       class="btn btn-outline-primary m-2">
            Editar
          </router-link>
        </div>
    </div>
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

  // eslint-disable-next-line camelcase,class-methods-use-this
  async submit_delete(id: number) {
    try {
      const response = await axios.delete(`/api/apiview/detalle/${id}`);
      // const { data } = response;
      await this.fetchListaMascotas();
    } catch (e) {
      console.error(e);
    }
  }
}
</script>
