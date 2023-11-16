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
                    // check if modify=true in url
                    const urlParams = new URLSearchParams(window.location.search);
                    const modify = urlParams.get('modify');
                    if (modify === 'true') {
                        displayMoviesModify(data.content);
                    }
                    else
                    {
                        displayMovies(data.content);
                    }
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

            const today = new Date();

            // If the start date < current date and current date < end date, the movie is displayed
            let date_start = new Date(movie[8]);
            let date_end = new Date(movie[9]);

            if (date_start < today && today < date_end)
            {
                movieItem.innerHTML = `
                    <h2>${movie[1]}</h2>
                    <p>Duration: ${movie[2]} minutes</p>
                    <p>Language: ${movie[3]}</p>
                    <p>Director: ${movie[5]}</p>
                    <p>Main Actors: ${movie[6]}</p>
                    <p>Min Age: ${movie[7]}</p>
                    <p>City: ${movie[10]}</p>
                `;

                movieListContainer.appendChild(movieItem);
            }
            else
            {
                movieItem.innerHTML = `
                    <h2>${movie[1]}</h2>
                    <p>Duration: ${movie[2]} minutes</p>
                    <p>Language: ${movie[3]}</p>
                    <p>Director: ${movie[5]}</p>
                    <p>Main Actors: ${movie[6]}</p>
                    <p>Min Age: ${movie[7]}</p>
                    <p>Not available</p>
                `;
                movieItem.style.color = 'grey';

                movieListContainer.appendChild(movieItem);
            }
        });
    }

    function displayMoviesModify(movies) {
        const movieListContainer = document.getElementById('movie-list');
        movieListContainer.innerHTML = ''; // Clear previous content

        movies.forEach(movie => {
            const movieItem = document.createElement('div');
            movieItem.classList.add('movie-item');

            movieItem.innerHTML = `
            <h2>${movie[1]}</h2>
            <input type="text" id="title" name="title" placeholder="Title" value="${movie[1]}">
            <input type="text" id="duration" name="duration" placeholder="Duration" value="${movie[2]}">
            <input type="text" id="language" name="language" placeholder="Language" value="${movie[3]}">
            <input type="text" id="director" name="director" placeholder="Director" value="${movie[5]}">
            <input type="text" id="main_actors" name="main_actors" placeholder="Main Actors" value="${movie[6]}">
            <input type="text" id="min_age" name="min_age" placeholder="Min Age" value="${movie[7]}">
            <input type="text" id="start_date" name="start_date" placeholder="Start Date" value="${movie[8]}">
            <input type="text" id="end_date" name="end_date" placeholder="End Date" value="${movie[9]}">
            <input type="text" id="city" name="city" placeholder="City" value="${movie[10]}">
            <button id="update" name="update" type="submit">Update</button>
            `;

            movieListContainer.appendChild(movieItem);
        });
    }
});
