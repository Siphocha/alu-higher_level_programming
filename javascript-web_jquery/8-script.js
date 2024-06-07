//fetches and lists the title for all movies by using this URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    for (let index in data.results) {
        $('UL#list_movies').append('<li>' + data.results[index].title + '</li>');
    }
});