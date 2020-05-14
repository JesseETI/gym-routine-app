<template>
    <div class="">

      <!-- responsive navbar expand to vertically stack links on smaller screens -->
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">

          <!-- Title / Logo -->
          <a class="navbar-brand" href="#">Gym Routine App</a>

          <!--button that appears on smaller screens (called navbar toggler) -->
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleDiv" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
          </button>

          <!--toggler targets div collapse with targetted id-->
          <div class="collapse navbar-collapse" id="collapsibleDiv">
              <!-- navbar list-->
              <ul class="navbar-nav mr-auto mt-2 mt-lg-0">

                <li class="nav-item">
                  <router-link :to="{ name : 'AllWorkouts'}" class="nav-link">Home</router-link>
                </li>
                <li class="nav-item">
                  <router-link :to="{ name : 'MyWorkouts'}" class="nav-link">My Workouts</router-link>
                </li>
              </ul>
              
                <span class="navbar-brand">
                  <a class="text-warning" v-on:click="logout">Logout</a>
                </span>

        </div>

      </nav>
    <br>

    </div>
</template>

<script>
import axios from 'axios'
import { tokenService } from '../storage/service'

export default {
    name: "Header",
    created() {
      this.token = tokenService.getToken()
      this.getCurrentUser()
    },
    methods : {
      logout() {
        localStorage.removeItem('user-token')
        localStorage.removeItem('username')
        this.$router.replace({name : "Login"})
        localStorage.removeItem('username')
        localStorage.removeItem('editWorkout')
        localStorage.removeItem('workout')
      },
      getCurrentUser() {

        let axiosConfig = {
          headers : {
            'Authorization': 'Token '+ this.token
            }
        }

        axios.get("http://localhost:8000/api/workouts/getcurrentuser", axiosConfig)
          .then (
            res => {
              localStorage.setItem('username', res.data.username)
            })
          .catch (
            err => {
              localStorage.removeItem('username')
              console.log(err)
            })
      }
      
    },
}
</script>