<template>
    <div class="card">
      <img
        class="card-img-top"
        alt="imagen de gato"
        src="https://cdn2.thecatapi.com/images/7ce.jpg">
      <div class="card-body">
        <h5 class="card-title text-center">{{ mascota.nombre }}</h5>
        <p class="card-text"><strong>Sexo:</strong>{{mascota.sexo}}</p>
        <p class="card-text"><strong>Edad Aproximada:</strong>{{mascota.edad_aproximada}}</p>
        <p class="card-text"><strong>Fecha de rescate:</strong>{{mascota.fecha_rescate}}</p>
        <hr>
        <p>Detalle del Dueño</p>
        <p class="card-text"><strong>Nombre:</strong>{{mascota.persona.nombre}}
          {{mascota.persona.apellido}}</p>
        <p class="card-text"><strong>Edad:</strong>{{mascota.persona.edad}}</p>
        <p class="card-text"><strong>Telefono:</strong>{{mascota.persona.telefono}}</p>
        <p class="card-text"><strong>Email:</strong>{{mascota.persona.email}}</p>
        <p class="card-text"><strong>Domicilio:</strong>{{mascota.persona.domicilio}}</p>
        <hr>
        <div v-if="!!mascota.vacuna.length">
          Vacunas:
          <span v-for="vacuna in mascota.vacuna"
          :key="vacuna.nombre + '-' + vacuna.id"
          >{{vacuna.nombre}},
          </span>
        </div>
        <div v-else>
          <span>No tiene ninguna vacuna</span>
        </div>
      </div>
    </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class MascotaCards extends Vue {
  @Prop() private id!: string;

  @Prop() private mascota!: Array<object>;
}

</script>
