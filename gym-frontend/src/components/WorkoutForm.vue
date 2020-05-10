<template>
    <div class="container">
        <h1>{{formTitle}}</h1>

        <form @submit.prevent="createWorkout" v-if="!createNew">
            <fieldset disabled="disabled" v-if="!createNew">

                <div class="form-group">
                    <input type="text" class="form-control" name="title"  v-model="workoutTitle" placeholder="Title"/>
                </div>

                <div class="form-group" v-if="createNew">
                    <select name="type" class="form-control" v-model="split">
                        <option disabled selected value> Select a Split </option>
                        <option value="upperlower" selected>Upper Lower</option>
                        <option value="PPL">Push / Pull / Legs</option>
                        <option value="fullbody">Full Body</option>
                    </select>
                </div>

                <div class="form-group" v-if="!createNew">
                    <input type="text" class="form-control" name="split" v-model="split" placeholder="Split"/>
                </div>

                <div class="form-group" v-if="!createNew">
                    <input type="text" class="form-control" name="date" v-model="date" placeholder="Date"/>
                </div>

                <div class="form-group">
                    <input type="text" class="form-control" name="duration" v-model="duration" placeholder="Duration of Workout"/>
                </div>

                <div class="form-group">
                    <input type="text" class="form-control" name="author" v-model="author" placeholder="Author"/>
                </div>

                <div class="form-group" v-if="createNew">
                    <button type="submit" class="btn btn-success btn-lg" id="submit">Create</button>
                </div>
            </fieldset>

            <div class="row">
                 <div class="col-6 text-right">
                    <div class="form-group" v-if="!createNew">
                        <button type="submit" class="btn btn-danger btn-lg" id="submit">Delete</button>
                    </div>
                </div>

                <div class="col-6 text-left">
                    <div class="form-group" v-if="!createNew">
                        <button type="submit" class="btn btn-primary btn-lg" id="submit">Edit</button>
                    </div>
                </div>
            </div>

        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name : "WorkoutForm",
    data () {
        return {
        }
    },
    methods : {
    },
    props : [
        'formTitle',
        'workoutTitle',
        'split',
        'date',
        'duration',
        'author',
        'createNew'
    ],
}
</script>

<style scoped>

</style>