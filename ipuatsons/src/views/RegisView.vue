<template>
    <div class="login-regis">
        <div class="menu">
            
            <form style="width: 35%;">
            <img src="@/img/logo.png" style="width:250px" alt="">
            <h1>Register</h1>
                <div style="text-align: left">
                    <label style="font-size: 15px">Email :</label>
                    <p>
                        <input id="email" type="email" @change="(e) => setUser({ ...user, email: e.target.value })"
                            style="color:black" />
                    </p>
                </div>

                <div style="text-align: left">
                    <label style="font-size: 15px">Password :</label>
                    <p>
                        <input id="password" type="password"
                            @change="(e) => setUser({ ...user, password: e.target.value })" style="color:black" />
                    </p>
                </div>
                <div style="text-align: left">
                    <label style="font-size: 15px">Password confirm :</label>
                    <p>
                        <input id="password_confirm" type="password" style="color:black" />
                    </p>
                </div>
                <div style="text-align: left">
                    <label style="font-size: 15px">Firstname :</label>
                    <p>
                        <input id="first_name" type="text"
                            @change="(e) => setUser({ ...user, first_name: e.target.value })" style="color:black" />
                    </p>
                </div>
                <div style="text-align: left">
                    <label style="font-size: 15px">Lastname :</label>
                    <p>
                        <input id="last_name" type="text"
                            @change="(e) => setUser({ ...user, last_name: e.target.value })" style="color:black" />
                    </p>
                </div>




                <div style="padding: 15px">
                    <input type="button" value="Regis" style="color:black" @click="register()" />
                    <input type="button" value="Clear" style="color:black" @click="clear()" />
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { useState } from '../composables/state';
import router from '@/router';
const axios = require('axios').default;
export default {
    name: "RegisView",
    data() {
        const [user, setUser] = useState({
            email: "",
            password: "",
            first_name: "",
            last_name: ""

        });
        return {
            users: [],
            user,
            setUser
        }
    },
    methods: {
        go_register() {
            router.push('register')
        },
        register() {
            if (document.getElementById("email").value.length == 0) {
                alert("Email is empty")
            } else if (document.getElementById("password").value.length == 0) {
                alert("Password is empty")
            } else if (document.getElementById("password_confirm").value.length == 0) {
                alert("Password confirm empty")
            } else if (document.getElementById("first_name").value.length == 0) {
                alert("Fisrtname is empty")
            } else if (document.getElementById("last_name").value.length == 0) {
                alert("Lastname is empty")
            } else {
                if (this.user.password == document.getElementById("password_confirm").value) {
                    axios.post('http://127.0.0.1:8000/api/register',
                        {
                            'user_id': Math.random().toString(36).slice(2),
                            'email': this.user.email,
                            'password': this.user.password,
                            'is_vip': 'false',
                            'first_name': this.user.first_name,
                            'last_name': this.user.last_name
                        }
                    ).then(async response => {
                        response.data
                        alert('Regis complete')
                        router.push('login')
                    }).catch(async error =>{
                        alert(error.response.data.email)
                        router.push('register')
                    })

                } else {
                    alert("Password is not macth with Password confirm")
                }
            }
        },
        clear() {
            document.getElementById("email").value=""
            document.getElementById("password").value=""
            document.getElementById("password_confirm").value=""
            document.getElementById("first_name").value=""
            document.getElementById("last_name").value=""

        }
    },
};
</script>

<style>

</style>