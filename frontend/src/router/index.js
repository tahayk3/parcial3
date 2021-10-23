import Vue from 'vue'
import VueRouter from 'vue-router'
import Ingredient from '@/components/ingrediente'
import Ingredient2 from '@/components/ingrediente2'
import Ingredient3 from '@/components/ingrediente3'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/ingredientes/listar',
    name: 'Ingredient',
    component: Ingredient
  },
  {
    path: '/ingredientes/ingresar',
    name: 'Ingresar',
    component: Ingredient2
  },
  {
    path: '/ingredientes/editar/:id/:name',
    name: 'Editar',
    component: Ingredient3
  },
]

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})
export default router