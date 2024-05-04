$.ajax({
	url: "https://swapi-api.alx-tools.com/api/films/?format=json",
	method: "GET",
	success: function(response) {
		response.results.forEach(function(film) {
			$('UL#list_movies').append("<li>" + film.title + "</li>");
		});
	},
	error: function(xhr, status, error) {
		console.error(status, error);
	}
});
