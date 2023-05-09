<template>
  <div class="table-pad">
      <h1 class="fw-light">Все задачи</h1>
      <div class="modal-v">
          <ModalWin
          ></ModalWin>
      </div>
      <table class="table">
          <thead>
          <tr>
              <th scope="col">id</th>
              <th scope="col">Название
                  <svg @click="sortByTitle" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-filter" viewBox="0 0 16 16">
                      <path d="M6 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z"/>
                  </svg></th>
              <th scope="col" @click="sortBydescription">Тип
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-filter" viewBox="0 0 16 16">
                      <path d="M6 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z"/>
                  </svg></th>
              <th scope="col" @click="sortreporter_email">Создал
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-filter" viewBox="0 0 16 16">
                      <path d="M6 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z"/>
                  </svg></th>
              <th scope="col" @click="sortassignee_email" >Адресовано
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-filter" viewBox="0 0 16 16">
                      <path d="M6 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z"/>
                  </svg></th>
              <th scope="col" @click="sortBycreation_date">Дата
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-filter" viewBox="0 0 16 16">
                      <path d="M6 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z"/>
                  </svg></th>
              <th scope="col" @click="sortBypriority">Приоритет
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-filter" viewBox="0 0 16 16">
                      <path d="M6 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5zm-2-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5z"/>
                  </svg></th>
              <th scope="col">Действие</th>
          </tr>
          </thead>
          <tbody  v-for="ticket in paginateTickets" :key="ticket" >
          <tr>
              <td>{{ticket.id}}</td>
              <td @click="ShowTicket(ticket)" style="cursor: pointer">{{ticket.title}}</td>
              <td>{{ticket.ttype}}</td>
              <td>{{ticket.reporter_email}}</td>
              <td>{{ticket.assignee_email}}</td>
              <td>{{ticket.creation_date.slice(0,10)}}</td>
              <td>{{ticket.priority}}</td>
              <td>
              <v-icon
                  v-if="this.$store.getters.is_admin  || this.$store.getters.user === ticket.reporter_email"
                  @click="dialogVisibel(ticket)"
                  size="small"
                  class="me-2">
                  mdi-pencil
              </v-icon>
              <v-icon
                  v-if="this.$store.getters.is_admin  || this.$store.getters.user === ticket.reporter_email"
                  @click="dialogVisibeldelete(ticket.id)"
                  size="small">
                  mdi-delete
              </v-icon>
              </td>
          </tr>
          </tbody>
      </table>
      <v-pagination :length="Math.ceil(len_t/5)"
                    v-model="this.pagination_page"
      >

      </v-pagination>
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
              Закрыть
          </v-btn>


      </ModalWinEdit>
      <ModalDelete
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

      </ModalDelete>
  </div>
</template>

<script>
import axios from "axios"
import ModalWin from "@/components/ModalWin.vue";
import ModalWinEdit from "@/components/ModalWinEdit.vue";
import ModalDelete from "@/components/ModalDelete.vue";
export default {
    name: "Tickets-v.vue",
    components:{
        ModalWinEdit,
        ModalWin,
        ModalDelete,
    },
    data() {
        return {
            dialogdelete: false,
            ticket: {},
            info: [],
            len_t: 0,
            pagination_page: 1,
            ticket_page: 5,
            dialog: false,
            id: null
        }
    },
    async mounted() {
        await axios
            .get('http://127.0.0.1:8000/ticket/all')
            .then((response) => (this.info = response.data,
                                this.len_t = response.data.length))
    },
    computed: {
        paginateTickets(){
            let from = (this.pagination_page-1) * this.ticket_page
            let to = from + this.ticket_page;
            return this.info.slice(from, to)

        }
    },
    methods: {
        ShowTicket(value){
            this.$store.dispatch('ticket', value)
            this.$router.push('/ticket')
        },
        sortByTitle(){
            this.info.sort((a,b) => a.title.localeCompare(b.title))
        },
        sortBydescription(){
            this.info.sort((a,b) => a.description.localeCompare(b.description))
        },
        sortreporter_email(){
            this.info.sort((a,b) => a.reporter_email.localeCompare(b.reporter_email))
        },
        sortassignee_email(){
            this.info.sort((a,b) => a.assignee_email.localeCompare(b.assignee_email))
        },
        sortBycreation_date(){
            this.info.sort((a,b) => a.creation_date.localeCompare(b.creation_date))
        },
        sortBypriority(){
            this.info.sort((a,b) => a.priority.localeCompare(b.priority))
        },
        async DeleteTicket(value){
            try{
                await axios.delete('http://127.0.0.1:8000/ticket/'+value).
                then(() => this.dialogdelete = false
                )} catch(e) {
                this.Message = true
        }
    },
        dialogVisibel(value){
            this.dialog = true
            this.ticket= value
        },
        dialogVisibeldelete(value){
            this.dialogdelete= true
            this.id = value
        },


    },
    watch:{
        dialogdelete(){
            axios
                .get('http://127.0.0.1:8000/ticket/all')
                .then((response) => (this.info = response.data,
                    this.len_t = response.data.length))

        },
        dialog(){
            axios
                .get('http://127.0.0.1:8000/ticket/all')
                .then((response) => (this.info = response.data,
                    this.len_t = response.data.length))


        }
    }
}
</script>

<style scoped>
.table-pad{
    padding: 35px;
}
table{
    border-radius: 15px;
    border: black;
}
th{
    padding: 10px;
}
td{
    padding: 10px;
    border: black;
}
svg{
    cursor: pointer;
}
.v-icon{
    cursor: pointer;
}

.icon{
    height: 9px;
}

.modal-v{
    display: block;
    width: 180px;
    height:445px;
    position: fixed;
    bottom: 0px;
    right: 0px;
}
</style>