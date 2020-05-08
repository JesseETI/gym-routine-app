<template>
    <div class="container">
        <h1>Workouts</h1>
        <p v-bind:key="workout.id" v-for="workout in workouts">
            {{workout.title}}
            <br>
        </p>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "ListWorkouts",
    components: {
    },
    data() {
            return {
                workouts : [],
            }
    },
    methods: {
        getWorkouts() {
            axios.get("http://localhost:8000/api/workouts/")
            .then(
                res => this.workouts = res.data
            )
            .catch(
                err => console.log(err)
            )
            console.log(this.workouts)
        },
    },
    created() {
            this.getWorkouts()
    },
}
</script>
 