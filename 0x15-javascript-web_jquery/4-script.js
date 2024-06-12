const $header = $('header');
const $divHeader = $('DIV#toggle_header');

$divHeader.on('click', () => {
  const currentClass = $header.attr('class');
  if (currentClass === 'green') {
    $header.removeClass('green').addClass('red');
  } else if (currentClass === 'red') {
    $header.removeClass('red').addClass('green');
  }
});
