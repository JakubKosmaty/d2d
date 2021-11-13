import {createRouter, createWebHistory} from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/MainLayout.vue'),
    children: [
      {path: 'home', name: 'home', component: () => import('@/pages/Home.vue')},
      {path: 'login', name: 'login', component: () => import('@/pages/Login.vue')},
      {path: 'register', name: 'register', component: () => import('@/pages/Register.vue')},
      {path: 'menu', name: 'menu', component: () => import('@/pages/Menu.vue')},
      {path: 'profile', name: 'profile', component: () => import('@/pages/Profile.vue')},
      {path: 'checkout', name: 'checkout', component: () => import('@/pages/Checkout.vue')}
    ],
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
