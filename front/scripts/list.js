document.addEventListener('DOMContentLoaded', function () {
    const filterForm = document.getElementById('filter-form');
    const locationField = document.getElementById('location');

    fetchAndDisplayMovies("");


    // Check if the user is already logged in
    const token = localStorage.getItem('token');
    if (token !== null) {
        button = document.getElementById('login-button');
        button.innerText = 'Dashboard';
    }
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
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    filterForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const location = locationField.value;
        fetchAndDisplayMovies(location);
    });

    /**
     * Function to display movies
     * @param movies
     */
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

    /**
     * Function to display movies in modify mode
     * @param movies
     */
    function displayMoviesModify(movies) {
        const movieListContainer = document.getElementById('movie-list');
        movieListContainer.innerHTML = ''; // Clear previous content

        movies.forEach(movie => {
            const movieItem = document.createElement('div');
            movieItem.classList.add('movie-item');

            movieItem.innerHTML = `
                <h2>${movie[1]}</h2>
                <span style="display:none" data-id="${movie[0]}"></span>
                <input type="text" id="title${movie[0]}" name="title" placeholder="Title" value="${movie[1]}">
                <input type="text" id="duration${movie[0]}" name="duration" placeholder="Duration" value="${movie[2]}">
                <input type="text" id="language${movie[0]}" name="language" placeholder="Language" value="${movie[3]}">
                <input type="text" id="director${movie[0]}" name="director" placeholder="Director" value="${movie[5]}">
                <input type="text" id="main_actors${movie[0]}" name="main_actors" placeholder="Main Actors" value="${movie[6]}">
                <input type="text" id="min_age${movie[0]}" name="min_age" placeholder="Min Age" value="${movie[7]}">
                <input type="text" id="start_date${movie[0]}" name="start_date" placeholder="Start Date" value="${movie[8]}">
                <input type="text" id="end_date${movie[0]}" name="end_date" placeholder="End Date" value="${movie[9]}">
                <input type="text" id="city${movie[0]}" name="city" placeholder="City" value="${movie[10]}">
                <button id="update${movie[0]}" name="update${movie[0]}">Update</button>
                <button id="delete${movie[0]}" name="delete${movie[0]}">Delete</button>
            `;

            movieListContainer.appendChild(movieItem);

            const updateButton = document.getElementById('update' + movie[0]);
            updateButton.addEventListener('click',Update);
            updateButton.movieItem = movieItem;
            updateButton.movie = movie;

            const deleteButton = document.getElementById('delete' + movie[0]);
            deleteButton.addEventListener('click',Delete);
            deleteButton.movieItem = movieItem;
            deleteButton.movie = movie;
        });
    }
});

/**
 * Update a movie
 * @param event
 * @param m
 * @constructor
 */
function Update(event, m) {

    event.preventDefault();
    m = event.currentTarget.movie;

    const id = event.currentTarget.movieItem.querySelector('span').getAttribute('data-id');
    const title = document.getElementById('title' + id).value;
    const duration = document.getElementById('duration' + id).value;
    const language = document.getElementById('language' + id).value;
    const director = document.getElementById('director' + id).value;
    const main_actors = document.getElementById('main_actors' + id).value;
    const min_age = document.getElementById('min_age' + id).value;
    const start_date = document.getElementById('start_date' + id).value;
    const end_date = document.getElementById('end_date' + id).value;
    const city = document.getElementById('city' + id).value;

    let movie = {
        id: id,
        title: title,
        duration: duration,
        language: language,
        subtitles: 'ENG',
        director: director,
        actors: main_actors,
        min_age: min_age,
        start_date: start_date,
        end_date: end_date,
        city: city
    };

    console.log(movie);

    fetch('http://127.0.0.1:5000/movies/update', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(movie)
    })
        .then(response => response.json())
        .then(data => {
            if (data.response === 'OK') {
                // Redirect to list page
                window.location.href = 'list.html?modify=true&updated=true';
            } else {
                alert('Error1:' + data.response);
            }
        })
        .catch(error => {
                alert('Error2:' + error);
            }
        );
}

/**
 * Delete movie
 * @param event
 * @param m
 * @constructor
 */
function Delete(event, m) {

        event.preventDefault();
        m = event.currentTarget.movie;

        const id = event.currentTarget.movieItem.querySelector('span').getAttribute('data-id');

        let movie = {
            id: id
        };

        fetch('http://127.0.0.1:5000/movies/delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(movie)
        })
            .then(response => response.json())
            .then(data => {
                if (data.response === 'OK') {
                    // Redirect to list page
                    window.location.href = 'list.html?modify=true&deleted=true';
                } else {
                    alert('Error1:' + data.response);
                }
            }
            )
            .catch(error => {
                    alert('Error2:' + error);
                }
            );
}