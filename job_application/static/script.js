
document.addEventListener("DOMContentLoaded", function () {
  const menuBtn = document.getElementById("mobile-menu-btn");
  const menu = document.getElementById("navbar-menu");

  menuBtn.addEventListener("click", function () {
    menuBtn.classList.toggle("active");  
    menu.classList.toggle("active");     
  });
})