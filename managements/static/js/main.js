// start navbar script

const menuBtn = document.getElementById("menuBtn");
const closeBtn = document.getElementById("closeBtn");
const navMenu = document.getElementById("navMenu");

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

// start notification script
const notificationIcon = document.getElementById("notificationIcon");
const notificationModel = document.getElementById("notificationModel");

notificationIcon.addEventListener("click", () => {
notificationModel.classList.toggle("hidden");
});

// start delete script
const deleteBotton = document.getElementById("deleteBotton");
const deleteModel = document.getElementById("deleteModel");

deleteBotton.addEventListener("click", () => {
  deleteModel.classList.toggle("hidden");
});
