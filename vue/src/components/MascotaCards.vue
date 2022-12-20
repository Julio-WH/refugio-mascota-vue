<template>
  <div>
    <h1>Hola mundo {{name}}</h1>
  </div>
</template>

<script >
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class MascotaCards extends Vue {
  // @Prop() private id!: string;
  // @Prop() private id!: string;
  // @Prop() private mascota!: string;
  name="Julio";
}

</script>

<style scoped>

</style>