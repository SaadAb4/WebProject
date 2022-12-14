import { createRouter, createWebHistory} from 'vue-router'
//import Home from '../views/Home.vue'
//import About from '../views/About.vue'
const Home = { template: '<div>Home</div>' }
const About = { template: '<div>About</div>' }

const routes = [
  {
    path: '/', 
    component: Home
  },

  {
    path: '/about',
    component: About
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router