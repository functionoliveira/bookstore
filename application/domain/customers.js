const axios = require('axios');

function Customers () {
    const createCustomers = async function (data) {
        // const response = await axios.post('http://localhost:5000/customers/', data);
        return 200//response.status;
    }
    const getAllCustomers = async function () {
        console.log('List all customers');
        const { data } = await axios.get('http://localhost:5000/customers/');
        return data;
    }
    const retrieveCustomers = async function (id) {
        console.log(`Retrieve customers id ${id}`);
        const { data } = await axios.get(`http://localhost:5000/customers/${id}`);
        return data;
    }
    return {
        createCustomers,
        getAllCustomers,
        retrieveCustomers
    }
}

module.exports = Customers;