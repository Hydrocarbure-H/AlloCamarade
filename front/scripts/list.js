document.addEventListener('DOMContentLoaded', function () {
    const filterForm = document.getElementById('filter-form');
    const locationField = document.getElementById('location');

    // Fetch and display movies
    function fetchAndDisplayMovies(location) {
        let apiUrl = 'http://127.0.0.1:5000/movies/get';

        if (location) {
            apiUrl += `?location=${location}`;
        }

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                if (data.response === 'OK') {
                    displayMovies(data.content);
                } else {
                    console.error('Error:', data.response);
                    // Handle error, display a message or redirect
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle error, display a message or redirect
            });
    }

    filterForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const location = locationField.value;
        fetchAndDisplayMovies(location);
    });

    // Function to display movies
    function displayMovies(movies) {
        const movieListContainer = document.getElementById('movie-list');
        movieListContainer.innerHTML = ''; // Clear previous content

        movies.forEach(movie => {
            const movieItem = document.createElement('div');
            movieItem.classList.add('movie-item');

            // Customize the structure based on your needs
            movieItem.innerHTML = `
                <h2>${movie[1]}</h2>
                <p>Duration: ${movie[2]} minutes</p>
                <p>Language: ${movie[3]}</p>
                <p>Director: ${movie[5]}</p>
                <p>Main Actors: ${movie[6]}</p>
                <p>Min Age: ${movie[7]}</p>
                <p>Start Date: ${movie[8]}</p>
                <p>End Date: ${movie[9]}</p>
                <p>City: ${movie[10]}</p>
            `;

            movieListContainer.appendChild(movieItem);
        });
    }
});
