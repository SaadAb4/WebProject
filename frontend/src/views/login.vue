<template>
    <div>
        <form class="" method="post">
            <div class="container">
            <label for="email"><b>Email</b></label>
            <input type="email" placeholder="Enter Email" name="email" required>

            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required>
                
            <button type="submit">Login</button>
            <label>
                <input type="checkbox" checked="checked" name="remember"> Remember me
            </label>
            </div>

            <div class="container" >
            <button type="button" onclick="document.getElementById('login').style.display='none'" class="cancelbtn">Cancel</button>
            </div>
        </form>

        <!-- signup -->

        <form @submit.prevent="submitForm">
            <div class="container">
            <label for="email"><b>Email</b></label>
            <input type="email" placeholder="Enter Email" v-model="email" required>

            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" v-model="password" required>

            <label for="dob"><b>Date of Birth</b></label>
            <input type="date" placeholder="Enter Date of Birth" v-model="dob" required>
                
            <button type="submit">Sign Up</button>
            <label>
                <input type="checkbox" checked="checked" name="remember"> Remember me
            </label>
            </div>

            <div class="container" >
            <button type="button" onclick="document.getElementById('login').style.display='none'" class="cancelbtn">Cancel</button>
            </div>

            <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }} </p>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default ({
    name: 'Signup',
    data() {
        return {
            email: '',
            password: '',
            dob: '',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.email == '') {
                this.errors.push('email missing')
            }
            
            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                    password: this.password
                }

                axios
                    .post("/api/user/", formData)
                    .then(response => {
                        toast({
                            message: 'account created',
                            type: 'is-success',
                            dismissable: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/')
                    })
            }

        }
    }

    }
)
</script>
