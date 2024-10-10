const socket = io('http://localhost:5050');

        socket.on('connect', () => console.log(socket.id));
        const value = document.getElementById('value');
        const cupom = document.getElementById('cupom');
        const btn = document.getElementById('btn');
        const table = document.getElementById('tableData');
        const typeCard = document.getElementById('card');
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const obj = {
                pValorTransacao: value.value,
                pNumeroCupom: cupom.value, 
                pTipoCartao: typeCard.value
            }
        socket.emit('do_transaction', obj);
        })
socket.on('result_transaction', (result) => {
                console.log(result)
                const row = document.createElement('tr');
                const cel1 = document.createElement('td');
                const cel2 = document.createElement('td');
                const cel3 = document.createElement('td');
                const cel4 = document.createElement('td');
                cel1.textContent = result.control_number;
                cel2.textContent = result.cupom_number;
                cel3.textContent = result.type_card;
                cel4.textContent = result.value;
                row.appendChild(cel1);
                row.appendChild(cel2);
                row.appendChild(cel3);
                row.appendChild(cel4);
                table.appendChild(row);
})