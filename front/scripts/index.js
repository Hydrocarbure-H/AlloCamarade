document.addEventListener('DOMContentLoaded', function () {
    // Check if the user is already logged in
    const token = localStorage.getItem('token');
    if (token !== null)
    {
        // Redirect to the home page
        window.location.href = 'choose.html';
    }
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
            .then(data =>
            {
                console.log(data);
                if (data.response === "OK")
                {
                    if (data.content !== "Incorrect username or password.")
                    {
                        // Store the token in local storage
                        localStorage.setItem('token', data.content);
                        // Redirect to the home page
                        window.location.href = 'choose.html';
                    }
                    else
                    {
                        errorMessage.innerText = 'Login failed. Please check your credentials.';
                        errorMessage.style.color = 'red';
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
                errorMessage.innerText = 'An error occurred. Please try again later.';
                errorMessage.style.color = 'red';
            });
    });
});
