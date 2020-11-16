<template>
    <div style="height: 75vh; width: 50vw;">
        <l-map
            zoom="13"
            :center="[-33.452873, -70.5703947]"
            @move="log('move')"
        >
            <l-tile-layer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            ></l-tile-layer>
            <l-control-layers />

            <l-marker
                v-for="parking in state.parkingLots"
                :key="parking.id"
                :lat-lng="[parking.latitude, parking.longitude]"
            >
                <l-icon :icon-size="iconSize" />
                <l-popup>
                    pop FUNCIONA
                </l-popup>
                <l-tooltip>
                    Tooltipo funcionaaaa
                </l-tooltip>
            </l-marker>

            <l-polygon
                :lat-lngs="state.laReina"
                color="#41b782"
                :fill="true"
                :fillOpacity="0.2"
                fillColor="#41b782"
            />
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
    LPolygon,
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
        LPolygon,
        // LRectangle,
    },
    setup(props) {
        const state = reactive({
            zoom: 13,
            laReina: [
                [-33.458715, -70.5742777],
                [-33.437819, -70.5755947],
                [-33.4332046, -70.5861769],
                [-33.4279259, -70.5429983],
                [-33.4311571, -70.5254009],
                [-33.4684966, -70.5224764],
            ],
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
