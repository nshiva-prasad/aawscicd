var result = document.getElementById("location");
const Http = new XMLHttpRequest();

function getLocation() {
  // console.log("getLocation Called");
  var bdcApi = "https://api.bigdatacloud.net/data/reverse-geocode-client";

  navigator.geolocation.getCurrentPosition(
    (position) => {
      bdcApi =
        bdcApi +
        "?latitude=" +
        position.coords.latitude +
        "&longitude=" +
        position.coords.longitude +
        "&localityLanguage=en";
      getApi(bdcApi);
    },
    (err) => {
      // Handle error when geolocation permission is denied
      var defaultCity = "Joyful";
      result.innerHTML =
        "<i class='fa-sharp fa-solid fa-location-dot'></i> " + defaultCity;
    },
    {
      enableHighAccuracy: true,
      timeout: 5000,
      maximumAge: 0,
    }
  );
}

function getApi(bdcApi) {
  Http.open("GET", bdcApi);
  Http.send();
  Http.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var response = JSON.parse(this.responseText);
      var city = response.city;
      result.innerHTML =
        "<i class='fa-sharp fa-solid fa-location-dot'></i> " + city;
      // console.log(response);
    }
  };
}

// Call the getLocation function
getLocation();

// Hamburger Toggle Menu

document.addEventListener("DOMContentLoaded", function () {
  var hamburgerMenu = document.querySelector(".hamburger-menu");
  var hamburgerMenuContent = document.querySelector(".hamburger-menu-content");
  var xmarkIcon = document.querySelector(".fa-xmark");

  hamburgerMenu.addEventListener("click", function () {
    hamburgerMenuContent.style.display = "block";
  });

  xmarkIcon.addEventListener("click", function () {
    hamburgerMenuContent.style.display = "none";
  });
});

// Handling drop-down options
var hamItems = document.querySelectorAll(".ham-item");

hamItems.forEach(function (hamItem) {
  var itemName = hamItem.querySelector(".ham-item-name");
  var dropdownOptions = hamItem.querySelector(".ham-dropdown-options");
  var plusIcon = hamItem.querySelector("#plus");
  var minusIcon = hamItem.querySelector("#minus");

  minusIcon.style.display = "none"; // Hide the minus icon initially
  hamItem.classList.add("closed"); // Add the "closed" class initially

  itemName.addEventListener("click", function () {
    if (hamItem.classList.contains("closed")) {
      dropdownOptions.style.display = "block";
      plusIcon.style.display = "none";
      minusIcon.style.display = "block";
      hamItem.classList.remove("closed");
    } else {
      dropdownOptions.style.display = "none";
      plusIcon.style.display = "block";
      minusIcon.style.display = "none";
      hamItem.classList.add("closed");
    }
  });
});

// Hover Script
document.addEventListener("DOMContentLoaded", function() {
  var items = document.querySelectorAll(".item");
  var optionsContainers = document.querySelectorAll(".options-container");

  items.forEach(function(item, index) {
    item.addEventListener("mouseover", function() {
      optionsContainers[index].style.display = "block";
      optionsContainers[index].style.position = "fixed";
      optionsContainers[index].style.width = "100%";
      optionsContainers[index].style.left = "0";
      optionsContainers[index].style.top = item.getBoundingClientRect().bottom + "px";
    });

    item.addEventListener("mouseout", function() {
      optionsContainers[index].style.display = "none";
    });
  });

  // Add a scroll event listener to reposition the options container when scrolling
  window.addEventListener("scroll", function() {
    items.forEach(function(item, index) {
      if (optionsContainers[index].style.display === "block") {
        optionsContainers[index].style.top = item.getBoundingClientRect().bottom + "px";
      }
    });
  });
});


// ****** With category and product ID ****
document.addEventListener('DOMContentLoaded', function () {
  const subcategoryItems = document.querySelectorAll('.subcategory-item');

  subcategoryItems.forEach(function (item) {
      item.addEventListener('click', function () {
          const dispatcher = item.getAttribute('data-subcategory');
          navigateToCategory(dispatcher);
      });
  });

  const productItems = document.querySelectorAll('.product-item');

  productItems.forEach(function (item) {
      const productId = item.getAttribute('data-product-id');
      const buyNowButton = item.querySelector('.action-buy');

      buyNowButton.addEventListener('click', function () {
          navigateToProduct(productId);
      });
  });

  function navigateToCategory(dispatcher) {
      // Construct the URL for the subcategory page using the dispatcher value
      const url = `/category/${dispatcher}/`;

      // Navigate to the subcategory page
      window.location.href = url;
  }

  function navigateToProduct(productId) {
      // Construct the URL for the product detail page with the product ID as dispatcher
      const url = `/product/${productId}/`;

      // Navigate to the product detail page
      window.location.href = url;
  }
});