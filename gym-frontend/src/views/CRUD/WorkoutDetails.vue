<template>
    <div class="workoutdetails">
        <Header />
        
        <div class="workoutinfo">
            <h1 class="text-success">{{workout.title}}</h1>
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
                    <div class="exercisebody" v-bind:key="exercise.id" v-for="exercise in exercises">
                        <br>
                        <h5 class="text-left">{{exercise.title}}</h5>
                        <h5 class="text-left">{{exercise.sets}} Sets of {{exercise.reps}} Reps</h5>
                        <img :src="exercise.image" height="400" width="500" v-if="exercise.image != null"/>
                        <button v-if="userCreated" v-on:click="deleteExercise(exercise)" class="btn btn-danger btn-small">Delete Exercise</button>
                        <br>
                    </div>
                    <br>
                    <button class="btn btn-info btn-sm" v-on:click="toggleExerciseForm" v-if="userCreated">Add Exercise</button>
                </div>
            </div>

            <div class="exerciseform" v-if="showExerciseForm">
                <h3>Create Exercise</h3>
                <form @submit.prevent="createExercise">
                    <input type="text" class="form-control" name="title"  placeholder="Title" v-model="exerciseTitle" required/>
                    <br>
                    <select v-model="sets" class="form-control">
                        <option selected disabled value="" required>Select # of sets</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                    <br>
                    <select v-model="reps" class="form-control" required>
                        <option selected disabled value="">Select # of reps</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                    <br>
                    <label for="file">Workout image: </label>
                    <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" accept="image/*"/>
                    <br/>
                    <br>
                    <button type="submit" class="btn btn-success btn-lg" id="submit">Create</button>
                </form>
            </div>

            <br>
            <div class="optionButtons text-right" v-if="userCreated">
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
            exercises : null,
            showExerciseForm : null,
            exerciseTitle : null,
            sets : "",
            reps : "",
            file : "",
            userCreated : null,
        }
    },
    components: {
        Header,
        WorkoutForm
    },
    created() {
        this.token = tokenService.getToken()
        this.loadedWorkout = this.$route.params.workout

        if (this.loadedWorkout != null) {
            this.workout = this.loadedWorkout
            localStorage.setItem('workout', JSON.stringify(this.workout))
            this.getRelatedExercises(this.workout)
        }
        else {
            this.workout = JSON.parse(localStorage.getItem('workout'))
            this.exercises = JSON.parse(localStorage.getItem('exercises'))
        }

        this.currentUser = localStorage.getItem('username')

        if (this.currentUser == this.workout.author_name) {
            this.userCreated = true;
        }
        else {
            this.userCreated = false;
        }

        this.showExerciseForm = false
    },
    methods: {
        getRelatedExercises(workout) {

            let axiosConfig = {
                    headers : {
                        'Authorization': 'Token '+ this.token
                    }
                }
                        
            axios.get(`http://localhost:8000/api/workouts/${this.workout.id}/getrelatedexercises`, axiosConfig)
            .then(
                res => {
                    this.exercises = res.data
                    localStorage.setItem('exercises', JSON.stringify(this.exercises))
                })
            .catch(
                err => console.log(err)
            )
        },
        toggleExerciseForm() {
            this.showExerciseForm = !this.showExerciseForm
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
        deleteExercise(exercise) {
            let decision = confirm("Would you like to delete this exercise?")
            if (decision) {

                let axiosConfig = {
                    headers : {
                        'Authorization': 'Token '+ this.token
                    }
                }

                axios.delete(`http://localhost:8000/api/exercises/${exercise.id}`, axiosConfig)
                .then(
                    res => {
                        this.exercises.pop(exercise)
                        localStorage.setItem('exercises', JSON.stringify(this.exercises))
                    } ).catch(
                    err => console.log(err)
                )
            }
        },
        handleFileUpload() {
            this.file = this.$refs.file.files[0]
        },
        createExercise() {

            const formData = new FormData();

            // Add images to form data
            formData.append('title', this.exerciseTitle)
            formData.append('sets', this.sets)
            formData.append('reps', this.reps)
            formData.append('image', this.file)
            formData.append('workout', this.workout.id)

            let axiosConfig = {
                    headers : {
                        'Authorization': 'Token ' + this.token,
                    }
                }
            
            axios({
                method: 'post',
                url: 'http://localhost:8000/api/exercises/',
                data: formData,
                headers: {'Content-Type': 'multipart/form-data',  'Authorization': 'Token ' + this.token}
            })
            .then(
                res => {
                    this.exercises.push(res.data)
                    localStorage.setItem('exercises', JSON.stringify(this.exercises))
                }
            )
            .catch(
                err => {
                console.log(err)
                alert("Exercise already exists")
        });
        }
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
  