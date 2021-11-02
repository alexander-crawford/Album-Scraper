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
// imagesLoaded( grid ).on( 'progress', function() {
  // iso.layout();
// });
const iso = $('.grid').data('isotope');
$('.grid').infiniteScroll({
  path: '/?page={{#}}',
  append: '.grid-item',
  outlayer: iso,
  scrollThreshold: 500,
  prefill: true
});
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

var mouse_down;
var mouse_up;
var elapsed;

function press(data,event) {
  const date = new Date();

  function long(data) {
    const url = 'https://duckduckgo.com/?q=';
    let artist = data.getElementsByClassName('artist')[0].innerText;
    let album = data.getElementsByClassName('title')[0].innerText;
    let link = url + artist + " " + album;
    window.open(link,'_blank')
  };

  if (event.type == "mousedown") {
    mouse_down = date.getTime();
  }

  if (event.type == "mouseup") {
    mouse_up = date.getTime();
    elapsed = date.getTime() - mouse_down;
    if (elapsed >= 500) {
      long(data);
    }
  }
};
