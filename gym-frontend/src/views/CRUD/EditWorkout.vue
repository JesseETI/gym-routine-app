<template>
    <div class="editworkout">
        <Header/>
        <WorkoutForm formTitle = "Edit Workout" :workout = workout />
    </div>
</template>

<script>
import axios from 'axios'
import WorkoutForm from "@/components/WorkoutForm.vue"
import Header from "@/components/Header.vue"

export default {
    name : "EditWorkout",
    data() {
        return {
            workout : null,
        }
    },
    components: {
        WorkoutForm,
        Header
    },
    created() {
        this.workout = this.$route.params.workout
    }
}
</script>