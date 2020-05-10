<template>
    <div class="row d-flex justify-content-center">
            
                <div class="card col-3 m-2" v-bind:key="workout.id" v-for="workout in workouts">
                    <img src="#" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{{workout.title}}</h5>
                        <p class="card-text">{{workout.split}}</p>
                        <p class="card-text">Created by: {{workout.author_name}}</p>
                        <router-link :to="{ name: 'WorkoutDetails' , params: { workout: workout } }" tag="button" class="btn btn-success">Details</router-link>
                    </div>
                </div>

            </div>
</template>

<script>
export default {
    name: "WorkoutCard",
    props : ["workouts"]
}
</script>