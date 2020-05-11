<template>
    <div class="workoutdetails">
        <Header />
        
        <div class="workoutinfo">
            <h1 class="text-primary">{{workout.title}}</h1>
            <div class="infobody text-left">
                <h5>Workout Type: {{workout.split}}</h5>
                <br>
                <h5>Date Created: {{workout.date}}</h5>
                <br>
                <h5>Session Duration: {{workout.duration}}</h5>
                <br>
                <h5>Created By: {{workout.author_name}}</h5>
                <br>
                <div class="exercises">
                    <h2 class="text-center text-success">Exercises</h2>
                    <h5>{{workout.exercises_list}}</h5>
                </div>
            </div>
        </div>

        {{workout}}
    </div>
</template>

<script>
import axios from 'axios'
import Header from "@/components/Header.vue"
import WorkoutForm from "@/components/WorkoutForm.vue"

export default {
    name: "WorkoutDetails",
    data () {
        return {
            workout : null,
        }
    },
    components: {
        Header,
        WorkoutForm
    },
    created() {
        this.workout = this.$route.params.workout;
    },
    data() {
            return {

            }
    },
    methods: {
        
    },
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
  