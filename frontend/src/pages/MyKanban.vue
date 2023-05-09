<template>

    <div>
        <a>Доска: {{board_show.board_name}} <strong v-if="!board_show.is_open">Закрыта</strong></a>
        <select class="form-select" label="Kanban" v-model="now_kanban" >
            <template v-for="name in boards">
            <option  class="opt"  v-if="name.is_open" v-bind:value="name.id"  >
                {{name.board_name}}
            </option>
            </template>
        </select>
    </div>
    <div class="kanban">
        <hr class="my-2">
            <h1 v-if="!this.$store.getters.kanban" class="fw-light">Выберите доску</h1>
          <div class="row"  v-for="column in columns" :key="column">
              <div class="col" v-for="(k, col) in column" :key="col">
                  <div class="p-2 alert ">
                          <h3>{{col}}</h3>
                      <div class="list-group list-group-light"  >
                              <div class="list-group-item px-3 border-1 rounded-3 mb-2 " v-for="el in k" :key="el">
                                  <div class="description" @click="ShowTicket(el)">
                                {{el.title}}
                                  </div>
                                  <br>
                                  <div >
                                      Создал: {{el.reporter_email}}
                                  </div>
                                  <div>
                                      <hr>
                                      <v-icon
                                             v-if="board_show.is_open && (this.$store.getters.is_admin  || this.$store.getters.user === el.reporter_email)"
                                              @click="dialogVisibel(el)"
                                              size="small"
                                              class="me-2">
                                          mdi-pencil
                                      </v-icon>
                                      <v-icon
                                          v-if="board_show.is_open && (this.$store.getters.is_admin  || this.$store.getters.user === el.reporter_email)"
                                              @click="dialogVisibeldelete(el.id)"
                                              size="small">
                                          mdi-delete
                                      </v-icon>
                                      <svg-icon type="mdi"
                                                v-if="board_show.is_open && (this.$store.getters.is_admin  || this.$store.getters.user === el.reporter_email)"
                                                @click="DialogColumn(el)"
                                                :path="path"
                                                class="swap-icon"
                                       ></svg-icon>
                                  </div>
                              </div>
                      </div>
                      <v-icon
                          v-if="board_show.is_open"
                          @click="dialogVisibechoise(col)"
                          icon="mdi-plus"

                      ></v-icon>
                      </div>

                  </div>
              </div>
        <ModalforKanban
            v-if="this.dialogcolumn"
            v-bind:dialogchoise="dialogcolumn"
            >
            <v-card>
                <v-card-title>Выберите столбец</v-card-title>
                <v-divider></v-divider>
                <v-card-text style="height: 155px; width: 400px">
                    <div v-if="Message" class="alert alert-danger">
                        Обязательное поле пустое
                    </div>
                    <v-col
                        cols="12"
                    >
                        <v-select
                            v-model="column_id"
                            :items="swap[0].columns"
                            item-title="columns"
                            item-value="columns"

                        ></v-select>
                    </v-col>
                </v-card-text>
                <v-divider></v-divider>

                <v-card-actions>
                    <v-btn
                        variant="text"
                        @click="dialogcolumn = false; Message = false; column_id = null"
                    >
                        Закрыть
                    </v-btn>
                    <v-btn
                        variant="text"
                        @click="TicketUpdateKanban"
                    >
                        Сохранить
                    </v-btn>
                </v-card-actions>
            </v-card>
        </ModalforKanban>
        <ModalWinEdit
                v-if="dialog"
                v-bind:dialog="dialog"
                v-bind:ticketedit="ticket"
        >
            <v-btn
                    color="blue-darken-1"
                    variant="text"
                    @click="dialog = false"
            >
                Close
            </v-btn>


        </ModalWinEdit>
        <modalDelete
                v-if="dialogdelete"
                v-bind:dialogwarning="dialogdelete"
        >
            <v-btn
                    color="green-darken-1"
                    variant="text"
                    @click="dialogdelete = false"
            >
                Нет
            </v-btn>
            <v-btn
                    color="green-darken-1"
                    variant="text"
                    @click="DeleteTicket(this.id)"
            >
                Да
            </v-btn>

        </modalDelete>
        <ModalforKanban
            v-if="dialogchois"
            v-bind:dialogchoise="dialogchois"
        >
            <v-card>
                <v-card-title>Select ticket</v-card-title>
                <v-divider></v-divider>
                <v-card-text style="height: 155px; width: 400px">
                    <div v-if="Message" class="alert alert-danger">
                        Обязательное поле пустое
                    </div>
                    <v-col
                        cols="12"
                    >
                        <v-select
                            v-model="ticketadd"
                            :items="tickets_all"
                            return-object

                        ></v-select>
                    </v-col>
                </v-card-text>
                <v-divider></v-divider>

                <v-card-actions>
                    <v-btn
                        variant="text"
                        @click="dialogchois = false; Message = false; ticketadd = null"
                    >
                        Закрыть
                    </v-btn>
                    <v-btn
                        variant="text"
                        @click="TicketAddKanban"
                    >
                        Сохранить
                    </v-btn>
                </v-card-actions>
            </v-card>
        </ModalforKanban>
    </div>

</template>

