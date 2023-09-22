import { createApp } from 'vue'
import App from './App.vue'
import NutUI, { Watermark } from "@nutui/nutui";
import "@nutui/nutui/dist/style.css";

createApp(App).use(NutUI).use(Watermark).mount('#app');