var grid = document.querySelector('.grid');
var iso = new Isotope( grid, {
  itemSelector: '.grid-item',
  columnWidth: '.grid-item',
  percentPosition:true,
  stamp: '.stamp'
});
imagesLoaded( grid ).on( 'progress', function() {
  iso.layout();
});