<script>
import axios from "axios";
import ModalWinEdit from "@/components/ModalWinEdit.vue";
import modalDelete from "@/components/ModalDelete.vue";
import ModalforKanban from "@/components/ModalforKanban.vue";
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiSwapHorizontal } from '@mdi/js'




export default {
    components:{
        ModalWinEdit,
        modalDelete,
        ModalforKanban,
        SvgIcon
    },
    name: "MyKanban",

    data(){
        return{
            id: null,
            columnchois: null,
            ticketadd: null,
            boards_id: null,
            tickets_all:[],
            dialog: false,
            ticket: {},
            board_show: {},
            columns: [],
            column_id: null,
            boards: [],
            swap: [],
            now_kanban: '',
            dialogdelete: false,
            dialogchois: false,
            dialogcolumn: false,
            Message: false,
            path: mdiSwapHorizontal,
        }
    },
    async mounted() {
        await axios.get('http://127.0.0.1:8000/board/all').
        then(response => (
            this.boards = response.data
        ))
        await axios.get('http://127.0.0.1:8000/board/'+this.$store.getters.kanban).
        then(response => (
            this.columns = response.data.columns,
                this.board_show = response.data
        ))
        await axios.get('http://127.0.0.1:8000/ticket/backlog').
        then(response => (
            this.tickets_all = response.data
        ))

        await axios.get('http://127.0.0.1:8000/board/all').
        then(response => (response.data.forEach((value,index) => {
            if (value.id === this.$store.getters.kanban) {
                this.swap.push({columns: value.columns})
            }
            })
        ))

    },
    methods:{
        async DeleteTicket(value){
            try{
                await axios.delete('http://127.0.0.1:8000/ticket/'+value).
                then(() => {
                    this.dialogdelete = false
                })} catch(e){
                    this.Message = true
            }


        },
        ShowTicket(value){
            this.$store.dispatch('ticket', value)
            this.$router.push('/ticket')
        },
        dialogVisibel(value){
            this.dialog = true
            this.ticket= value
        },
        dialogVisibeldelete(value){
            this.dialogdelete= true
            this.id = value
        },
        dialogVisibechoise(value){
            this.dialogchois= true
            this.boards_id = value
        },
        async TicketAddKanban(){
            try{
                await axios.patch('http://127.0.0.1:8000/ticket/'+this.ticketadd.id, this.ticketadd
            ).then(() => {
                this.dialogchois = false
            })} catch(e){
                this.Message = true
            }
            axios.get('http://127.0.0.1:8000/ticket/backlog').
            then(response => (
                this.tickets_all = response.data
            ))
            this.ticketadd = null
        },
        DialogColumn(value){
            this.dialogcolumn= true
            this.boards_id = value

            this.column_id = null


        },
        async TicketUpdateKanban(){
            try{
                await axios.patch('http://127.0.0.1:8000/ticket/'+this.boards_id.id, this.boards_id
                ).then(() => {
                    this.dialogcolumn = false
                })} catch(e){
                this.Message = true
            }
        },

    },
    watch: {
        swap() {
            axios.get('http://127.0.0.1:8000/board/all').
            then(response => (response.data.forEach((value,index) => {
                    if (value.id === this.$store.getters.kanban) {
                        this.swap.push({columns: value.columns})
                    }
                })
            ))
        },
        now_kanban() {
            this.$store.dispatch('kanban', this.now_kanban)
        },
        '$store.getters.kanban': function() {
            axios.get('http://127.0.0.1:8000/board/'+this.$store.getters.kanban).
            then(response => (
                this.columns = response.data.columns,
                    this.board_show = response.data
            ))
            this.swap = []
        },
        ticketadd(){
            this.ticketadd.board_id = this.board_show.id
            this.ticketadd.column_id = this.boards_id
        },
        column_id(){
            this.boards_id.column_id = this.column_id
        },
        dialogcolumn() {
            axios.get('http://127.0.0.1:8000/board/' + this.$store.getters.kanban).then(response => (
                this.columns = response.data.columns,
                    this.board_show = response.data
            ))
        },
        dialogchois(){
            axios.get('http://127.0.0.1:8000/board/'+this.$store.getters.kanban).
            then(response => (
                this.columns = response.data.columns,
                    this.board_show = response.data
            ))
        },
        dialogdelete(){
            axios.get('http://127.0.0.1:8000/board/'+this.$store.getters.kanban).
            then(response => (
                this.columns = response.data.columns,
                    this.board_show = response.data
            ))
        },
        }
}
</script>

<style scoped>
.form-select{
    width: 130px;
    margin-left: 10px;
    margin-top: 10px;
}

a{
  padding-left: 13px;
}
.fw-light{
    margin-left: 475px;
}
svg{
    cursor: pointer;
}
.list-group{
    border-radius: 20px;
}

.list-group-item{
    border-radius: 40px;
    box-shadow: 0px 25px 22px -2px rgba(90, 94, 97, 0.2);

}
.kanban{
    padding: 5px;
}
.description{
    cursor: pointer;
    background-color: whitesmoke;
    border-radius: 6px;
    padding: 10px;
}
.swap-icon{
    cursor: pointer;
    margin-left: 4px;
}
.alert{
    background-color: #e7e7e7;
}


</style>