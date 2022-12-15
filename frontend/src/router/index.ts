import { createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import LogIn from '../views/login.vue'
import Profile from '../views/profilepage.vue'

const routes = [
  {
    path: '/', 
    name:"Home",
    component: Home
  },

  {
    path: '/profile',
    name:"Profile",
    component: Profile
  },
  {
    path: '/login', 
    name:"login",
    component: LogIn
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router