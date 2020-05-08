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
                
            }
    },
    methods: {
        
    },
    created() {
            this.getWorkouts()
    },
}
</script>
  