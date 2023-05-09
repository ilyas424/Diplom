<template>

    <div class="container">
        <main>
            <div class="py-5 text-center">
                <h2>Регистрация</h2>
                <p class="lead">Ниже расположена форма для регистарциия в Cedar.</p>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-7 col-lg-7">
                    <div v-if="Message1" class="alert alert-danger">
                        Некорректные данные
                    </div>
                    <h4 class="mb-3">Контактные данные</h4>
                    <form @submit.prevent="CreateUser" >
                        <div class="row g-3">
                            <div class="col-sm-6">
                                <label  class="form-label">Имя <span class="text-muted">*</span></label>
                                <input v-model="user.name" type="text" class="form-control" name="first_name" placeholder="Иван" />
                            </div>

                            <div class="col-sm-6">
                                <label class="form-label">Email <span class="text-muted">*</span></label>
                                <input v-model="user.email"  type="text" class="form-control" name="email" placeholder="user@example.com"  />

                            </div>

                            <div class="col-12">
                                <label  class="form-label">Пароль <span class="text-muted">*</span></label>
                                <div class="input-group has-validation">
                                    <input v-model="user.hash"  type="password" class="form-control" name="password"   />
                                </div>
                            </div>



                            <div class="col-12">
                                <div class="form-check">
                                    <input type="checkbox" class="form-check-input" id="same-address" required />
                                    <label class="form-check-label" for="same-address">Согласие на обработку персональных данных</label>
                                </div>
                                <div  v-if="Message2"  class="alert alert-danger">
                                    пользователь с таким логином уже существует
                                </div>
                            </div>


                        </div>


                        <hr class="my-4">
                        <button  class="w-100 btn btn-outline-secondary" type="submit">Зарегистрироваться</button>
                </form>
            </div>
            </div>
        </main>
    </div>

</template>

<script itemscope>
import axios from "axios";

export default {
    name: "Registration-v",
    data() {
        return {
            user: {
                name: '',
                email: '',
                hash: '',
            },
            Message1: false,
            Message2: false
        }
    },
    methods: {
        async CreateUser() {

            await axios.post('http://127.0.0.1:8000/register', this.user,
            ).then(() => {
                this.$router.push('/auth');
            }).catch((error) => {
                if (error.response.status === 422){
                    this.Message1 = true
                }else{
                    this.Message2 = true
                }

            });


        },

    }
}
</script>

<style scoped>

</style>