<template>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="#">Mobike APP</a>
            <button
                class="navbar-toggler"
                type="button"
                data-toggle="collapse"
                data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li
                        v-for="tab in state.tabs"
                        :key="tab"
                        :class="[
                            'nav-link',
                            { active: state.currentTab === tab },
                        ]"
                        @click="state.currentTab = tab"
                    >
                        {{ tab }}
                    </li>
                </ul>
            </div>
        </nav>

        <div id="active-app">
            <!-- <keep-alive> -->
            <component :is="state.currentTab"> </component>
            <!-- </keep-alive> -->
        </div>
    </div>
</template>
<script>
import BicyclesAdmin from '@/components/BicyclesAdmin.vue';
import ParkingLotAdmin from '@/components/ParkingLotAdmin.vue';
import { reactive } from 'vue';

export default {
    name: 'App',
    components: {
        BicyclesAdmin,
        ParkingLotAdmin,
    },
    setup() {
        const state = reactive({
            currentTab: 'BicyclesAdmin',
            tabs: ['BicyclesAdmin', 'ParkingLotAdmin'],
        });
        return {
            state,
        };
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
}
</style>
