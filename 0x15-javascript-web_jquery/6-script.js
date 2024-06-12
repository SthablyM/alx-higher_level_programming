const $header = $('header');
const $newheader = $('DIV#update_header');

$newheader.on('click', () => {
  $header.text('New Header!!!');
});
