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
$('.grid-item').click(function () {
  let text_container = $(this).find('.text-container--off');
  let image = $(this).find('img');
  function off() {
    text_container.removeClass('text-container--on');
    image.removeClass('img--off');
  }
  text_container.addClass('text-container--on');
  image.addClass('img--off');
  setTimeout(off,2000);
});
