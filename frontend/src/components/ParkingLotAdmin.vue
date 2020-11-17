<template>
    <div>
        <ul>
            <li v-for="(value, key) in state.errors" :key="value.id">
                {{ key }} : {{ value[0] }}
            </li>
        </ul>
        <form @submit.prevent="submitForm">
            <div class="form-group row">
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="Description"
                    v-model="state.parkingLot.description"
                />
                <input
                    type="number"
                    class="form-control col-3 mx-2"
                    placeholder="Max Capacity"
                    v-model="state.parkingLot.max_capacity"
                />
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="Address"
                    v-model="state.parkingLot.address"
                />
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="Latitude"
                    v-model="state.parkingLot.latitude"
                />
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="Longitude"
                    v-model="state.parkingLot.longitude"
                />
                <!-- <label for="is_locked_chk">is locked?</label>
                <input
                    name="is_locked_chk"
                    type="checkbox"
                    class="form-control col-3 mx-2"
                    placeholder="Is locked?"
                    v-model="state.parkingLot.is_locked"
                /> -->
                <button class="btn btn-success">
                    Submit
                </button>
            </div>
        </form>
        <button class="btn btn-success" @click="filterParkingLots">
            Search!
        </button>
        <button class="btn btn-success" @click="cleanForm">
            Clean all!
        </button>
        <keep-alive>
            <Map :parking-lots-position="state.parkingLots" />
        </keep-alive>

        <table class="table table-hover">
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
        });

        function cleanForm() {
            state.parkingLot = {};
            state.errors = [];
            state.parkingLots = this.getParkingLots();
        }

        async function filterParkingLots() {
            console.log(state.parkingLot);
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
            const parkingLots = await response.json();
            state.parkingLots = parkingLots;

            return parkingLots;
        }

        async function createParkingLot() {
            try {
                await this.getParkingLots();
                var parkingLot = state.parkingLot;
                parkingLot.bicycles = [];
                const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
                let response = await fetch(
                    'http://localhost:8000/api/parkinglots/',
                    {
                        method: 'post',
                        headers: {
                            'Content-Type': 'application/json',
                            Authorization: token,
                        },
                        body: JSON.stringify(parkingLot),
                    }
                );
                let jsonResponse = await response.json();
                console.log('aaaaaa');
                console.log(jsonResponse);
                if (!response.ok) {
                    state.errors = jsonResponse;
                } else {
                    state.errors = [];
                }

                await this.getParkingLots();
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
        };
    },

    async created() {
        await this.getParkingLots();
    },
};
</script>

<style></style>
