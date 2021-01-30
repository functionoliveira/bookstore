const axios = require('axios');

function Books () {
    const createBooks = async function (data) {
        // const response = await axios.post('http://localhost:5000/books/', data);
        return 200//response.status;
    }
    const getAllBooks = async function () {
        console.log('List all books');
        const { data } = await axios.get('http://localhost:5000/books/');
        return data;
    }
    const retrieveBooks = async function (id) {
        console.log(`Retrieve books id ${id}`);
        const { data } = await axios.get(`http://localhost:5000/books/${id}`);
        return data;
    }
    return {
        getAllBooks,
        createBooks,
        retrieveBooks
    }
}

module.exports = Books;