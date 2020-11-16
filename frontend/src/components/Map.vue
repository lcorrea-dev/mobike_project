<template>
    <div style="height: 40vh; width: 50vw;" class="mx-auto">
        <l-map zoom="13" :center="[-33.445841, -70.546285]">
            <l-tile-layer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            ></l-tile-layer>
            <l-control-layers />

            <l-marker
                v-for="parking in state.parkingLots"
                :key="parking.id"
                :lat-lng="[parking.latitude, parking.longitude]"
            >
                <l-icon :icon-size="12" />
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

            <!-- <l-polyline
                :lat-lngs="state.laReina"
                color="#41b782"
                :fill="true"
                :fillOpacity="0.2"
                fillColor="#41b782"
            /> -->
        </l-map>
    </div>
</template>
<script>
import {
    LMap,
    LIcon,
    LTileLayer,
    LMarker,
    LControlLayers,
    LTooltip,
    LPopup,
    // LPolyline,
    // LPolygon,
    // LRectangle,
} from '@vue-leaflet/vue-leaflet';
import 'leaflet/dist/leaflet.css';
import { toRef, reactive } from 'vue';

export default {
    props: ['parkingLotsPosition'],
    components: {
        LMap,
        LIcon,
        LTileLayer,
        LMarker,
        LControlLayers,
        LTooltip,
        LPopup,
        // LPolyline,
        // LPolygon,
        // LRectangle,
    },
    setup(props) {
        const state = reactive({
            zoom: 13,
            // laReina: [
            //     [-33.458715, -70.5742777],
            //     [-33.437819, -70.5755947],
            //     [-33.4332046, -70.5861769],
            //     [-33.4279259, -70.5429983],
            //     [-33.4311571, -70.5254009],
            //     [-33.4684966, -70.5224764],
            // ],
            parkingLots: toRef(props, 'parkingLotsPosition'),
            // parkingLots: [
            //     { id: 1, latitude: -33.458715, longitude: -70.5742777 },
            //     { id: 1, latitude: -33.4684966, longitude: -70.5224764 },
            // ],
        });
        return {
            state,
        };
    },
};
</script>
