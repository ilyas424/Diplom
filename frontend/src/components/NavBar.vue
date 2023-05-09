<template>
        <v-app-bar app>
            <v-app-bar-nav-icon v-if="this.$store.getters.user" @click="onDrawerIconClick">
            </v-app-bar-nav-icon>

            <v-toolbar-title>
                <h1 class="display-6" ><a href="/" >Cedar</a></h1>
            </v-toolbar-title>

            <div v-if="this.$store.state.user">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"></path>
                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"></path>

                </svg>
            </div>
            <div v-if="this.$store.state.user" class="user">
                {{this.$store.state.user}}
            </div>
            <div @click="handClick" v-if="this.$store.state.user" class="logout" >
                <button type="button" class="btn btn-outline-secondary">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="19" fill="currentColor" class="bi bi-box-arrow-right" viewBox="0 3 16 16">
                        <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"></path>
                        <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"></path>
                    </svg>
                </button>
            </div>

        </v-app-bar>

        <v-navigation-drawer app
                             v-model="drawer_visible"
        >
            <v-list
                    nav
            >
                <v-list-item
                        v-for="(item, i) in navigation_items"
                        :key="i"
                        :value="item"
                        :to="item.path"
                >
                    <template v-slot:prepend>
                        <v-icon :icon="item.icon"></v-icon>
                    </template>

                    <v-list-item-title
                            v-text="item.title"

                    >
                    </v-list-item-title>
                </v-list-item>
            </v-list>
            <div @click="Telebot" style="margin-left: 9px; margin-top: 200px; cursor: pointer">
                <v-icon icon="mdi-face-agent" />
                Техподдержка
            </div>
        </v-navigation-drawer>
</template>


<script>

export default {
    data:() => ({
        navigation_items: [
            {
                title: 'Home',
                icon: "mdi-home-outline",
                path: "/home"
            },
            {
                title: 'Backlog',
                icon: "mdi-fast-forward",
                path: "/tickets"
            },
            {
                title: 'Boards',
                icon: "mdi-flag",
                path: "/boards"
            },
            {
                title: 'Kanban',
                icon: "mdi-view-dashboard",
                path: "/kanban"
            },
            {
                title: 'Users',
                icon: "mdi-account-group",
                path: "/users"
            }
        ],
        drawer_visible: false,
        state: null

    }),
    methods: {
        onDrawerIconClick() {
            this.drawer_visible = !this.drawer_visible
        },
        handClick() {
            localStorage.removeItem('token');
            sessionStorage.clear();
            this.$store.dispatch('user', null)
            this.$store.dispatch('is_admin', null)
            this.$router.push('/')
            this.drawer_visible = false
        },
        Telebot() {
            window.open('https://t.me/CedarSupportBot', '_blank')
        }

    }

}

</script>

<style scoped>

.logout{
    padding: 15px;
}
.user{
    padding: 5px;
    margin-top: 2px;
}
a{
    text-decoration: none;
    color: #545454
}
a:hover{
    color: #545454
}

</style>