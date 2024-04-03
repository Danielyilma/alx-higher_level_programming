
fetch("https://swapi-api.alx-tools.com/api/films/?format=json")
  .then((response) => response.json())
  .then((json) => {
    json['results'].forEach(element => {
        $('UL#list_movies').append("<li>" + element['title'] + "</li>")
    });
  });