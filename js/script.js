var grid = document.querySelector('.grid');
var iso = new Isotope( grid, {
  itemSelector: '.grid-item',
  columnWidth: '.grid-item',
  percentPosition:true,
  stamp: '.stamp',
  sortBy:'position',
  getSortData: {
    'position': '.position parseInt'
  }
});
imagesLoaded( grid ).on( 'progress', function() {
  iso.layout();
});
function onClick(data) {
  artist_id = data.children[0].innerText;
  album_position = data.children[3].children[0].innerText;
  album_id = data.children[1].innerText; 
  var request = new XMLHttpRequest();
  request.open('GET','http://localhost:8000/?position=' + album_position + '&artist_id=' + artist_id + '&album_id=' + album_id);
  request.responseType = "document";
  request.onload = function () {
    iso.insert(this.responseXML.body.children)
  }
  request.send();
};
