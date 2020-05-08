import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from "../views/Registration/Login.vue"
import Home from "../views/Home.vue"
import SignUp from "../views/Registration/SignUp.vue"

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    redirect: {
      name: "Login"
    }
  },
  {
    path: '/registration/login',
    name: 'Login',
    component: Login
  },
  {
    path: "/registration/signup",
    name: "SignUp",
    component: SignUp
  },
  {
    path: "/home",
    name: "Home",
    component: Home
  }
]

const router = new VueRouter({
  routes
})

export default router
