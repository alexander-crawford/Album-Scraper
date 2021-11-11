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
// TODO: function is not called for albums loaded via infinite scroll
$('.grid-item').dblclick(function () {
  const url = 'http://localhost:8000/'
  let artist_id = $(this).find('.artist_id').text();
  let album_id = $(this).find('.album_id').text();
  let position = $(this).find('.position').text();
  $.ajax({
    url : url,
    data : {
      artist_id : artist_id,
      album_id : album_id,
      position : position
    },
    success : function (data) {
      console.log(data);
      // TODO: add albums to isotope layout
      // iso.insert()
    }
  });
});
function single(data) {
  let text_container = $(data).find('.text-container--off');
  let image = $(data).find('img');
  function off() {
    text_container.removeClass('text-container--on');
    image.removeClass('img--off');
  }
  text_container.addClass('text-container--on');
  image.addClass('img--off');
  setTimeout(off,2000);
};
