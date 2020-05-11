<template>
    <div class="row d-flex justify-content-center mt-4">
                <div class="card col-4 m-1" v-bind:key="workout.id" v-for="workout in workouts">
                    <img src="#" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{{workout.title}}</h5>
                        <p class="card-text">{{workout.split}}</p>
                        <p class="card-text">Created by: {{workout.author_name}}</p>
                        <router-link :to="{ name: 'WorkoutDetails' , params: { workout: workout } }" tag="button" class="btn btn-info">Details</router-link>
                        &nbsp;
                        <button class="btn btn-danger" v-if="myworkouts" v-on:click="deleteWorkout(workout)">Delete</button>
                        &nbsp;
                        <router-link :to="{ name: 'WorkoutDetails' , params: { workout: workout } }" tag="button" class="btn btn-primary" v-if="myworkouts">Edit</router-link>

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
    mounted() {
        this.token = tokenService.getToken()
    },
    methods: {
        deleteWorkout(workout) {
            let decision = confirm("Would you like to delete this workout?")
            if (decision) {

                let axiosConfig = {
                    headers : {
                        'Authorization': 'Token '+ this.token
                    }
                }

                axios.delete(`http://localhost:8000/api/workouts/${workout.id}`, axiosConfig)
                .then(
                    res => {
                        console.log(res)
                        this.$delete(this.workouts, 10)
                    } ).catch(
                    err => console.log(err)
                )
            }
        }
    }
}
</script>