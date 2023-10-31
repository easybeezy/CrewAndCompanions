// variables //
let navHamburgerBtn = document.getElementById("mobile-nav-btn");
let nav = document.getElementById("header-nav");

// functions //
function toggleMobileNav() {
    nav.classList.toggle("visible");
}

// listeners //
navHamburgerBtn.addEventListener("click", toggleMobileNav);