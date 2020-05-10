<template>
    <div class="workoutdetails">
        <Header />
        <WorkoutForm 
            formTitle = "Workout Details"
            :workoutTitle = workout.title
            :split = workout.split
            :date = workout.date
            :duration = workout.duration
            :author = workout.author_name
        />
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
  