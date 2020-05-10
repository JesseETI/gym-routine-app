<template>
    <div class="createWorkout">
        <Header/>
        <WorkoutForm formTitle = "Create Workout"/>
    </div>
</template>

<script>
import axios from 'axios'
import WorkoutForm from "@/components/WorkoutForm.vue"
import Header from "@/components/Header.vue"

export default {
    name : "CreateWorkout",
    components: {
        WorkoutForm,
        Header
    },
    methods : {

    }
}
</script>