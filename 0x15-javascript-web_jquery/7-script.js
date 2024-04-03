
fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
  .then((response) => response.json())
  .then((json) => {
    $('DIV#character').text(json['name'])
  });