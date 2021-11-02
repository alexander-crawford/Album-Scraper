$('.grid').isotope({
  itemSelector: '.grid-item',
  columnWidth: '.grid-item',
  percentPosition:true,
  stamp: '.stamp',
  sortBy:'album_position',
  getSortData: {
    'album_position': '.position parseInt'
  }
});
const iso = $('.grid').data('isotope');
$('.grid').infiniteScroll({
  path: '/?page={{#}}',
  append: '.grid-item',
  outlayer: iso,
  scrollThreshold: 500,
  prefill: true
});
// TODO: rewrite double press / click function using jquery
function double(data) {
  artist_id = data.getElementsByClassName('artist_id')[0].innerText;
  album_id = data.getElementsByClassName('album_id')[0].innerText;
  row_num = data.getElementsByClassName('row_num')[0].innerText;
  var request = new XMLHttpRequest();
  request.open('GET','http://localhost:8000/?artist_id=' + artist_id + '&album_id=' + album_id + '&row_num=' + row_num);
  request.responseType = "document";
  request.onload = function () {
    if (this.status = 200) {
      iso.insert(this.responseXML.body.children)
    }
  }
  request.send();
};
// TODO: rewrite single click / press function using jquery
function single(data) {
  let text_container = data.getElementsByClassName('text-container--off')[0];
  let image = data.getElementsByTagName('img')[0];
  function off() {
    text_container.classList.remove('text-container--on');
    image.classList.remove('img--off');
  }
  text_container.classList.add('text-container--on');
  image.classList.add('img--off');
  setTimeout(off,2000);
};
