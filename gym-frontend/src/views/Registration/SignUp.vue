<template>
    <div class="signup">
        <h1>Account Sign-Up</h1>
        <br/>
        <form method="POST">
            <input type="text" class="form-control" name="username" placeholder="Username"/>
            <input type="password" class="form-control" name="email" placeholder=" Enter Email">
            <input type="password" class="form-control" name="password1" placeholder=" Enter Password">
            <input type="password" class="form-control" name="password1" placeholder=" Enter Password Again">
            <br>
            <button type="submit" class="btn btn-success btn-lg" id="submit">SIGN UP</button>
        </form>

        <br>
        
    <router-link :to="{ name: 'Login' }">User Already Registered? Log In</router-link>

    </div>
</template>

<script>

export default {
    name: "SignUp"
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