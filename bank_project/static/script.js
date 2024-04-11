document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var initialBalance = document.getElementById('initialBalance').value;
    var role = document.getElementById('role').value;

    fetch('/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password,
            initial_balance: parseFloat(initialBalance),
            role: role
        })
    })
    .then(response => {
        if (response.ok) {
            alert('Registration successful.');
        } else {
            alert('Registration failed.');
        }
    })
    .catch(error => console.error('Error:', error));
});
