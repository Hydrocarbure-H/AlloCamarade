document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const usernameField = document.getElementById('username');
        const passwordField = document.getElementById('password');

        const username = usernameField.value;
        const password = passwordField.value;

        const requestData = {
            username: username,
            password: password
        };

        fetch('http://127.0.0.1:5000/user/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.response === "OK") {
                    // Store the token in local storage
                    localStorage.setItem('token', data.content);
                } else {
                    errorMessage.innerText = 'Login failed. Please check your credentials.';
                    errorMessage.style.color = 'red';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                errorMessage.innerText = 'An error occurred. Please try again later.';
                errorMessage.style.color = 'red';
            });
    });
});
