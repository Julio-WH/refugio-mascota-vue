import { RouteConfig } from 'vue-router';
import ListView from '@/components/MascotaList.vue';
import FormMascota from '@/components/MascotaForm.vue';
// import UpdateView from '@/app/views/UpdateView';
const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'list',
    component: ListView,
  },
  {
    path: '/mascota',
    name: 'mascota',
    component: FormMascota,
  },
  {
    path: '/mascota/:id',
    name: 'mascota_editar',
    component: FormMascota,
  },
  {
    path: '*',
    name: 'error404',
    component: ListView,
  },
  // {
  //     path: '/:id',
  //     name: 'retrieve',
  //     component: UpdateView,
  // },
];
export default routes;
