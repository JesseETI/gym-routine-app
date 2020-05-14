<template>
    <div class="allworkouts">
        <Header/>
    
        <div class="container-fluid">
            <h1>All Workouts</h1>
            <WorkoutCard 
                :workouts = workouts
                :myworkouts = "false"
            />

        </div>

    </div>
</template>

<script>
import axios from 'axios'
import {tokenService} from '../storage/service'
import Header from "@/components/Header.vue"
import WorkoutCard from "@/components/WorkoutCard.vue"

export default {
    name: "AllWorkouts",
    components: {
        Header,
        WorkoutCard
    },
    data() {
            return {
                workouts : [],
            }
    },
    created() {
            this.token = tokenService.getToken()
            this.getWorkouts()
    },
    methods: {
        getWorkouts() {

            let axiosConfig = {
                headers : {
                    'Authorization': 'Token '+ this.token
                }
            }
            
            axios.get("http://jesseeti.pythonanywhere.com/api/workouts/", axiosConfig)
            .then(
                res => this.workouts = res.data
            )
            .catch(
                err => console.log(err)
            )
            console.log(this.workouts)
            
        },

    },
}
</script>
 