const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const livroRoutes = require('./routes/livro');

const app = express();

// Conectar ao MongoDB
mongoose.connect('mongodb+srv://<usuario:senha>@livroapi.rz0cq.mongodb.net/?retryWrites=true&w=majority&appName=LivroApi', {
}).then(() => {
    console.log('Conectado ao MongoDB');
}).catch(err => {
    console.error('Erro ao conectar ao MongoDB', err);
});

// Configurar body-parser para processar JSON
app.use(bodyParser.json());

// Configurar rotas
app.use('/api/livros', livroRoutes);

module.exports = app;
