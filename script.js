const socket = io.connect("http://localhost:4001");

const rankingBody= document.querySelector("#table-body");

socket.on('tabel-data', (data) => {
    rankingBody.innerHTML = '';
    console.log(data);
    for(const tickerData of data) {
        const tr = document.createElement('tr');
        for(const property in tickerData) {
            const td = document.createElement('td');
            if(property!="symbol")
                td.textContent = "$"+tickerData[property];
            else
                td.textContent = tickerData[property]+"/USDT";
            tr.appendChild(td);
        }
        rankingBody.appendChild(tr);
    }
})

