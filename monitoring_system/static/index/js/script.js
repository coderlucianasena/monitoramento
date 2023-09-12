function updateMeters() {
    fetch('/dados')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
            } else {
                document.getElementById('cpuMeter').getElementsByClassName('value')[0].textContent = `Uso da CPU: ${data.cpu}%`;
                document.getElementById('diskMeter').getElementsByClassName('value')[0].textContent = `Uso do Disco: ${data.disk}%`;
                document.getElementById('memoryMeter').getElementsByClassName('value')[0].textContent = `Uso da Memória: ${data.memory}%`;
                document.getElementById('output').textContent = data.output;
            }
        });
}

setInterval(updateMeters, 1000);