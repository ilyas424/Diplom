<template>
    <main style="padding:30px" >
    <div class="container" >
        <h1 class="fw-light"><strong>Задача</strong>: {{this.ticket.title}}</h1>
    </div>
        <br>
    <div class="container" style="background-color: #f6f6f6; border-radius: 10px">
        <div class="hstack gap-3" style="padding: 15px">
            <button type="button" class="btn btn-outline-secondary"
                @click="DialogAddComment = true;"
            >Прокомментировать</button>
            <button type="button" class="btn btn-outline-danger"
                    v-if=" this.$store.getters.is_admin  || this.$store.getters.user === this.ticket.reporter_email"
                @click="DialogDeleteTicket = true;"
            >Удалить</button>
        </div>
        <div class="d-flex" style="height: 15px;">
            <div class="vr" style="color:white"></div>
        </div>
        <div style="width: 100%; height: 20px; border-bottom: 1px solid black; text-align: left">
            <span style="font-size: 18px; background-color: #F3F5F6; padding: 0 10px">
            <strong> Детали </strong>
          </span>
            <div class="container">
                <br>
                <div class="row">
                    <div class="col-4">
                        <ul class="list-unstyled text-small">
                            <li class="mb-1"><strong>id</strong>: {{this.ticket.id}} </li>
                            <li class="mb-1"><strong>Приоритет</strong>: {{this.ticket.priority}}</li>
                            <li class="mb-1"><strong>Тип</strong>: {{this.ticket.ttype}} </li>
                        </ul>
                    </div>
                    <div class="col-4">
                        <ul class="list-unstyled text-small">
                            <li class="mb-1"><strong>Создал</strong> : {{this.ticket.reporter_email}}</li>
                            <li class="mb-1"><strong>Адресовано</strong>: {{this.ticket.assignee_email}}</li>
                            <li class="mb-1"><strong>Дата</strong>: {{this.ticket.creation_date}}</li>
                        </ul>
                    </div>
                    <div class="col-4" v-if="this.name_board">
                        <ul class="list-unstyled text-small">
                            <li class="mb-1"
                                @click="PushKanbanById"
                                style="cursor: pointer"
                            ><strong>Доска</strong>: {{this.name_board}} </li>
                            <li class="mb-1"><strong>Столбец</strong>: {{this.ticket.column_id}} </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <br>
        <div class="d-flex" style="height: 120px;">
            <div class="vr" style="color:white"></div>
        </div>
        <div style="width: 100%; height: 15px; border-bottom: 1px solid black; text-align: left">
          <span style="font-size: 18px; background-color: #F3F5F6; padding: 0 10px;">
            <strong> Описание </strong>
          </span>
            <div class="container">
                <div class="word">
                    {{this.ticket.description}}
                </div>
            </div>
        </div>
        <div class="d-flex" style="height: 80px; color:white">
            <div class="vr"></div>
        </div>
        <div style="margin-top: 10px">
            <div>
                <div style="width: 100%; height: 15px; border-bottom: 1px solid black; text-align: left">
                    <span style="font-size: 18px; background-color: #F3F5F6; padding: 0 10px;">
                        <strong> Комментарии </strong>
                    </span>
                </div>
                <div v-if="this.comments.length" class="container" style="margin-top: 10px;padding: 10px;margin-left: 149px">
                    <ul class="list-group list-group-flush"  >
                        <li class="list-group-item" v-for="comment in comments" :key="comment" style="padding: 15px;width: 750px;border-radius: 10px; display:inline-block">
                            <div class="row">
                                <div class="col-sm-4">
                                <strong>{{comment.author_email}}</strong>
                                {{comment.creation_date.slice(2,10)}} {{comment.creation_date.slice(11,16)}}
                                </div>
                                <div v-if='comment.is_edited' class="col-sm" style="color:#757575">
                                    Изменено
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-sm-10">
                                    {{ comment.text }}
                                </div>
                                <div class="col" style="margin-left: 40px" v-if="this.$store.getters.is_admin  || this.$store.getters.user === this.ticket.reporter_email">
                                    <v-icon
                                        v-if="this.$store.getters.is_admin || this.$store.getters.user === comment.author_email "
                                        @click="DialogEditComment = true; this.comment_id = comment.id; this.comment_text=comment.text"
                                        size="small"
                                        class="me-2">
                                        mdi-pencil
                                    </v-icon>
                                    <v-icon
                                        v-if="this.$store.getters.is_admin || this.$store.getters.user === comment.author_email "
                                        @click="DialogDeleteComment = true; this.comment_id = comment.id"
                                        size="small">
                                        mdi-delete
                                    </v-icon>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
                <div v-if="!comments.length"  style="text-align: center; font-size: 20px">
                    Комментариев нет
                </div>
            </div>
            </div>
    </div>

    </main>
    <ModalDelete
        v-bind:dialogwarning="this.DialogDeleteTicket">
        <v-btn
            color="green-darken-1"
            variant="text"
            @click="DialogDeleteTicket = false"
        >
            Нет
        </v-btn>
        <v-btn
            color="green-darken-1"
            variant="text"
            @click="DeleteComment"
        >
            Да
        </v-btn>
    </ModalDelete>
    <Modal
        v-bind:dialogwarning="this.DialogEditComment">
        <v-card-title class="text-h6" style="width: 400px; height: 140px">
            <strong>Добавление коментария</strong>
            <v-text-field
                v-model="this.comment_text"
                variant="outlined"
                label="комментарий"
                required
            ></v-text-field>
        </v-card-title>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                color="green-darken-1"
                variant="text"
                @click="DialogEditComment = false; this.comment_text = ''"
            >
                Закрыть
            </v-btn>
            <v-btn
                color="green-darken-1"
                variant="text"
                @click="CommentEditByTicket"
            >
                Изменить
            </v-btn>
        </v-card-actions>

    </Modal>
    <Modal
        v-bind:dialogwarning="this.DialogAddComment">
        <v-card-title class="text-h6" style="width: 400px; height: 140px">
            <strong>Добавление коментария</strong>
            <v-text-field
                v-model="this.comment_text"
                variant="outlined"
                label="комментарий"
                required
            ></v-text-field>
        </v-card-title>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                color="green-darken-1"
                variant="text"
                @click="DialogAddComment = false;"
            >
                Закрыть
            </v-btn>
            <v-btn
                color="green-darken-1"
                variant="text"
                @click="CommentAddByTicket"
            >
                Добавить
            </v-btn>
        </v-card-actions>

    </Modal>
    <ModalDelete
    v-bind:dialogwarning="this.DialogDeleteComment">
        <v-btn
            color="green-darken-1"
            variant="text"
            @click="DialogDeleteComment = false"
        >
            Нет
        </v-btn>
        <v-btn
            color="green-darken-1"
            variant="text"
            @click="DeleteCommentByTicket"
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
    name: "TicketById",
    components:{
        ModalDelete,
        Modal
    },
    data() {
        return{
            ticket: [],
            name_board: null,
            comments: [],
            DialogDeleteComment: false,
            DialogDeleteTicket: false,
            DialogAddComment: false,
            DialogEditComment: false,
            comment_id: null,
            comment_text: ''
            }
        },
    mounted() {
        this.ticket = this.$store.getters.ticket
        this.ticket.creation_date = this.ticket.creation_date.slice(0,10)

        axios.get('http://127.0.0.1:8000/ticket/'+this.ticket.id+'/comment/all')
            .then((response) => (this.comments = response.data))

        axios.get('http://127.0.0.1:8000/board/'+this.ticket.board_id).
        then(response => (
            this.name_board = response.data.board_name
        ))

    },
    methods:{
        async PushKanbanById(){
            this.$store.dispatch('kanban', this.ticket.board_id)
            this.$router.push('/kanban')
        },
        async DeleteCommentByTicket(){
            await axios.delete('http://127.0.0.1:8000/ticket/'+this.ticket.id+'/comment/'+this.comment_id)

            this.DialogDeleteComment = false

            axios.get('http://127.0.0.1:8000/ticket/'+this.ticket.id+'/comment/all')
                .then((response) => (this.comments = response.data))

            axios.get('http://127.0.0.1:8000/board/'+this.ticket.board_id).
            then(response => (
                this.name_board = response.data.board_name
            ))
        },
        async CommentAddByTicket(){
            await axios.post('http://127.0.0.1:8000/ticket/'+this.ticket.id+'/comment/all',{
                "text": this.comment_text,
                "author_email": this.$store.getters.user
            })

            this.DialogAddComment = false

            axios.get('http://127.0.0.1:8000/ticket/'+this.ticket.id+'/comment/all')
                .then((response) => (this.comments = response.data))

            axios.get('http://127.0.0.1:8000/board/'+this.ticket.board_id).
            then(response => (
                this.name_board = response.data.board_name
            ))

            this.comment_text = ''
        },
        async CommentEditByTicket(){
            await axios.patch('http://127.0.0.1:8000/ticket/'+this.ticket.id+'/comment/'+this.comment_id,{
                "text": this.comment_text,
                "author_email": this.$store.getters.user
            })

            this.DialogEditComment = false

            axios.get('http://127.0.0.1:8000/ticket/'+this.ticket.id+'/comment/all')
                .then((response) => (this.comments = response.data))

            axios.get('http://127.0.0.1:8000/board/'+this.ticket.board_id).
            then(response => (
                this.name_board = response.data.board_name
            ))

            this.comment_text = ''
        },
        async DeleteComment(){
            await axios.delete('http://127.0.0.1:8000/ticket/'+this.ticket.id)
            this.$router.push('/tickets')
        }
    },
    watch:{
        comments(){
             this.comments.sort((a,b) => a.creation_date.localeCompare(b.creation_date))
         }
    }
}
</script>

<style scoped>
.word {
    width: 880px;
    word-break: break-all;
}
.col-sm-10{
    width: 630px;
    word-break: break-all;
}


</style>