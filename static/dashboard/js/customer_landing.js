

var currentImage = 0;
  var images = document.querySelectorAll('.banner img');
  var touchStartX = 0;
  var touchEndX = 0;
  
  document.querySelector('.banner').addEventListener('touchstart', function(event) {
    touchStartX = event.touches[0].clientX;
  });
  
  document.querySelector('.banner').addEventListener('touchend', function(event) {
    touchEndX = event.changedTouches[0].clientX;
    handleSwipe();
  });
  
  function handleSwipe() {
    var swipeThreshold = 100; // Adjust the threshold as needed
    
    if (touchEndX < touchStartX - swipeThreshold) {
      showNextImage();
    } else if (touchEndX > touchStartX + swipeThreshold) {
      showPreviousImage();
    }
  }
  
  function showPreviousImage() {
    images[currentImage].classList.remove('active');
    currentImage = (currentImage === 0) ? images.length - 1 : currentImage - 1;
    images[currentImage].classList.add('active');
  }
  
  function showNextImage() {
    images[currentImage].classList.remove('active');
    currentImage = (currentImage === images.length - 1) ? 0 : currentImage + 1;
    images[currentImage].classList.add('active');
  }
  
  function changeImageAutomatically() {
    images[currentImage].classList.remove('active');
    currentImage = (currentImage === images.length - 1) ? 0 : currentImage + 1;
    images[currentImage].classList.add('active');
  }
  
var autoChangeInterval = setInterval(changeImageAutomatically, 5000);
  

// function changeTitle() {
//   var title = document.title;
//   if (title === "Welcome To") {
//     document.title = "Joyful Surprises";
//   } else {
//     document.title = "Welcome To";
//   }
// }

// setInterval(changeTitle, 500);





// ******** Disable right-click ****************
// window.addEventListener('contextmenu', function (e) {
//   e.preventDefault();
// }, false);


// ******** Disable long-press ***************
// window.addEventListener('touchstart', function (e) {
//   if (e.touches.length > 1) {
//     e.preventDefault();
//   }
// }, false);
