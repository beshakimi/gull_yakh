// start navbar script
const menuBtn = document.getElementById("menuBtn");
const closeBtn = document.getElementById("closeBtn");
const navMenu = document.getElementById("navMenu");
const bodys = document.querySelector("body");

menuBtn.addEventListener("click", () => {
  navMenu.classList.remove("hidden");
  menuBtn.classList.add("hidden");
  closeBtn.classList.remove("hidden");
});

closeBtn.addEventListener("click", () => {
  navMenu.classList.add("hidden");
  menuBtn.classList.remove("hidden");
  closeBtn.classList.add("hidden");
});


// start full screen
const fullscreenIcon = document.querySelector("#fullscreen-icon");
fullscreenIcon.addEventListener("click", () => {
  const userAgent = navigator.userAgent.toLowerCase();
  const isChrome = /chrome/.test(userAgent);

  if (isChrome) {
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen();
    } else if (document.documentElement.webkitRequestFullscreen) {
      document.documentElement.webkitRequestFullscreen();
    }
  }
});
// remove full screnn 
fullscreenIcon.addEventListener("click", () => {
  if (document.exitFullscreen) {
    document.exitFullscreen();
  } else if (document.webkitExitFullscreen) {
    document.webkitExitFullscreen();
  }
});


// start display comments scripts

// start notification script
const userIcon = document.getElementById("user-icon");
const userModel = document.getElementById("user-model");
const body = document.querySelector("body");

userIcon.addEventListener("click", () => {
  userModel.classList.toggle("hidden");
});

body.addEventListener("click", (event) => {
  if (event.target !== userIcon) {
    userModel.classList.add("hidden");
  }
});

// start profile show and hide
// const logInProfile = document.getElementById("log-in-profile");
// const logIn = document.getElementById("log-in");
// const closeProfile = document.getElementById("close-profil");

// logInProfile.addEventListener("click", () => {
//   logIn.classList.remove("hidden");
// });

// closeProfile.addEventListener("click", () => {
//   logIn.classList.add("hidden");
// });

// show delete model script
var deleteButtons = document.querySelectorAll('.deleteButton');
deleteButtons.forEach(function (button) {
  button.addEventListener('click', function () {
    var ithemId = button.id.split('_')[1];
    var deleteModel = document.getElementById('deleteModel_' + ithemId);
    deleteModel.classList.toggle('hidden');
  });
});


//validation user infrmation  for order
// form validation script for add food and add drink 
function validateForm() {
  var nameInput = document.getElementById("name");
  var emailInput = document.getElementById("email");
  var phone1Input = document.getElementById("phone1");
  var phone2Input = document.getElementById("phone2");
  var addressInput = document.getElementById("address");
  var errorElement = document.getElementById("formError");

  var namePattern = /^[a-zA-Z\u0600-\u06FF]{1}[^!@#$%^&*()+=\[\]{};':"\\|,.<>\/?]*$/;
  var phonePattern = /^93[\d]{9}$/;
  var emailPattern = /^[A-Za-z][A-Za-z0-9_.]*@[a-zA-Z]{3,}\.[a-zA-Z]{2,5}$/;


  if (nameInput.value === "" && emailInput.value === "" && imageInput.value === "" && descriptionInput.value === "") {
      errorElement.textContent = "هیچ مقداری وارد نشده است";
      errorElement.classList.remove("hidden");
      setTimeout(function () {
          errorElement.classList.add("hidden");
      }, 5000);
      return false;
  }

  if (nameInput.value === "") {
      errorElement.textContent = "نام خود را وارد نکرده اید";
      errorElement.classList.remove("hidden");
      setTimeout(function () {
          errorElement.classList.add("hidden");
      }, 5000);
      return false;
  }

  if (!namePattern.test(nameInput.value)) {
      errorElement.textContent = "نام نامعتبر است";
      errorElement.classList.remove("hidden");
      setTimeout(function () {
          errorElement.classList.add("hidden");
      }, 5000);
      return false;
  }

  if (emailInput.value === "") {
    errorElement.textContent = "ایمیل خود را وارد نکرده اید";
    errorElement.classList.remove("hidden");
    setTimeout(function () {
        errorElement.classList.add("hidden");
    }, 5000);
    return false;
}

if (!emailPattern.test(emailInput.value)) {
    errorElement.textContent = "ایمیل نامعتبر است";
    errorElement.classList.remove("hidden");
    setTimeout(function () {
        errorElement.classList.add("hidden");
    }, 5000);
    return false;
}

  if (phone1Input.value === "") {
      errorElement.textContent = "شماره تماسخ خود را وارد نکرده اید";
      errorElement.classList.remove("hidden");
      setTimeout(function () {
          errorElement.classList.add("hidden");
      }, 5000);
      return false;
  }

   

  if (!phonePattern.test(phone2Input.value)) {
      errorElement.textContent = "شماره تماس 2 نامعتبر است";
      errorElement.classList.remove("hidden");
      setTimeout(function () {
          errorElement.classList.add("hidden");
      }, 5000);
      return false;
  }


  if (addressInput.value === "") {
      errorElement.textContent = "آدرس را وارد کند. لطفاً در نوشتن آدرس خود دقت کنید";
      errorElement.classList.remove("hidden");
      setTimeout(function () {
          errorElement.classList.add("hidden");
      }, 5000);
      return false;
  }


  errorElement.classList.add("hidden");
  return true;
}

// start slider script
const slider = document.getElementById("slider");
let currentSlide = 0;

const images = slider.getElementsByTagName("img");

setInterval(() => {
  images[currentSlide].classList.add("hidden");
  currentSlide = (currentSlide + 1) % images.length;
  images[currentSlide].classList.remove("hidden");
}, 5000);

// end slider script


