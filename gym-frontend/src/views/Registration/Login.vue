<template>
    <div class="login">
        <h1>Account Login</h1>
        <br>
        <form @submit.prevent="login">
            <input type="text" class="form-control" name="username"  v-model="username" placeholder="Username" required/>
            <input type="password" class="form-control" name="password" placeholder="Password" v-model="password" required>
            <br>
            <button type="submit" class="btn btn-success btn-lg" id="submit">LOGIN</button>
        </form>

        <br>
        
    <router-link :to="{ name: 'SignUp' }">Not Registered? Sign Up</router-link>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Login",
    data() {
        return {
            username : '',
            password : '',
            token : localStorage.getItem('user-token') || null,
        }
    },
    mounted() {
        if (this.token != null) {
            this.$router.replace({ name: "AllWorkouts" })
        }
        
    },
    methods : {
        login() {
            axios.post('http://localhost:8000/api/auth/', {
                username: this.username,
                password: this.password,
            })
            .then(resp => {
                this.token = resp.data.token
                localStorage.setItem('user-token', resp.data.token)
                this.$router.replace({ name: 'AllWorkouts' })
            })
            .catch(err => {
                localStorage.removeItem('user-token')
                alert("Incorrect Login Credentials")
            })
        },
    }
}
</script>

<style scoped>
    .login {
            width: 50%;
            height: 50%;
            background-color: white;
            border-radius: 5px;
            padding: 3rem;
            margin: auto;
            margin-top: 10%;
            border: 1px solid #E4E6E7;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.4);
        }
</style>