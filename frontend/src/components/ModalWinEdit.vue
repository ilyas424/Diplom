<template>

    <v-row justify="center">
        <v-dialog
                v-model="this.dialog"
                persistent
                width="1024"
        >
            <template  v-slot:activator="{ props }">

            </template>
            <v-card>
                <v-card-title>
                    <span class="text-h5">Задача</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <div v-if="Message1" class="alert alert-danger">
                            Некорректные данные
                        </div>
                        <v-row>
                            <v-col
                                    cols="12"

                            >
                                <v-text-field
                                        v-model="ticket.description"
                                        label="Описание"
                                        itemprop="ticket.id"
                                        hint="example of helper text only on focus"
                                ></v-text-field>
                            </v-col>
                            <v-col
                                    cols="12"
                            >
                                <v-text-field
                                        v-model="ticket.title"
                                        label="Название*"
                                        required
                                ></v-text-field>
                            </v-col>
                            <v-col
                                    cols="12"
                                    sm="6"
                                    md="4"
                            >
                                <v-select
                                        v-model="ticket.assignee_email"
                                        :items="this.users"
                                        label="Получатель*"
                                        required
                                ></v-select>
                            </v-col>
                            <v-col
                                    cols="12"
                                    sm="6"
                                    md="4"
                            >
                                <v-select
                                        v-model="ticket.priority"
                                        :items="this.priorities"
                                        label="Приоритет*"
                                        required
                                ></v-select>
                            </v-col>
                            <v-col
                                    cols="12"
                                    sm="6"
                                    md="4"
                            >
                                <v-select
                                        v-model="ticket.ttype"
                                        :items="this.types"
                                        label="Тип*"
                                        required
                                ></v-select>
                            </v-col>
                            <v-col
                                    cols="12"
                                    sm="6"
                            >
                                <v-select
                                        v-model="columns"
                                        :items="boards"
                                        item-title="name"
                                        item-value="value"
                                        label="Доска"
                                        return-object

                                ></v-select>
                            </v-col>
                            <v-col
                                    cols="12"
                                    sm="6"
                            >
                                <v-select
                                        v-if="this.ticket"
                                        v-model="ticket.column_id"
                                        :items="columns.columns"
                                        item-title="columns"
                                        item-value="columns"
                                        label="Столбец"
                                        required
                                ></v-select>
                            </v-col>
                        </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <slot></slot>
                    <v-btn
                        color="blue-darken-1"
                        variant="text"
                        @click="UpdateTicket"
                    >
                        Сохранить
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-row>
</template>

<script>
import axios from "axios";

export default {
    props: {
        ticketedit: {},
        dialog: false,
    },
    data: () => ({
        users: [],
        priorities: [],
        types: [],
        boards:[],
        columns: [],
        ticket: {
            title: '',
            description: '',
            priority: '',
            ttype: '',
            reporter_email: '',
            assignee_email:'',
            board_id: '',
            column_id: ''
        },
        Message1: false,
    }),
    mounted() {
        this.ticket.title = this.ticketedit.title
        this.ticket.description = this.ticketedit.description
        this.ticket.priority = this.ticketedit.priority
        this.ticket.ttype = this.ticketedit.ttype
        this.ticket.assignee_email = this.ticketedit.assignee_email
        this.ticket.board_id = this.ticketedit.board_id
        this.ticket.reporter_email = this.$store.getters.user

        axios.get('http://127.0.0.1:8000/user/all').
        then(response => (response.data.forEach((value,index) => {
                this.users.push(value.email);
            })
        ))

        axios.get('http://127.0.0.1:8000/ticket/priorities').
        then((response) => (this.priorities = response.data))

        axios.get('http://127.0.0.1:8000/ticket/types').
        then((response) => (this.types = response.data))

        axios.get('http://127.0.0.1:8000/board/all').
        then(response => (response.data.forEach((value,index) => {
                this.boards.push({name: value.board_name, id: value.id, columns: value.columns})
            })
        ))
    },
    methods: {

        async UpdateTicket(){
            if (this.ticket.column_id === ''){
                this.ticket.board_id = null
                await axios.patch('http://127.0.0.1:8000/ticket/'+this.ticketedit.id, this.ticket
                ).then(() => {
                    location.reload();
                    this.dialog = false
                }).catch((error) => {
                    if (error.response.status === 422){
                        this.Message1 = true
                    }
                    if (error.response.status === 400){
                        this.Message1 = true
                    }
                });
            }else{
                await axios.patch('http://127.0.0.1:8000/ticket/'+this.ticketedit.id, this.ticket
                ).then(() => {
                    location.reload();
                    this.dialog = false
                }).catch((error) => {
                    if (error.response.status === 422){
                        this.Message1 = true
                    }
                    if (error.response.status === 400){
                        this.Message1 = true
                    }
                });
            }


        },
    },

    watch:{
        columns(){
            this.ticket.board_id = this.columns.id
            this.ticket.column_id = ''
        }
    },
}
</script>

<style scoped>

.icon{
    margin-left: 10px;
    margin-bottom: 10px;
    margin-top: 7px;
}


</style>