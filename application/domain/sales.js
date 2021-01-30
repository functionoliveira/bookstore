const axios = require('axios');

function Sales () {
    const createSales = async function (data) {
        // const response = await axios.post('http://localhost:5000/sales/', data);
        return 200//response.status;
    }
    const getAllSales = async function () {
        console.log('List all sales');
        const { data } = await axios.get('http://localhost:5000/sales/');
        return data;
    }
    const retrieveSales = async function (id) {
        console.log(`Retrieve sales id ${id}`);
        const { data } = await axios.get(`http://localhost:5000/sales/${id}`);
        return data;
    }
    return {
        createSales,
        getAllSales,
        retrieveSales
    }
}

module.exports = Sales;