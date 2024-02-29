const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data) {
  const helloTranslation = data.hello;
  $('#hello').text(helloTranslation);
});
