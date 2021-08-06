var grid = document.querySelector('.grid');
var msnry = new Masonry( grid, {
  itemSelector: '.grid-item',
  columnWidth: '.grid-item',
  percentPosition:true,
  stamp: '.stamp'
});
imagesLoaded( grid ).on( 'progress', function() {
  msnry.layout();
});
