var grid = document.querySelector('.grid');
var msnry = new Masonry( grid, {
  itemSelector: '.grid-item'
});
imagesLoaded( grid ).on( 'progress', function() {
  msnry.layout();
});
