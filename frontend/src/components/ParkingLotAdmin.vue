<template>
    <div>
        <ul>
            <li v-for="(value, key) in state.errors" :key="value.id">
                {{ key }} : {{ value[0] }}
            </li>
        </ul>
        <form @submit.prevent="submitForm">
            <div class="form-row">
                <div class="col-md-6 mb-3 text-left">
                    <label for="description_txt">Description</label>
                    <input
                        type="text"
                        class="form-control "
                        id="description_txt"
                        placeholder="Description"
                        v-model="state.parkingLot.description"
                    />
                </div>
                <div class="col-md-6 mb-3 text-left">
                    <label for="maxcapacity_txt">Max capacity</label>
                    <input
                        type="number"
                        class="form-control "
                        placeholder="Max Capacity"
                        id="maxcapacity_txt"
                        v-model="state.parkingLot.max_capacity"
                    />
                </div>
            </div>
            <div class="form-row">
                <div class="col-md-6 mb-3 text-left">
                    <label for="address_txt">Address</label>
                    <input
                        type="text"
                        class="form-control "
                        placeholder="Address"
                        id="address_txt"
                        v-model="state.parkingLot.address"
                    />
                </div>
                <div class="col-md-6 mb-3 text-left">
                    <label for="latitude_txt">Latitude</label>
                    <input
                        type="text"
                        class="form-control "
                        placeholder="Latitude"
                        id="latitude_txt"
                        v-model="state.parkingLot.latitude"
                    />
                </div>
            </div>
            <div class="form-row">
                <div class="col-md-6 mb-3 text-left">
                    <label for="longitude_txt">Longitude</label>
                    <input
                        type="text"
                        class="form-control "
                        placeholder="Longitude"
                        id="longitude_txt"
                        v-model="state.parkingLot.longitude"
                    />
                </div>
            </div>

            <button class="btn btn-success btn-lg mb-md-3">
                Submit
            </button>
        </form>
        <button class="btn btn-info" @click="filterParkingLots">
            Search!
        </button>
        <button class="btn btn-info" @click="cleanForm">
            Clean all!
        </button>

        <Map
            :parking-lots-position="state.parkingLots"
            :key="state.componentKey"
        />

        <table class="table table-hover mt-md-3">
            <thead>
                <th>Description</th>
                <th>Max. Capacity</th>
                <th>Adress</th>
                <th>Latitude</th>
                <th>Longitude</th>
                <th>Bicycles in it</th>
            </thead>
            <tbody>
                <tr
                    v-for="parkingLot in state.parkingLots"
                    :key="parkingLot.id"
                    @dblclick="state.parkingLot = parkingLot"
                    :class="[
                        {
                            'table-warning':
                                state.parkingLot.id === parkingLot.id,
                        },
                    ]"
                >
                    <td>{{ parkingLot.description }}</td>
                    <td>{{ parkingLot.max_capacity }}</td>
                    <td>{{ parkingLot.address }}</td>
                    <td>{{ parkingLot.latitude }}</td>
                    <td>{{ parkingLot.longitude }}</td>
                    <td>{{ parkingLot.bicycles.length }}</td>
                    <td>
                        <button
                            class="btn btn-outline-danger btn-sm mx-1"
                            @click="deleteParkingLot(parkingLot)"
                        >
                            x
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import { reactive } from 'vue';
import Map from '@/components/Map.vue';

export default {
    name: 'ParkingLotAdmin',
    components: {
        Map,
    },
    setup() {
        const state = reactive({
            parkingLot: {},
            parkingLots: [],
            errors: [],
            componentKey: 0,
        });

        function cleanForm() {
            state.parkingLot = {};
            state.errors = [];
            this.getParkingLots();
        }

        function forceRerender() {
            state.componentKey += 1;
        }

        async function filterParkingLots() {
            if (Object.keys(state.parkingLot).length === 0) {
                this.getParkingLots();
                return;
            }
            var url = new URL('http://localhost:8000/api/parkinglots/');

            var query = state.parkingLot;
            // Delete empty query parameters
            for (let param in query) {
                if (
                    query[param] === undefined ||
                    query[param] === null ||
                    query[param] === ''
                ) {
                    delete query[param];
                }
            }

            url.search = new URLSearchParams(query).toString();

            const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
            var response = await fetch(url, {
                headers: {
                    Authorization: token,
                },
            });
            state.parkingLots = await response.json();
            this.forceRerender();
        }

        function submitForm() {
            if (state.parkingLot.id === undefined) {
                this.createParkingLot();
            } else {
                this.editParkingLot();
            }
        }

        async function getParkingLots() {
            const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
            var response = await fetch(
                'http://localhost:8000/api/parkinglots/',
                {
                    headers: {
                        Authorization: token,
                    },
                }
            );
            state.parkingLots = await response.json();
        }

        async function createParkingLot() {
            try {
                await this.getParkingLots();
                state.parkingLot.bicycles = [];
                const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
                let response = await fetch(
                    'http://localhost:8000/api/parkinglots/',
                    {
                        method: 'post',
                        headers: {
                            'Content-Type': 'application/json',
                            Authorization: token,
                        },
                        body: JSON.stringify(state.parkingLot),
                    }
                );
                let jsonResponse = await response.json();

                if (!response.ok) {
                    state.errors = jsonResponse;
                } else {
                    state.errors = [];
                }
                await this.getParkingLots();
                this.forceRerender();
            } catch (e) {
                state.errors = e;
            }
        }

        async function editParkingLot() {
            await this.getParkingLots();
            const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
            await fetch(
                `http://localhost:8000/api/parkinglots/${state.parkingLot.id}/`,
                {
                    method: 'put',
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: token,
                    },
                    body: JSON.stringify(state.parkingLot),
                }
            );

            await this.getParkingLots();
            state.parkingLot = {};
        }

        async function deleteParkingLot(parkingLot) {
            await this.getParkingLots();
            const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
            await fetch(
                `http://localhost:8000/api/parkinglots/${parkingLot.id}/`,
                {
                    method: 'delete',
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: token,
                    },
                    body: JSON.stringify(this.parkingLot),
                }
            );

            await this.getParkingLots();
        }

        return {
            state,
            cleanForm,
            submitForm,
            getParkingLots,
            createParkingLot,
            editParkingLot,
            deleteParkingLot,
            filterParkingLots,
            forceRerender,
        };
    },

    async created() {
        await this.getParkingLots();
    },
};
</script>

<style></style>
