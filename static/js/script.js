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

bodys.addEventListener("click", (event) => {
  if (event.target !== closeBtn) {
    navMenu.classList.add("hidden");
  }
});


// const menuBtn = document.getElementById("menuBtn");
// const closeBtn = document.getElementById("closeBtn");
// const navMenu = document.getElementById("navMenu");
// const bodys = document.querySelector("body");

// menuBtn.addEventListener("click", () => {
//   navMenu.classList.remove("hidden");
//   menuBtn.classList.add("hidden");
//   closeBtn.classList.remove("hidden");
// });

// closeBtn.addEventListener("click", () => {
//   navMenu.classList.add("hidden");
//   menuBtn.classList.remove("hidden");
//   closeBtn.classList.add("hidden");
// });
// // bodys.addEventListener("click", (event) => {
// //   if (event.target !== closeBtn) {
// //     navMenu.classList.add("hidden");
// //   }
// // });

// end navbar script

// end slider script

// start full screen
const fullscreenIcon = document.querySelector("#fullscreen-icon");

fullscreenIcon.addEventListener("click", () => {
  if (document.documentElement.requestFullscreen) {
    document.documentElement.requestFullscreen();
  } else if (document.documentElement.mozRequestFullScreen) {
    // Firefox
    document.documentElement.mozRequestFullScreen();
  } else if (document.documentElement.webkitRequestFullscreen) {
    // Chrome, Safari, and Opera
    document.documentElement.webkitRequestFullscreen();
  } else if (document.documentElement.msRequestFullscreen) {
    // Internet Explorer and Edge
    document.documentElement.msRequestFullscreen();
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
const logInProfile = document.getElementById("log-in-profile");
const logIn = document.getElementById("log-in");
const closeProfile = document.getElementById("close-profil");

logInProfile.addEventListener("click", () => {
  logIn.classList.remove("hidden");
});

closeProfile.addEventListener("click", () => {
  logIn.classList.add("hidden");
});
