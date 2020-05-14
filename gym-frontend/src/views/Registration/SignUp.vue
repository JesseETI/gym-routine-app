<template>
    <div class="signup">
        <h1>Account Sign-Up</h1>
        <br/>
        <form method="POST" @submit.prevent="signUp">
            <input type="text" class="form-control" name="username" placeholder="Username" v-model="username" required/>
            <input type="password" class="form-control" name="password" placeholder=" Enter Password" v-model="password" required/>
            <br>
            <button type="submit" class="btn btn-success btn-lg" id="submit">SIGN UP</button>
        </form>

        <br>
        
    <router-link :to="{ name: 'Login' }">User Already Registered? Log In</router-link>

    </div>
</template>

<script>

import axios from 'axios'

export default {
    name: "SignUp",
    data() {
        return {
            username : null,
            password : null,
        }
    },
    methods : {
        signUp() {
            axios.post("https://jesseeti.pythonanywhere.com/api/users/", {
                username : this.username,
                password : this.password
            }).then(
                resp => {
                alert("User Created")
                this.$router.replace({name : 'Login'})
                }).catch(
                err => {
                    console.log(err)
                    alert("Account Signup Failed \n \
                    \nPlease try another username & password combination. ")
                })
        }
    }
}
</script>

<style scoped>

    .signup {
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