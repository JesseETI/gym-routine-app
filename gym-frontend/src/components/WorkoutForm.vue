<template>
    <div class="container">
        <h1>{{formTitle}}</h1>

        <form @submit.prevent="WorkoutFormHandler(workout)">
                <div class="form-group">
                    <input type="text" class="form-control" name="title"  v-model="workoutTitle" placeholder="Title" required/>
                </div>
                <div class="form-group">
                    <input type="text" class="form-control" name="split" v-model="split" placeholder="Split" required/>
                </div>

                <div class="form-group" v-if="!createNew">
                    <input type="text" class="form-control" name="date" :placeholder="workout.date" disabled/>
                </div>

                <div class="form-group">
                    <input type="text" class="form-control" name="duration" v-model="duration" placeholder="Duration of Workout" required/>
                </div>

                <div class="form-group" v-if="!createNew">
                    <input type="text" class="form-control" name="author" :placeholder="workout.author_name" disabled/>
                </div>

                <div class="form-group" v-if="createNew">
                    <button type="submit" class="btn btn-success btn-lg" id="submit">Create</button>
                </div>

                <div class="form-group" v-if="!createNew">
                    <button type="submit" class="btn btn-primary btn-lg" id="submit">Edit</button>
                </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
import { tokenService } from '../storage/service'

export default {
    name : "WorkoutForm",
    data() {
        return {
            workoutTitle : null || this.workout.title,
            split : null || this.workout.split,
            duration : null || this.workout.duration,
        }
    },
    created() {
        this.token = tokenService.getToken()
    }, 
    methods : {
        WorkoutFormHandler(workout) {

            if (this.createNew) {
                this.createWorkout()
            }
            else {
                this.editWorkout(workout)
            }
        },
        createWorkout() {

            let axiosConfig = {
                    headers : {
                        'Authorization': 'Token '+ this.token
                    }
                }
            
            axios.post("http://localhost:8000/api/workouts/", {
                title : this.workoutTitle,
                split : this.split,
                duration : this.duration,
            },
            axiosConfig).then(
                res => {
                    this.$router.replace({ name: 'MyWorkouts'})
                }
            ).catch(
                err => {console.log(err)
                })
        },
        editWorkout(workout) {

            let axiosConfig = {
                    headers : {
                        'Authorization': 'Token '+ this.token
                    }
                }

            axios.put(`http://localhost:8000/api/workouts/${workout.id}/`, {
                title : this.workoutTitle,
                split : this.split,
                duration : this.duration,
            },
            axiosConfig).then(
                res => {
                    this.$router.replace({ name: 'WorkoutDetails', params: { workout: res.data }})
                }
            ).catch(
                err => console.log(err)
            )
        }
    },
    props : {
        'formTitle' : {
            default : ""
        },
        'createNew': {
        },
        'workout' : {
            type: Object,
            default () {
                return {
                    title : "",
                    split : "",
                    duration : ""
                }
            }
        }
    },
}
</script>