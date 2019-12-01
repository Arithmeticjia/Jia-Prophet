import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import About from "@/components/About";
import NotFound from "@/components/NotFound";
import Home from "@/components/Home";
import Archive from "@/components/Archive";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/archive',
      name: 'Archive',
      component: Archive
    },
  ],
  mode: 'history',
})
