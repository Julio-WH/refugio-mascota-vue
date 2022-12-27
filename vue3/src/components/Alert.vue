<template>
  <div :class="classAlert" role="alert">
      {{message}}
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"
              @click="closeAlert"></button>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

@Component
export default class Alert extends Vue {
  @Prop() private variant!: string;

  @Prop() private message!: string;

  beforeDestroy() {
    this.$store.dispatch('removeAlert', { root: true });
  }

  get classAlert() {
    return `alert alert-${this.variant} alert-dismissible fade show`;
  }

  closeAlert() {
    this.$store.dispatch('removeAlert', { root: true });
  }
}
</script>

<style scoped>

</style>
