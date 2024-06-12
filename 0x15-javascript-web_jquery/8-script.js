const movieurl = ('https://swapi-api.alx-tools.com/api/films/?format=json');
const $List = $('UL#list_movies');

$.ajax({
  url: movieurl,
  dataType: 'json'
}).done((data) => {
  const movies = data.results;

  for (let m = 0; m < movies.length; m++) {
    const movietitle = movies[m].title;
    const e = `<li>${movietitle}`;
    $List.append(e);
  }
});
