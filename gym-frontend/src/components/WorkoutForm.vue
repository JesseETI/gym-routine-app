<template>
    <div class="container">
        <h1>{{formTitle}}</h1>

        <form @submit.prevent="createWorkout">
            <fieldset>

                <div class="form-group">
                    <input type="text" class="form-control" name="title"  v-model="workoutTitle" placeholder="Title" required/>
                </div>

                <div class="form-group">
                    <input type="text" class="form-control" name="split" v-model="split" placeholder="Split"/>
                </div>

                <div class="form-group" v-if="!createNew">
                    <input type="text" class="form-control" name="date" placeholder="Date"/>
                </div>

                <div class="form-group">
                    <input type="text" class="form-control" name="duration" v-model="duration" placeholder="Duration of Workout"/>
                </div>

                <div class="form-group" v-if="!createNew">
                    <input type="text" class="form-control" name="author" placeholder="Author"/>
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
import { tokenService } from '../storage/service'

export default {
    name : "WorkoutForm",
    data () {
        return {
            workoutTitle : '',
            split : '',
            duration : '',
        }
    },
    created() {
        this.token = tokenService.getToken()
    }, 
    methods : {
        createWorkout() {

            let axiosConfig = {
                    headers : {
                        'Authorization': 'Token '+ this.token
                    }
                }
            
            axios.post("http://localhost:8000/api/workouts/", {
                title : this.workoutTitle,
                split : this.split,
                duration : this.duration,
            },
            axiosConfig).then(
                res => console.log(res.data)
            ).catch(
                err => console.log(err)
            )
        }
    },
    props : [
        'formTitle',
        'createNew',
    ],
}
</script>