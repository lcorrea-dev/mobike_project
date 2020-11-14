<template>
    <div id="app">
        <form @submit.prevent="submitForm">
            <div class="form-group row">
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="QR Code"
                    v-model="bicycle.qr_code"
                />
                <input
                    type="date"
                    class="form-control col-3 mx-2"
                    placeholder="Purchase date"
                    v-model="bicycle.purchase_date"
                />
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="Brand"
                    v-model="bicycle.brand"
                />
                <input
                    type="text"
                    class="form-control col-3 mx-2"
                    placeholder="Model"
                    v-model="bicycle.model"
                />
                <input
                    type="number"
                    class="form-control col-3 mx-2"
                    placeholder="Metters traveled"
                    v-model="bicycle.m_traveled"
                />
                <input
                    type="checkbox"
                    class="form-control col-3 mx-2"
                    placeholder="Is locked?"
                    v-model="bicycle.is_locked"
                />
                <button class="btn btn-success">Submit</button>
            </div>
        </form>

        <table class="table">
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
                    v-for="bicycle in bicycles"
                    :key="bicycle.id"
                    @dblclick="$data.bicycle = bicycle"
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
export default {
    name: 'App',

    data() {
        return {
            bicycle: {},
            bicycles: [],
        };
    },

    async created() {
        await this.getBicycles();
    },

    methods: {
        submitForm() {
            if (this.bicycle.id === undefined) {
                this.createBicycle();
            } else {
                this.editBicycle();
            }
        },

        async getBicycles() {
            var response = await fetch('http://localhost:8000/api/bicycles/');
            this.bicycles = await response.json();
        },

        async createBicycle() {
            await this.getBicycles();

            await fetch('http://localhost:8000/api/bicycles/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.bicycle),
            });

            await this.getBicycles();
        },

        async editBicycle() {
            await this.getBicycles();

            await fetch(
                `http://localhost:8000/api/bicycles/${this.bicycle.id}/`,
                {
                    method: 'put',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.bicycle),
                }
            );

            await this.getBicycles();
            this.bicycle = {};
        },
        async deleteBicycle(bicycle) {
            await this.getBicycles();

            await fetch(`http://localhost:8000/api/bicycles/${bicycle.id}/`, {
                method: 'delete',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.bicycle),
            });

            await this.getBicycles();
        },
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
    margin-top: 60px;
}
</style>
