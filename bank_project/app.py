<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đăng ký tài khoản</title>
</head>
<body>
    <h1>Đăng ký tài khoản</h1>
    <form id="registerForm">
        <label for="username">Tên đăng nhập:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Mật khẩu:</label>
        <input type="password" id="password" name="password" required><br>
        <label for="initialBalance">Số dư ban đầu:</label>
        <input type="number" id="initialBalance" name="initialBalance" min="0" value="0" required><br>
        <button type="submit">Đăng ký</button>
    </form>

    <script>
        document.getElementById('registerForm').addEventListener('submit', function(event) {
            event.preventDefault();

            var username = document.getElementById('username').value;
            var password = document.getElementById('password').value;
            var initialBalance = document.getElementById('initialBalance').value;

            fetch('/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                    initial_balance: parseFloat(initialBalance)
                })
            })
            .then(response => {
                if (response.ok) {
                    alert('Đăng ký tài khoản thành công.');
                } else {
                    alert('Lỗi khi đăng ký tài khoản.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>
