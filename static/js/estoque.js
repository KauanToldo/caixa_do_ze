function close_addproduto() {
    modal = document.querySelector('#modal_produto')
    modal.style.display = 'none';
}

function close_editproduto() {
    modal = document.querySelector('.modal_produto_edit')
    modal.style.display = 'none';
}

function open_editproduto() {
    modal = document.querySelector('.modal_produto_edit')
    modal.style.display = 'flex';
}

function open_addproduto() {
    modal = document.querySelector('#modal_produto')
    modal.style.display = 'flex';
}

function open_addvenda() {
    modal = document.querySelector('#modal_venda')
    modal.style.display = 'flex';
}

function close_addvenda() {
    modal = document.querySelector('#modal_venda')
    modal.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.addprodutoform');
    
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        const data = {
            nome: formData.get('nome'),
            quantidade: formData.get('quantidade'),
            preco_compra: formData.get('preco_compra'),
            preco_venda: formData.get('preco_venda')
        };
        
        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(produto => {
            form.reset();
            document.getElementById('modal_produto').style.display = 'none';
        })
        .catch(error => console.error('Erro:', error));
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const formVendas = document.querySelector('.addvendaform');
    
    formVendas.addEventListener('submit', function (e) {
        e.preventDefault();
        
        const formData = new FormData(formVendas);
        
        const data = {
            produto: formData.get('produto'),
            data: formData.get('data'),
            quantidade: formData.get('quantidade'),
            valor_uni: formData.get('valor_uni'),
            valor_total: formData.get('valor_total')
        };
        
        fetch(formVendas.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(venda => {
            formVendas.reset();
            document.getElementById('modal_venda').style.display = 'none';
        })
        .catch(error => alert(error));
    });
});