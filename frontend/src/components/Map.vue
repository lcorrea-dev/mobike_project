<template>
    <div style="height: 40vh; width: 50vw;" class="mx-auto">
        <l-map zoom="13" :center="[-33.445841, -70.546285]">
            <l-tile-layer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            ></l-tile-layer>
            <l-marker
                v-for="parking in parkingLotsPosition"
                :key="parking.id"
                :lat-lng="[parking.latitude, parking.longitude]"
            >
                <l-popup>
                    <p class="font-weight-bold">{{ parking.description }}</p>
                    <p>
                        {{ parking.bicycles.length }}/{{ parking.max_capacity }}
                        <i class="fas fa-bicycle" style="font-size: 16px"></i>
                    </p>
                    <p>{{ parking.address }}</p>
                </l-popup>
                <l-tooltip>
                    {{ parking.description }}
                </l-tooltip>
            </l-marker>
        </l-map>
    </div>
</template>
<script>
import {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
    LPopup,
} from '@vue-leaflet/vue-leaflet';
import 'leaflet/dist/leaflet.css';
import { reactive } from 'vue';

export default {
    props: ['parkingLotsPosition'],
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LTooltip,
        LPopup,
    },
    setup(props) {
        const state = reactive({
            parkingLots: props.ParkingLotsPosition,
        });
        return {
            state,
        };
    },
};
</script>
