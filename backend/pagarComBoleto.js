const axios = require('axios');

async function pagarComBoleto(pk) {
    try {
        const url = `http://127.0.0.1:8000/tasks/${pk}`;
        const response = await axios.get(url);

        const price = response.data.price;

        const valorFinal = price * 2;

        console.log(`Valor a pagar: R$ ${valorFinal}`);
    } catch (error) {
        console.error('Erro ao buscar dados:', error.message);
    }
}


pagarComBoleto(123);
