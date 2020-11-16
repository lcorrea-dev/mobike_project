<template>
    <div id="app">
        <NavBar />
        <div id="active-app">
            <BicyclesAdmin />
        </div>
    </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue';
import BicyclesAdmin from '@/components/BicyclesAdmin.vue';

export default {
    name: 'App',
    components: {
        NavBar,
        BicyclesAdmin,
    },
};
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    /* margin-top: 60px; */
}
</style>
