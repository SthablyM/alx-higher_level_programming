const $header = $('header');
const $divHeader = $('DIV#red_header');

$divHeader.on('click', function () {
  $header.css('#FF0000');
});
