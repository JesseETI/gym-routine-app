<template>
    <div>
        <Header/>
    </div>
</template>

<script>
import Header from "@/components/Header.vue"
import axios from "axios"
import { tokenService } from '../storage/service'

export default {
    name: "MyWorkouts",
    components : {
        Header,
    },
    created() {
        this.token = tokenService.getToken()
        this.getMyWorkouts()
    },
    methods : {
        getMyWorkouts() {
            
            let axiosConfig = {
                headers : {
                    'Authorization': 'Token '+ this.token
                }
            }
            
            axios.get("http://localhost:8000/api/workouts/getmyworkouts", axiosConfig)
            .then(
                res => console.log(res.data)
            )
            .catch(
                err => console.log(err)
            )

        }
    }
}
</script>

<style scoped>

</style>