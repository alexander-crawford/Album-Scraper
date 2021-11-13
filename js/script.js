const Grid =  $('.grid');
Grid.isotope({
  itemSelector: '.grid-item',
  columnWidth: '.grid-item',
  percentPosition:true,
  stamp: '.stamp',
  sortBy:'album_position',
  getSortData: {
    'album_position': '.position parseInt'
  }
});
const Iso = Grid.data('isotope');
Grid.infiniteScroll({
  path: '/?page={{#}}',
  append: '.grid-item',
  outlayer: Iso,
  scrollThreshold: 500,
  prefill: true
});
Grid.on('append.infiniteScroll',function() {
  Grid.isotope();
});
function double(data) {
  const url = 'http://localhost:8000/'
  let artist_id = $(data).find('.artist_id').text();
  let album_id = $(data).find('.album_id').text();
  let position = $(data).find('.position').text();
  $.ajax({
    url : url,
    data : {
      artist_id : artist_id,
      album_id : album_id,
      position : position
    },
    success : function (data) {
      iso.insert($(data).siblings())
    }
  });
};
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
