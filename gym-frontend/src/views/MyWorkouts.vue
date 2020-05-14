<template>
    <div class="myworkouts">
        <Header/>
    
        <div class="container-fluid">
            <h1>My Workouts</h1>
            <p>Logged in as: {{currUser}}</p>
            <router-link :to="{ name: 'CreateWorkout' }" tag="button" class="btn btn-success">
                Create Workout
            </router-link>
            <WorkoutCard 
                :workouts = workouts
                :myworkouts = "true"
            />

        </div>

    </div>
</template>

<script>
import Header from "@/components/Header.vue"
import axios from "axios"
import { tokenService } from '../storage/service'
import WorkoutCard from "@/components/WorkoutCard.vue"

export default {
    name: "MyWorkouts",
    components : {
        Header,
        WorkoutCard
    },
    data() {
        return {
            workouts : [],
            currUser : localStorage.getItem('username')
        }
    },
    created() {
        this.token = tokenService.getToken()
        this.getMyWorkouts()
    },
    methods : {
        getMyWorkouts() {
            
            let axiosConfig = {
                headers : {
                    'Authorization': 'Token '+ this.token
                }
            }
            
            axios.get("https://jesseeti.pythonanywhere.com/api/workouts/getmyworkouts", axiosConfig)
            .then(
                res => this.workouts = res.data
            )
            .catch(
                err => console.log(err)
            )

        }
    }
}
</script>