<template>
  <v-app>
      <div class="my-3 p-3 bg-body rounded shadow-sm">
          <div class="row">
              <div class="col-12">
                  <h1 class="fw-light">Проекты</h1>
              </div>
              <div class="col" >
              <button
                  v-if="this.$store.getters.is_admin"
                  class="btn btn-outline-success"
                  @click="DialogCreate = true"
              >Создать+</button>
              </div>
          </div>
          <div v-for="board in paginateBoards" :key="board" class="d-flex text-muted pt-3">
              <hr>
              <div class="pb-3 mb-0 small lh-sm border-bottom w-100" style="background-color: whitesmoke; padding: 10px; border-radius: 4px">
                  <div class="d-flex justify-content-between">
                      <div>
                      <p @click="RedirectBoardById(board.id)" class="fst-italic" style="font-size: 17px; color:black">
                          id {{board.id}} /
                          {{ board.board_name }}</p>
                          <p>Описание: {{board.description}}</p>
                          <p>Создал: {{board.creator_email}}</p>
                          <p>Дата: {{board.creation_date.slice(0,10)}}</p>
                          <p
                              v-if="board.is_open"
                          >Cтатус: Открыта</p>
                          <p
                              v-if="!board.is_open"
                          >Cтатус: Закрыта</p>
                      </div>
                      <div>
                          <button
                              @click="DialogBoardClose=true; board_id=board.id"
                              v-if="board.is_open && this.$store.getters.is_admin"
                              type="button" class="btn btn-outline-danger" style="margin-right: 10px">Закрыть доску</button>
                      <button
                          @click="DialogBoardClose=true; board_id=board.id"
                          v-if="!board.is_open && this.$store.getters.is_admin"
                          type="button" class="btn btn-outline-success" style="margin-right: 10px">Открыть доску</button>
                      <button type="button" class="btn btn-danger"
                              v-if="this.$store.getters.is_admin"
                              @click="BoardDeleteDialog=true; board_id=board.id"
                      >Удалить</button>
                      </div>
                  </div>
                  <div>
                  </div>

              </div>
          </div>
          <v-pagination :length="Math.ceil(this.boards.length/3)"
                        v-model="this.pagination_page"
          >

          </v-pagination>

      </div>

      <ModalDelete
          v-bind:dialogwarning="BoardDeleteDialog"
      >
          <v-btn
              color="green-darken-1"
              variant="text"
              @click="BoardDeleteDialog = false"
          >
              Нет
          </v-btn>
          <v-btn
              color="green-darken-1"
              variant="text"
              @click="DeleteBoardById"
          >
              Да
          </v-btn>
      </ModalDelete>
      <Modal
      v-bind:dialogwarning="DialogBoardClose"
      >
          <v-card-title class="text-h5">
              <strong>Подтверждения</strong>
          </v-card-title>
          <v-card-text>Вы действительно хотите изменить состояние доски?</v-card-text>
          <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                  color="green-darken-1"
                  variant="text"
                  @click="DialogBoardClose = false"
              >
                  Нет
              </v-btn>
              <v-btn
                  color="green-darken-1"
                  variant="text"
                  @click="CloseBoardById"
              >
                  Да
              </v-btn>
          </v-card-actions>
      </Modal>
      <Modal
      v-bind:dialogwarning="DialogCreate">
          <v-card-title class="text-h5">
              <strong>Создание доски</strong>
          </v-card-title>
              <v-card-text>
                  <v-container>
                      <p>Заполните пожалуйста все поля</p>
                      <v-row>
                          <v-col
                              cols="12"

                          >
                              <v-text-field
                                  v-model="board.board_name"
                                  label="Название"
                                  hint=""
                              ></v-text-field>
                              <v-text-field
                                  v-model="board.description"
                                  label="Описание"
                                  required
                              ></v-text-field>
                              <div
                                  v-for="(input, index) in Columns"
                                  :key="`columninput-${index}`"
                                  class="input wrapper flex items-center"
                              >
                                  <input
                                      v-model="input.column"
                                      type="text"
                                      class="h-10 rounded  p-2"
                                      placeholder="Название столбца"
                                  />
                                  <svg

                                      @click="addField(input, Columns)"
                                      xmlns="http://www.w3.org/2000/svg"
                                      viewBox="0 0 24 24"
                                      width="24"
                                      height="24"
                                      class="ml-2"
                                  >
                                      <path fill="none" d="M0 0h24v24H0z" />
                                      <path
                                          fill="green"
                                          d="M11 11V7h2v4h4v2h-4v4h-2v-4H7v-2h4zm1 11C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z"
                                      />
                                  </svg>

                                  <!--          Remove Svg Icon-->
                                  <svg
                                          v-show="Columns.length > 1"
                                      @click="removeField(index, Columns)"
                                      xmlns="http://www.w3.org/2000/svg"
                                      viewBox="0 0 24 24"
                                      width="24"
                                      height="24"
                                      class="ml-2"
                                  >
                                      <path fill="none" d="M0 0h24v24H0z" />
                                      <path
                                          fill="#EC4899"
                                          d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16zm0-9.414l2.828-2.829 1.415 1.415L13.414 12l2.829 2.828-1.415 1.415L12 13.414l-2.828 2.829-1.415-1.415L10.586 12 7.757 9.172l1.415-1.415L12 10.586z"
                                      />
                                  </svg>
                              </div>
                          </v-col>

                      </v-row>
                  </v-container>
              </v-card-text>
             <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                  color="green-darken-1"
                  variant="text"
                  @click="DialogCreate = false ; this.board = {}"
              >
                  Закрыть
              </v-btn>
              <v-btn
                  color="green-darken-1"
                  variant="text"
                  @click="BoardCreate"
              >
                  Создать
              </v-btn>
          </v-card-actions>
      </Modal>
  </v-app>
