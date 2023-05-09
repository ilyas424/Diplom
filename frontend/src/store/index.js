import {createStore} from 'vuex'
import createPersistedState from 'vuex-persistedstate'

export default createStore({
    plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
    state: {
        user: null,
        kanban: null,
        ticket: null,
        is_admin: null
    },
    getters: {
        user: (state) => {
            return state.user
        },
        is_admin: (state) => {
            return state.is_admin
        },
        kanban: (state) => {
            return state.kanban
        },
        ticket: (state) => {
            return state.ticket
        },

    },
    mutations: {
        user(state, user){
            state.user = user
        },
        is_admin(state, is_admin){
            state.is_admin = is_admin
        },
        kanban(state, kanban){
            state.kanban = kanban
        },
        ticket(state, ticket){
            state.ticket = ticket
        },


    },
    actions: {
        user(context, user) {
            context.commit('user', user)
        },
        is_admin(context, is_admin) {
            context.commit('is_admin', is_admin)
        },
        kanban(context, kanban) {
            context.commit('kanban', kanban)
        },
        ticket(context, ticket) {
            context.commit('ticket', ticket)
        },

    }

})

