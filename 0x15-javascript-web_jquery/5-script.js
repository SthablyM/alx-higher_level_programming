const $list = $('UL.my_list');
const $items = $('DIV#add_item');

$items.on('click', () => {
  $list.append('<li>Item</li>');
});
