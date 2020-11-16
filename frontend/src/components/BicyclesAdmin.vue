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
                    placeholder="QR Code"
                    v-model="state.bicycle.qr_code"
                />
                <input
                    type="date"
                    class="form-control col-3 mx-2"
                    placeholder="Purchase date"
                    v-model="state.bicycle.purchase_date"
                />
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="Brand"
                    v-model="state.bicycle.brand"
                />
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="Model"
                    v-model="state.bicycle.model"
                />
                <input
                    type="number"
                    class="form-control col-3 mx-2"
                    placeholder="Metters traveled"
                    v-model="state.bicycle.m_traveled"
                />
                <label for="is_locked_chk">is locked?</label>
                <input
                    name="is_locked_chk"
                    type="checkbox"
                    class="form-control col-3 mx-2"
                    placeholder="Is locked?"
                    v-model="state.bicycle.is_locked"
                />
                <button class="btn btn-success">
                    Submit
                </button>
            </div>
        </form>
        <button class="btn btn-success" @click="filterBicycles">
            Search!
        </button>
        <button class="btn btn-success" @click="cleanForm">
            Clean all!
        </button>
        <Map markers="state.markers" />
        <table class="table table-hover">
            <thead>
                <th>QR Code</th>
                <th>Purchase date</th>
                <th>Brand</th>
                <th>Model</th>
                <th>Metters traveled</th>
                <th>Is locked?</th>
            </thead>
            <tbody>
                <tr
                    v-for="bicycle in state.bicycles"
                    :key="bicycle.id"
                    @dblclick="state.bicycle = bicycle"
                    :class="[
                        { 'table-warning': state.bicycle.id === bicycle.id },
                    ]"
                >
                    <td>{{ bicycle.qr_code }}</td>
                    <td>{{ bicycle.purchase_date }}</td>
                    <td>{{ bicycle.brand }}</td>
                    <td>{{ bicycle.model }}</td>
                    <td>{{ bicycle.m_traveled }}</td>
                    <td>{{ bicycle.is_locked }}</td>
                    <td>
                        <button
                            class="btn btn-outline-danger btn-sm mx-1"
                            @click="deleteBicycle(bicycle)"
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

export default {
    name: 'BicyclesAdmin',
    setup() {
        const state = reactive({
            bicycle: {},
            bicycles: [],
            errors: [],
        });

        function cleanForm() {
            state.bicycle = {};
            state.errors = [];
            this.getBicycles();
        }

        async function filterBicycles() {
            console.log(state.bicycle);
            if (Object.keys(state.bicycle).length === 0) {
                this.getBicycles();
                return;
            }
            var url = new URL('http://localhost:8000/api/bicycles/');

            var query = state.bicycle;
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

            console.log(query);
            console.log(url);
            var response = await fetch(url);
            state.bicycles = await response.json();
        }

        function submitForm() {
            if (state.bicycle.id === undefined) {
                this.createBicycle();
            } else {
                this.editBicycle();
            }
        }

        async function getBicycles() {
            var response = await fetch('http://localhost:8000/api/bicycles/');
            state.bicycles = await response.json();
        }

        async function createBicycle() {
            try {
                await this.getBicycles();

                let response = await fetch(
                    'http://localhost:8000/api/bicycles/',
                    {
                        method: 'post',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(state.bicycle),
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

                await this.getBicycles();
            } catch (e) {
                state.errors = e;
            }
        }

        async function editBicycle() {
            await this.getBicycles();
            await fetch(
                `http://localhost:8000/api/bicycles/${state.bicycle.id}/`,
                {
                    method: 'put',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(state.bicycle),
                }
            );

            await this.getBicycles();
            state.bicycle = {};
        }

        async function deleteBicycle(bicycle) {
            await this.getBicycles();

            await fetch(`http://localhost:8000/api/bicycles/${bicycle.id}/`, {
                method: 'delete',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.bicycle),
            });

            await this.getBicycles();
        }

        return {
            state,
            cleanForm,
            submitForm,
            getBicycles,
            createBicycle,
            editBicycle,
            deleteBicycle,
            filterBicycles,
        };
    },

    async created() {
        await this.getBicycles();
    },
};
</script>
