<template>
    <div class="workoutdetails">
        <Header />
        
        <div class="workoutinfo">
            <h1>{{workout.title}}</h1>
            <br>
            <div class="infobody text-left">

                <h5>Workout Type: {{workout.split}}</h5>
                <br>
                <h5>Date Created: {{workout.date}}</h5>
                <br>
                <h5>Session Duration: {{workout.duration}}</h5>
                <br>
                <h5>Created By: {{workout.author_name}}</h5>
                <br><br>    

                <div class="exercises">
                    <h2>Exercises</h2>
                    <br>
                    <h5 class="text-left">{{workout.exercises_list}}</h5>
                    <br>
                    <button class="btn btn-info btn-sm" v-on:click="toggleExerciseForm">Add Exercise</button>
                </div>
            </div>

            <div class="exerciseform" v-if="showExerciseForm">
                <h3>Create Exercise</h3>
                <form @submit.prevent="createExercise">
                    <input type="text" class="form-control" name="username"  placeholder="Username" required/>
                    <br>
                    <button type="submit" class="btn btn-success btn-lg" id="submit">Add</button>
                </form>
            </div>

            <br>
            <div class="optionButtons text-right">
                <router-link :to="{ name: 'EditWorkout' , params: { workout: workout } }" tag="button" class="btn btn-primary">Edit Workout</router-link>
                &nbsp;
                <button class="btn btn-danger btn-md" v-on:click="deleteWorkout(workout)">Delete Workout</button>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Header from "@/components/Header.vue"
import WorkoutForm from "@/components/WorkoutForm.vue"
import { tokenService } from '../../storage/service'

export default {
    name: "WorkoutDetails",
    data () {
        return {
            workout : null,
            showExerciseForm : null,
        }
    },
    components: {
        Header,
        WorkoutForm
    },
    created() {
        this.workout = this.$route.params.workout
        this.token = tokenService.getToken()
        this.showExerciseForm = false
    },
    methods: {
        toggleExerciseForm() {
            this.showExerciseForm = !this.showExerciseForm
        },
        getCurrentUser() {
            let axiosConfig = {
                    headers : {
                        'Authorization': 'Token '+ this.token
                    }
                }

            axios.get("http://localhost:8000/api/workouts/getcurrentuser", axiosConfig)
            .then(
                res => {
                    console.log(res.data)
                })
            .catch(
                err => console.log(err)
            )
        },
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
                        console.log(res.data)
                        this.$router.replace({ name: 'MyWorkouts' })
                    } ).catch(
                    err => console.log(err)
                )
            }
        },
    }
}
</script>

<style scoped>
    .workoutinfo {
        width: 80%;
        height: auto;
        background-color: white;
        border-radius: 5px;
        padding: 3rem;
        margin: auto;
        border: 1px solid #E4E6E7;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.4);
    }

</style>
  