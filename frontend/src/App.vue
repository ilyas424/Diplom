<template>
    <v-app>
        <NavBar></NavBar>
        <v-main>
            <router-view>
            </router-view>
        </v-main>
        <my-footer></my-footer>
    </v-app>

</template>

<script>
import NavBar from "@/components/NavBar.vue";
import myFooter from "@/components/myFooter.vue";
import axios from "axios";

export default {
    components: {
        NavBar,
        myFooter,
    }

}
</script>

<style scoped>

</style>

