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
                    <label for="qr_code_txt">QR Code</label>
                    <input
                        type="text"
                        class="form-control"
                        id="qr_code_txt"
                        placeholder="QR Code"
                        v-model="state.bicycle.qr_code"
                    />
                </div>
                <div class="col-md-6 mb-3 text-left">
                    <label for="purchase_date_txt">Purchase date</label>
                    <input
                        type="date"
                        class="form-control"
                        id="purchase_date_txt"
                        placeholder="Purchase date"
                        v-model="state.bicycle.purchase_date"
                    />
                </div>
            </div>

            <div class="form-row">
                <div class="col-md-6 mb-3 text-left">
                    <label for="brand_txt">Brand</label>
                    <input
                        type="text"
                        class="form-control"
                        placeholder="Brand"
                        id="brand_txt"
                        v-model="state.bicycle.brand"
                    />
                </div>
                <div class="col-md-6 mb-3 text-left">
                    <label for="model_txt">Model</label>
                    <input
                        type="text"
                        class="form-control"
                        placeholder="Model"
                        id="model_txt"
                        v-model="state.bicycle.model"
                    />
                </div>
            </div>
            <div class="form-row">
                <div class="col-md-6 mb-3 text-left">
                    <label for="metters_txt">Model</label>
                    <input
                        type="number"
                        class="form-control"
                        id="metters_txt"
                        placeholder="Metters traveled"
                        v-model="state.bicycle.m_traveled"
                    />
                </div>
                <div class="col-md-6 mb-3 text-left">
                    <label for="is_locked_select">Is locked?</label>

                    <select
                        class="form-control"
                        v-model="state.bicycle.is_locked"
                        id="is_locked_select"
                    >
                        <option
                            v-for="option in state.options"
                            :key="option.text"
                            :value="option.value"
                            :selected="option.value == undefined"
                            >{{ option.text }}</option
                        >
                    </select>
                </div>
            </div>
            <button class="btn btn-success btn-lg mb-md-3">
                Submit
            </button>
        </form>

        <button class="btn btn-info" @click="filterBicycles">
            Search!
        </button>
        <button class="btn btn-info" @click="cleanForm">
            Clean all!
        </button>
        <Map markers="state.markers" />
        <table class="table table-hover mt-md-3 ">
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
                    <td>{{ bicycle.is_locked == true ? 'Yes' : 'No' }}</td>
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
            options: [
                { text: 'Select one', value: undefined },
                { text: 'Yes', value: true },
                { text: 'No', value: false },
            ],
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

            const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
            var response = await fetch(url, {
                headers: {
                    Authorization: token,
                },
            });
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
            const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
            var response = await fetch('http://localhost:8000/api/bicycles/', {
                headers: {
                    Authorization: token,
                },
            });
            state.bicycles = await response.json();
        }

        async function createBicycle() {
            try {
                await this.getBicycles();
                const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
                let response = await fetch(
                    'http://localhost:8000/api/bicycles/',
                    {
                        method: 'post',
                        headers: {
                            'Content-Type': 'application/json',
                            Authorization: token,
                        },
                        body: JSON.stringify(state.bicycle),
                    }
                );
                let jsonResponse = await response.json();

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
            const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
            await fetch(
                `http://localhost:8000/api/bicycles/${state.bicycle.id}/`,
                {
                    method: 'put',
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: token,
                    },
                    body: JSON.stringify(state.bicycle),
                }
            );

            await this.getBicycles();
            state.bicycle = {};
        }

        async function deleteBicycle(bicycle) {
            await this.getBicycles();
            const token = 'Token 9d6b8e13d658bb78210dad6602ac3ff2112df1e8';
            await fetch(`http://localhost:8000/api/bicycles/${bicycle.id}/`, {
                method: 'delete',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: token,
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
