
fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then((response) => response.json())
  .then((json) => {
    $('DIV#hello').text(json['hello'])
  });