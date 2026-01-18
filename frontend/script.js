function submitFeedback() {
    const name = document.getElementById("name").value;
    const message = document.getElementById("message").value;

    fetch("https://your-backend-url.onrender.com"
, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, message })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("response").innerText = data.message;
    });
}

function loadFeedback() {
    fetch("http://127.0.0.1:8000/admin/feedback")
    .then(res => res.json())
    .then(data => {
        const table = document.getElementById("feedbackTable");
        table.innerHTML = "";
        data.forEach(item => {
            table.innerHTML += `
                <tr>
                    <td>${item.name}</td>
                    <td>${item.message}</td>
                </tr>`;
        });
    });
}
