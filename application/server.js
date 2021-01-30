const Books = require('./domain/books');
const Customers = require('./domain/customers');
const Sales = require('./domain/sales');
const DataBooks = require('./data/data-books');
const DataCustomers = require('./data/data-customers');
const DataSales = require('./data/data-sales');

const books = Books();
const customers = Customers();
const sales = Sales();

function insertAllBooks () {
    console.log('BOOKS');
    console.log('Insert at least 5 books');
    return Promise.all([
        books.createBooks(DataBooks.animal_farm).then((status) => console.log("Status ", status)),
        books.createBooks(DataBooks.brave_new_world).then((status) => console.log("Status ", status)),
        books.createBooks(DataBooks.design_patterns).then((status) => console.log("Status ", status)),
        books.createBooks(DataBooks.clean_code).then((status) => console.log("Status ", status)),
        books.createBooks(DataBooks.the_odyssey).then((status) => console.log("Status ", status))
    ]);
}

function insertAllCustomers () {
    console.log('CUSTOMERS');
    console.log('Inserts at least 3 customers');
    return Promise.all([
        customers.createCustomers(DataCustomers.mike_johnson).then((status) => console.log("Status ", status)),
        customers.createCustomers(DataCustomers.emma_thompson).then((status) => console.log("Status ", status)),
        customers.createCustomers(DataCustomers.susan_jones).then((status) => console.log("Status ", status))
    ]);
}

function insertAllSales () {
    console.log('SALES');
    console.log('Insert at least 2 sales');
    return Promise.all([
        sales.createSales(DataSales[0]).then((status) => console.log("Status ", status)),
        sales.createSales(DataSales[1]).then((status) => console.log("Status ", status))
    ]);
}

(async () => {
    await insertAllBooks();
    await books.getAllBooks().then(data => console.log(data));
    await books.retrieveBooks(1).then(data => console.log(data));
    await books.retrieveBooks(2).then(data => console.log(data));
    
    await insertAllCustomers();
    await customers.getAllCustomers().then(data => console.log(data));
    await customers.retrieveCustomers(2).then(data => console.log(data));

    await insertAllSales();
    await sales.getAllSales().then(data => console.log(data));
    await sales.retrieveSales(1).then(data => console.log(data));
})();