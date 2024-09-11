const express = require('express');
const Livro = require('../models/livro');
const router = express.Router();

// 1. Cadastro de livros
router.post('/', async (req, res) => {
    const { titulo, autor, editora, anoPublicacao, numeroPaginas } = req.body;
    if (!titulo || !autor || !editora || !anoPublicacao || !numeroPaginas) {
        return res.status(400).json({ message: 'Todos os campos são obrigatórios!' });
    }
    try {
        const novoLivro = new Livro({ titulo, autor, editora, anoPublicacao, numeroPaginas });
        await novoLivro.save();
        res.status(201).json(novoLivro);
    } catch (error) {
        res.status(500).json({ message: 'Erro ao cadastrar livro', error });
    }
});

// 2. Listagem de livros
router.get('/', async (req, res) => {
    try {
        const livros = await Livro.find();
        res.status(200).json(livros);
    } catch (error) {
        res.status(500).json({ message: 'Erro ao listar livros', error });
    }
});

// 3. Consulta de livro por ID
router.get('/:id', async (req, res) => {
    try {
        const livro = await Livro.findById(req.params.id);
        if (!livro) return res.status(404).json({ message: 'Livro não encontrado' });
        res.status(200).json(livro);
    } catch (error) {
        res.status(500).json({ message: 'Erro ao buscar livro', error });
    }
});

// 4. Remoção de livro
router.delete('/:id', async (req, res) => {
    try {
        const livro = await Livro.findByIdAndDelete(req.params.id);
        if (!livro) return res.status(404).json({ message: 'Livro não encontrado' });
        res.status(200).json({ message: 'Livro removido com sucesso' });
    } catch (error) {
        res.status(500).json({ message: 'Erro ao remover livro', error });
    }
});

module.exports = router;