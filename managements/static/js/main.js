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



// error message script
setTimeout(function () {
  var errorMessage = document.querySelector('.success-message');
  if (errorMessage) {
      errorMessage.classList.add('hidden');
  }
}, 5000);

// show delete model script 
var deleteButtons = document.querySelectorAll('.deleteButton');
deleteButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        var ithemId = button.id.split('_')[1];
        var deleteModel = document.getElementById('deleteModel_' + ithemId);
        deleteModel.classList.toggle('hidden');
    });
});

// form validation script for add food and add drink 
function validateForm() {
    var nameInput = document.getElementById("name");
    var priceInput = document.getElementById("price");
    var imageInput = document.getElementById("chose-image");
    var descriptionInput = document.getElementById("description");
    var errorElement = document.getElementById("formError");

    var namePattern = /^[a-zA-Z\u0600-\u06FF]{1}[^!@#$%^&*()+=\[\]{};':"\\|,.<>\/?]*$/;
    var imagePattern = /\.(jpg|jpeg|png|gif|svg|webp)$/i;
    var pricePattern = /^(?!0)\d+$/;

    if (nameInput.value === "" && priceInput.value === "" && imageInput.value === "" && descriptionInput.value === "") {
        errorElement.textContent = "هیچ مقداری وارد نشده است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (nameInput.value === "") {
        errorElement.textContent = "نام را وارد نکرده اید";
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

    if (priceInput.value === "") {
        errorElement.textContent = "قیمت را وارد نکرده اید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (!pricePattern.test(priceInput.value)) {
        errorElement.textContent = "قیمت نامعتبر است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (imageInput.value === "") {
        errorElement.textContent = "عکس را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }
  
    if (!imagePattern.test(imageInput.value)) {
        errorElement.textContent = "فرمت عکس نامعتبر است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (descriptionInput.value === "") {
        errorElement.textContent = "توضیحات را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }


    errorElement.classList.add("hidden");
    return true;
}

// form validation script adit food and edit drink 
function update_validateForm() {
    var nameInput = document.getElementById("name");
    var priceInput = document.getElementById("price");
    var imageInput = document.getElementById("chose-image");
    var descriptionInput = document.getElementById("description");
    var errorElement = document.getElementById("formError");

    var namePattern = /^[a-zA-Z\u0600-\u06FF]{1}[^!@#$%^&*()+=\[\]{};':"\\|,.<>\/?]*$/;
    var imagePattern = /\.(jpg|jpeg|png|gif|svg|webp)$/i;
    var pricePattern = /^(?!0)\d+$/;

    if (nameInput.value === "" && priceInput.value === "" && imageInput.value === "" && descriptionInput.value === "") {
        errorElement.textContent = "هیچ مقداری وارد نشده است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (nameInput.value === "") {
        errorElement.textContent = "نام را وارد کنید";
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

    if (priceInput.value === "") {
        errorElement.textContent = "قیمت را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (!pricePattern.test(priceInput.value)) {
        errorElement.textContent = "قیمت نامعتبر است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }


    if (imageInput.value !== "") {
        if (!imagePattern.test(imageInput.value)) {
            errorElement.textContent = "فرمت عکس نامعتبر است";
            errorElement.classList.remove("hidden");
            setTimeout(function () {
                errorElement.classList.add("hidden");
            }, 5000);
            return false;
        }
    }

  if (descriptionInput.value === "") {
        errorElement.textContent = "توضیحات را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }
  

    errorElement.classList.add("hidden");
    return true;
}

// form validation script for add posts 
function post_validateForm() {
    var nameInput = document.getElementById("name");
    var imageInput = document.getElementById("chose-image");
    var descriptionInput = document.getElementById("description");
    var errorElement = document.getElementById("formError");

    var namePattern = /^[a-zA-Z\u0600-\u06FF]{1}[^!@#$%^&*()+=\[\]{};':"\\|,.<>\/?]*$/;
    var imagePattern = /\.(jpg|jpeg|png|gif|svg|webp)$/i;
    

    if (nameInput.value === "" && imageInput.value === "" && descriptionInput.value === "") {
        errorElement.textContent = "هیچ مقداری وارد نشده است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (nameInput.value === "") {
        errorElement.textContent = "عنوان را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (!namePattern.test(nameInput.value)) {
        errorElement.textContent = "عنوان نامعتبر است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (imageInput.value === "") {
        errorElement.textContent = "عکس را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }
  
    if (!imagePattern.test(imageInput.value)) {
        errorElement.textContent = "فرمت عکس نامعتبر است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }
    
  if (descriptionInput.value === "") {
        errorElement.textContent = "توضیحات را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }
  

    errorElement.classList.add("hidden");
    return true;
}

// form validation script for update posts 
function post_update_validateForm() {
    var nameInput = document.getElementById("name");
    var imageInput = document.getElementById("chose-image");
    var descriptionInput = document.getElementById("description");
    var errorElement = document.getElementById("formError");

    var namePattern = /^[a-zA-Z\u0600-\u06FF]{1}[^!@#$%^&*()+=\[\]{};':"\\|,.<>\/?]*$/;
    var imagePattern = /\.(jpg|jpeg|png|gif|svg|webp)$/i;
    

    if (nameInput.value === "" && imageInput.value === "" && descriptionInput.value === "") {
        errorElement.textContent = "هیچ مقداری وارد نشده است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (nameInput.value === "") {
        errorElement.textContent = "عنوان را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (!namePattern.test(nameInput.value)) {
        errorElement.textContent = "عنوان نامعتبر است";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }

    if (imageInput.value !== "") {
        if (!imagePattern.test(imageInput.value)) {
            errorElement.textContent = "فرمت عکس نامعتبر است";
            errorElement.classList.remove("hidden");
            setTimeout(function () {
                errorElement.classList.add("hidden");
            }, 5000);
            return false;
        }
    }
 
    
  if (descriptionInput.value === "") {
        errorElement.textContent = "توضیحات را وارد کنید";
        errorElement.classList.remove("hidden");
        setTimeout(function () {
            errorElement.classList.add("hidden");
        }, 5000);
        return false;
    }
  

    errorElement.classList.add("hidden");
    return true;
}