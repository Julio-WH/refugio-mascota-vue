<template>
  <div>
    <div class="m-4">
      <h1 class="text-center mb-4">Listado de Mascotas con Vue.js</h1>
      <AlertComponent
    v-if="alert != null"
    :variant="alert.variant"
    :message="alert.message"
  />
   <router-link to="/mascota/" class="btn btn-info m-2">Agregar</router-link>
    </div>

    <div class="row m-4">
      <div class="d-flex justify-content-center" v-if="loading != false">
        <strong>Cargando la lista de mascotas</strong><br>
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
      <div v-for="(ele,i) in list"
        :key="i"
        :id="i+1"
      class="col-sm-3">
      <MascotaCards
        :mascota="ele"
      />
        <div class="text-center mb-4">
          <button  @click="submit_delete(ele.id, ele.nombre)" type="button"
                   class="btn btn-outline-danger m-2">Eliminar</button>
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
import AlertComponent from './Alert.vue';

@Component({
  components: {
    MascotaCards,
    AlertComponent,
  },
})
export default class AsideMenu extends Vue {
  list = []

  loading = true;

  mounted() {
    this.fetchListaMascotas();
  }

  async fetchListaMascotas() {
    const response = await axios.get('/api/apiview/');
    this.list = response.data;
    this.loading = false;
  }

  // eslint-disable-next-line camelcase,class-methods-use-this
  async submit_delete(id: number, nombre:string) {
    try {
      const response = await axios.delete(`/api/apiview/detalle/${id}`);
      const alert = {
        message: `Se eliminó correctamente ${nombre}`,
        variant: 'success',
      };
      await this.fetchListaMascotas();
      this.$store.dispatch('addAlert', alert, { root: true });
    } catch (e) {
      const alert = {
        message: 'No se pudo eliminar',
        variant: 'danger',
      };
      this.$store.dispatch('addAlert', alert, { root: true });
    }
  }

  get alert() {
    return this.$store.state.alert;
  }
}
</script>
