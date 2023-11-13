document.addEventListener('DOMContentLoaded', function () {
    const moviePostForm = document.getElementById('movie-post-form');
    const errorMessage = document.getElementById('error-message');

    moviePostForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const titleField = document.getElementById('title');
        const durationField = document.getElementById('duration');
        const languageField = document.getElementById('language');
        const subtitlesField = document.getElementById('subtitles');
        const directorField = document.getElementById('director');
        const actorsField = document.getElementById('actors');
        const minAgeField = document.getElementById('min-age');
        const startDateField = document.getElementById('start-date');
        const endDateField = document.getElementById('end-date');

        const title = titleField.value;
        const duration = durationField.value;
        const language = languageField.value;
        const subtitles = subtitlesField.value;
        const director = directorField.value;
        const actors = actorsField.value;
        const minAge = minAgeField.value;
        const startDate = startDateField.value;
        const endDate = endDateField.value;

        const requestData = {
            title: title,
            duration: duration,
            language: language,
            subtitles: subtitles,
            director: director,
            actors: actors,
            min_age: minAge,
            start_date: startDate,
            end_date: endDate,
        };

        const token = localStorage.getItem('token');

        if (!token) {
            errorMessage.innerText = 'Authorization token not found. Please log in.';
            errorMessage.style.color = 'red';
            return;
        }

        // Assuming the server expects a Bearer token in the Authorization header
        fetch('http://127.0.0.1:5000/movies/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify(requestData)
        })
            .then(response => response.json())
            .then(data => {
                if (data.response === "OK") {
                    // Movie posted successfully, you can perform additional actions
                    console.log('Movie posted successfully!');
                } else {
                    errorMessage.innerText = 'Failed to post movie. Please check the form data.';
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
