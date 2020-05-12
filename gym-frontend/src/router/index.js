import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from "../views/Registration/Login.vue"
import SignUp from "../views/Registration/SignUp.vue"
import AllWorkouts from "../views/AllWorkouts.vue"
import MyWorkouts from "../views/MyWorkouts.vue"
import WorkoutDetails from "../views/CRUD/WorkoutDetails.vue"
import CreateWorkout from "../views/CRUD/CreateWorkout.vue"
import EditWorkout from "../views/CRUD/EditWorkout.vue"

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
    path: '/registration/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: "/home",
    name: "AllWorkouts",
    component: AllWorkouts
  },
  {
    path: "/myworkouts",
    name: "MyWorkouts",
    component: MyWorkouts
  },
  {
    path: "/details",
    name: "WorkoutDetails",
    component: WorkoutDetails
  },
  {
    path: '/create',
    name: 'CreateWorkout',
    component: CreateWorkout
  },

  {
    path: '/edit',
    name: 'EditWorkout',
    component: EditWorkout
  }
]

const router = new VueRouter({
  routes
})

export default router
