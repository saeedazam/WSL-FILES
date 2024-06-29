document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#form').onsubmit = (event) => {
        event.preventDefault();

        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').value;
        request.open('POST', '/convert');

        request.onload = () => {
            console.log(request.responseText);
           
            const data = JSON.parse(request.responseText);

           
            if (data.success) {
                const contents = `1 USD is equal to ${data.rate} ${currency}.`;
                document.querySelector('#result').innerHTML = contents;
            } else {
                document.querySelector('#result').innerHTML = 'bla blah An error occurred. Try again. ERROR CODE: 1001';
            }
        };

        const data = new FormData();
        data.append('currency', currency);

        request.send(data);
    };
});
