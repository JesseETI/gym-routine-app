<template>
    <div class="row d-flex justify-content-center mt-4">
                <div class="card col-4 m-1" v-bind:key="workout.id" v-for="workout in workouts">
                    <div class="card-body">
                        <h5 class="card-title">{{workout.title}}</h5>
                        <p class="card-text">{{workout.split}}</p>
                        <p class="card-text">Created by: {{workout.author_name}}</p>
                        <router-link :to="{ name: 'WorkoutDetails' , params: { workout: workout} }" tag="button" class="btn btn-info">Details</router-link>
                     </div>
                </div>
            </div>
</template>

<script>
import axios from 'axios'
import { tokenService } from '../storage/service'

export default {
    name: "WorkoutCard",
    props : ["workouts", "myworkouts"],
    beforeMount() {
        this.token = tokenService.getToken()
    },
}
</script>