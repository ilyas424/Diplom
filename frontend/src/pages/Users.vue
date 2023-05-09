<template>
    <div class="my-3 p-3 bg-body rounded shadow-sm">
        <div class="row">
            <div class="col-12">
                <h1 class="fw-light">Пользователи</h1>
            </div>
        </div>
        <br>
        <div>
            <input
                type="search" class="form-control" v-model="search" placeholder="Поиск пользователя по email">
        </div>
        <div v-for="user in searchHadler" :key="user">
        <div  class="d-flex text-muted pt-3">
            <hr>
            <div class="pb-3 mb-0 small lh-sm border-bottom w-100" style="background-color: whitesmoke; padding: 10px; border-radius: 4px">
                <div class="d-flex justify-content-between">
                    <div>
                        <p  class="fst-italic" style="font-size: 17px; color:black">
                            {{user.name}}
                            </p>
                        <p>Email: {{user.email}} </p>
                        <p
                            v-if="user.is_admin"
                        >Статус: Администратор</p>
                        <p
                            v-if="!user.is_admin"
                        >Статус: Пользователь</p>
                    </div>
                    <div>
                        <button
                            v-if="!user.is_admin && this.$store.getters.is_admin"
                            @click="DialogUserAdmin = true; user_email = user.email"
                            type="button" class="btn btn-outline-success" style="margin-right: 10px">Назначить админом</button>
                        <button type="button" class="btn btn-danger"
                                v-if="!user.is_admin && this.$store.getters.is_admin"
                                @click="DialogDeleteUser = true; user_email = user.email"
                        >Удалить</button>
                    </div>
                </div>
                <div>
                </div>
            </div>
        </div>
        </div>
    </div>
    <Modal
        v-bind:dialogwarning = this.DialogUserAdmin
    >
        <v-card-title class="text-h5">
            <strong>Подтверждения</strong>
        </v-card-title>
        <v-card-text>Вы действительно хотите назначить {{this.user_email}} администратором?</v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                color="green-darken-1"
                variant="text"
                @click="DialogUserAdmin = false"
            >
                Нет
            </v-btn>
            <v-btn
                color="green-darken-1"
                variant="text"
                @click="UpdateRole"
            >
                Да
            </v-btn>
        </v-card-actions>
    </Modal>
    <ModalDelete
        v-bind:dialogwarning = DialogDeleteUser
    >
        <v-btn
            color="green-darken-1"
            variant="text"
            @click="DialogDeleteUser = false"
        >
            Нет
        </v-btn>
        <v-btn
            color="green-darken-1"
            variant="text"
            @click="DeleteUser"
        >
            Да
        </v-btn>

    </ModalDelete>
</template>

<script>

import axios from "axios";
import ModalDelete from "@/components/ModalDelete.vue";
import Modal from "@/components/Modal.vue";

export default {
    name: "Users",
    components:{
        ModalDelete,
        Modal
    },
    data(){
        return{
            search:'',
            Users: [],
            DialogDeleteUser: false,
            DialogUserAdmin: false,
            user_email: null
        }
    },
    async mounted(){
        await axios.get('http://127.0.0.1:8000/user/all').
        then(response => (this.Users = response.data));
    },
    computed: {
        searchHadler() {
            return this.Users.filter(elem => {
                return elem.email.includes(this.search)
            })
        }
    },
    methods: {
        async DeleteUser(){
            await axios.delete('http://127.0.0.1:8000/user/'+this.user_email)

            this.DialogDeleteUser = false

            await axios.get('http://127.0.0.1:8000/user/all').
            then(response => (this.Users = response.data));
        },
        async UpdateRole(){
            await axios.post('http://127.0.0.1:8000/role',{
                "email": this.user_email,
                "is_admin": true
            })

            this.DialogUserAdmin = false

            await axios.get('http://127.0.0.1:8000/user/all').
            then(response => (this.Users = response.data));
        }
    }
}
</script>

<style scoped>

</style>