import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
import "bootstrap/dist/js/bootstrap.js"
import 'bootstrap-select'
import store from "@/store";
import '@/axios'
import 'material-design-icons-iconfont'

loadFonts()




createApp(App).use(router).use(store)
    .use(vuetify)
  .mount('#app')

