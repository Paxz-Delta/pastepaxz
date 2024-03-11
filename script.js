// script.js
async function upload() {
    const text = document.getElementById('text').value;
    const response = await fetch('https://api.example.com/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    });
    const data = await response.json();
    window.location.href = `/${data.post_id}`;
}
