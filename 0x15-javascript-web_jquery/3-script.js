const $header = $('header');
const $divHeader = $('DIV#red_header');

$divHeader.on('click', function () {
  $header.addClass('red');
});
