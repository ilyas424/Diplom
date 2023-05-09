<template>
    <div class="container">
        <div class="py-5 text-center">
            <div class="row justify-content-center">
                <div class="col-md-5 col-lg-4">
        <form @submit.prevent="AuthUser">
            <h1 class="h3 mb-3 fw-normal">Пожалуйста, войдите</h1>

            <div v-if="error" class="alert alert-danger">
                {{error}}
            </div>

            <div class="form-floating">
                <input v-model="user.email"   class="form-control"  placeholder="name@example.com">
                <label >Адрес эл. почты</label>
            </div>
            <br>
            <div class="form-floating">
                <input v-model="user.hash" type="password" class="form-control"  placeholder="Password">
                <label >Пароль</label>
            </div>
            <div>
                <hr class="my-4">
            </div>

            <button  class="w-100 btn btn-outline-secondary" type="submit">Войти</button>
        </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script  itemscope>
import axios from "axios";
export default {
    name: "Authorisation-v",
    data() {
        return {
            user: { email: '',
                    hash: ''
                },
            error: ''
        }
    },
    methods:{
        async AuthUser() {
            try {
                const admin = await axios.get('http://127.0.0.1:8000/user/'+ this.user.email)
                const response = await axios.post('http://127.0.0.1:8000/login', this.user)
                localStorage.setItem('token', response.data.token)
                this.$store.dispatch('is_admin', admin.data.is_admin)
                this.$store.dispatch('user', this.user.email)
                this.$router.push('/home');
            }catch(e) {
                this.error = 'Неверный пароль и/или логин'
            }
        },
    }
}
</script>

<style scoped>

</style>