</template>

<script>
import axios from "axios";
import ModalDelete from "@/components/ModalDelete.vue";
import Modal from "@/components/Modal.vue";
export default {
    name: "Boards-v.vue",
    components:{
        ModalDelete,
        Modal
    },
    data() {
        return{
            ticket_page: 3,
            pagination_page: 1,
            Columns: [{ column: "" }],
            boards: [],
            BoardDeleteDialog: false,
            board_id: null,
            DialogBoardClose: false,
            DialogCreate: false,
            board:{
                board_name: '',
                description: '',
                creator_email: '',
                columns: []
            }
        }
    },
    mounted() {
        axios
            .get('http://127.0.0.1:8000/board/all')
            .then(response => (this.boards = response.data));
    },
    computed: {
        paginateBoards(){
            let from = (this.pagination_page-1) * this.ticket_page
            let to = from + this.ticket_page;
            return this.boards.slice(from, to)

        }
    },
    methods:{
        addField(value, fieldType) {
            fieldType.push({ value: "" });
        },
        removeField(index, fieldType) {
            fieldType.splice(index, 1);
        },
        async BoardCreate(){
            for (let i in this.Columns){
                this.board.columns.push(this.Columns[i].column)
            }
            this.board.creator_email = this.$store.getters.user

            await axios.post('http://127.0.0.1:8000/board/', this.board)

            this.DialogCreate = false
            this.board = {}
            this.Columns = [{ column: "" }]

            axios
                .get('http://127.0.0.1:8000/board/all')
                .then(response => (this.boards = response.data));

            this.board ={board_name: '',description: '', creator_email: '', columns: []}

        },
        async DeleteBoardById(){
            await axios.delete('http://127.0.0.1:8000/board/'+this.board_id)

            this.BoardDeleteDialog = false


            axios
                .get('http://127.0.0.1:8000/board/all')
                .then(response => (this.boards = response.data));

        },
        async CloseBoardById(){
            await axios.patch('http://127.0.0.1:8000/board/'+this.board_id)

            this.DialogBoardClose = false

            axios
                .get('http://127.0.0.1:8000/board/all')
                .then(response => (this.boards = response.data));

        },
        RedirectBoardById(value) {
            this.$store.dispatch('kanban',value)
            this.$router.push('kanban')
        }
    },
}
</script>

<style scoped>
.fst-italic{
    cursor: pointer;
}
.ml-2{
    cursor: pointer;
}
</style>