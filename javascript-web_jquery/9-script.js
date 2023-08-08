$(document).ready(function () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.get(url, function (data) {
        const frenchHello = data.hello;
        $('DIV#hello').text(frenchHello);
    })
  });