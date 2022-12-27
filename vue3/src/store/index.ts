import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    MascotaList: [],
    alert: null,
  },
  getters: {
  },
  mutations: {
    SET_ALERT(state, alert) {
      state.alert = alert;
    },
    UNSET_ALERT(state) {
      state.alert = null;
    },
  },
  actions: {
    addAlert({ commit }, alert) {
      commit('SET_ALERT', alert);
    },
    removeAlert({ commit }, alert) {
      commit('UNSET_ALERT', alert);
    },
  },
  modules: {
  },
});
