<template>
  <div class="container">
    <div class="row g-0 text-center">
  <h1 class="text-center">{{computedTitle}} Mascota</h1>
  <AlertComponent
    v-if="alert != null"
    :show="alert.show"
    :variant="alert.variant"
    :message="alert.message"
  />
  <div class="col-sm-12 col-md-8">
    <MascotaCards
    :mascota="computedMascota"
    :id="1"
  />
  </div>
  <form v-on:submit.prevent class="col-md-4">
    <div class="m-4">
      <p>
        <label>Nombre de la mascota:</label>
        <input v-model="nombre" class="form-control">
      </p>
      <p>
        <label for="">Sexo:</label>
        <select v-model="sexo" class="form-control">
          <option value="Macho">Macho</option>
          <option value="Hembra">Hembra</option>
        </select>
      </p>
      <p>
        <label>Edad aproximada:</label>
        <input v-model="edad" class="form-control" type="number">
      </p>
      <p>
        <label>Fecha de rescate:</label>
        <input v-model="fechaRescate" class="form-control" type="date">
      </p>
      <p>
        <label>Adoptante:</label>
        <select v-model="persona" class="form-control">
          <option v-for="{id, nombre } in listaPersonas"
                    :key="`${nombre}-${id}`"
                    :value="id">{{nombre}}</option>
        </select>
      </p>
      <p>
        <label>Vacunas:</label>
        <select v-model="vacunas" class="form-control" multiple >
          <option v-for="{id, nombre, status_select } in listaVacunas"
                    :key="`${nombre}-${id}`"
                    :value="id"
                    :selected="status_select"
          >{{nombre}}</option>
        </select>
      </p>
    </div>
  <div class="text-center">
    <button type="submit" @click="submit" :class="computedstyleBtn">{{computedBtnText}}</button>
    <router-link type="button" to="/" class="btn btn-danger m-2">
              Cancelar
    </router-link>
  </div>
  </form>
</div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import axios from 'axios';
import MascotaCards from './MascotaCards.vue';
import AlertComponent from './Alert.vue';

@Component({
  components: {
    MascotaCards,
    AlertComponent,
  },
})

export default class MascotaForm extends Vue {
  id = this.$route.params.id;

  listaVacunas= []

  listaPersonas= []

  nombre = '';

  sexo= '';

  edad=0;

  fechaRescate= '';

  persona= '';

  vacunas= [0];

  mounted() {
    this.fetchListPersonas();
    this.fetchListVacunas();
    if (this.id) {
      this.fechDetailMascota();
    }
  }

  // Para que se llene el formulario
  async fechDetailMascota() {
    try {
      const response = await axios.get(`/api/apiview/detalle/${this.id}`);
      const { data } = response;
      this.nombre = data.nombre;
      this.sexo = data.sexo;
      this.fechaRescate = data.fecha_rescate;
      this.edad = data.edad_aproximada;
      this.persona = data.persona.id;
      this.listaVacunas = this.vacunasSeleccionadas(data.vacuna);
    } catch (e) {
      console.error(e);
    }
  }

  // Para que se pinte en el Card
  personaSeleccionada() {
    const encontrado = this.listaPersonas.find((elem) => {
      const vacuna = JSON.parse(JSON.stringify(elem));
      return vacuna.id === this.persona;
    });
    return !encontrado ? {} : encontrado;
  }

  // eslint-disable-next-line camelcase,class-methods-use-this
  vacunasSeleccionadas(data_vacunas: Array<object>) {
    const list = this.listaVacunas;
    const select: any[] = [];
    // eslint-disable-next-line camelcase,array-callback-return
    const new_list = list.map((element) => {
      // eslint-disable-next-line camelcase
      const element_data = JSON.parse(JSON.stringify(element));
      const posicion = data_vacunas.findIndex((ele) => {
        // eslint-disable-next-line camelcase
        const element_api = JSON.parse(JSON.stringify(ele));
        return element_api.id === element_data.id;
      });
      if (posicion >= 0) {
        // eslint-disable-next-line camelcase
        select.push(element_data.id);
        // eslint-disable-next-line camelcase
        return { ...element_data, status_select: true };
      }
      // eslint-disable-next-line camelcase
      return element_data;
    });
    this.vacunas = select;
    return JSON.parse(JSON.stringify(new_list));
  }

  vacunasSeleccionadasCard() {
    // eslint-disable-next-line camelcase
    const vacunas_selected: any[] = [];
    // eslint-disable-next-line array-callback-return,camelcase
    const vacunas_lis = this.vacunas.map((element) => {
      // eslint-disable-next-line arrow-body-style
      const filtered = this.listaVacunas.find((ele) => {
        // eslint-disable-next-line camelcase
        const vacuna = JSON.parse(JSON.stringify(ele));
        return vacuna.id === element;
      });
      vacunas_selected.push(filtered);
    });
    // eslint-disable-next-line camelcase
    return vacunas_selected;
  }

  alert() {
    return this.$store.state.alert;
  }

  async fetchListVacunas() {
    const response = await axios.get('/api/apiview/vacunas');
    this.listaVacunas = response.data;
  }

  async fetchListPersonas() {
    try {
      const response = await axios.get('/api/apiview/personas');
      this.listaPersonas = response.data;
    } catch (e) {
      console.error(e);
    }
  }

  get computedTitle(): string {
    return !this.id ? 'Agregar' : 'Editar';
  }

  get computedBtnText(): string {
    return !this.id ? 'Agregar' : 'Guardar';
  }

  get computedstyleBtn(): string[] {
    return !this.id ? ['btn btn-info m-2'] : ['btn btn-success m-2'];
  }

  get computedMascota(): object {
    return {
      nombre: this.nombre,
      edad_aproximada: this.edad,
      fecha_rescate: this.fechaRescate,
      persona: this.personaSeleccionada(),
      vacuna: this.vacunasSeleccionadasCard(),
      sexo: this.sexo,
    };
  }

  submit() {
    return !this.id ? this.submitAdd() : this.submitEdit();
  }

  // eslint-disable-next-line class-methods-use-this
  async submitAdd() {
    try {
      const response = await axios.post('/api/apiview/', {
        nombre: this.nombre,
        sexo: this.sexo,
        edad_aproximada: String(this.edad),
        fecha_rescate: this.fechaRescate,
        persona: this.persona,
        vacuna: this.vacunas,
      });
      console.log(response.request);
    } catch (e) {
      console.error(e);
    }
  }

  // eslint-disable-next-line class-methods-use-this
  async submitEdit() {
    try {
      const response = await axios.put(`/api/apiview/detalle/${this.id}/`, {
        nombre: this.nombre,
        sexo: this.sexo,
        edad_aproximada: String(this.edad),
        fecha_rescate: this.fechaRescate,
        persona: this.persona,
        vacuna: this.vacunas,
      });
    } catch (e) {
      console.error(e);
    }
  }
}
</script>

<style scoped>

</style>
