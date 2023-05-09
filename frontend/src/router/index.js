import { createRouter, createWebHistory } from 'vue-router'
import MainPage from "@/pages/MainPage.vue";
import TicketsV from "@/pages/Tickets-v.vue";
import BoardsV from "@/pages/Boards-v.vue";
import AuthorisationV from "@/pages/Authorisation-v.vue";
import RegistrationV from "@/pages/Registration-v.vue";
import HomePage from "@/pages/HomePage.vue";
import myKanban from "@/pages/MyKanban.vue";
import TicketById from "@/pages/TicketById.vue";
import Users from "@/pages/Users.vue";



const routes = [
  {
    path: '/home',
    name: 'main',
    component: MainPage
  },
  {
    path: '/tickets',
    name: 'tickets',
    component: TicketsV
  },
  {
    path: '/boards',
    name: 'boards',
    component: BoardsV
  },
  {
    path: '/auth',
    name: 'auth',
    component: AuthorisationV
  },
  {
    path: '/registration',
    name: 'registration',
    component: RegistrationV
  },
  {
    path: '/',
    name: 'home',
    component:HomePage
  },
  {
    path: '/kanban',
    name: 'kanban',
    component: myKanban
  },
  {
    path: '/ticket',
    name: 'ticket',
    component: TicketById
  },
  {
    path: '/users',
    name: 'users',
    component: Users
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})



router.beforeEach((to, from, next) => {
  if ((to.name === 'home' || to.name === 'auth' || to.name === 'registration') && !localStorage.getItem('token')) {
    next()
  }else if (to.path === '/' && localStorage.getItem('token') ) {
    next({path: '/home'})
  }
  else if ((to.name !== 'home' || to.name !== 'auth' || to.name !== 'registration') && localStorage.getItem('token') ) {
    next()
  }
})




export default router
