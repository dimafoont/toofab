// STICKY MENU


var headerOffset = document.querySelector('.header-container').clientHeight
var header = document.querySelector('header')
var headerContainerMain = document.querySelector('.header-container_main')
var headerContainerTop = document.querySelector('.header-container_top')
var headerLogo = document.querySelector('.logo img')
var headerMargin = document.querySelector('.block')

function scrollOffset () {
    if (window.pageYOffset > headerOffset && window.pageYOffset < headerOffset * 2 ) {
        header.style.top = '-159px';
    }
    else if (window.pageYOffset > headerOffset * 2) {
        header.style.top = '0px';
        headerMargin.style.display = 'block';
        headerLogo.style.height = '41px';
        headerLogo.style.marginTop = '10px';
        headerLogo.style.paddingTop = '0px';
        header.classList.add('sticky-active');
        headerContainerTop.style.display = 'none';
        headerContainerMain.classList.add('sticky-container');
    }
    else {
        header.style.top = '0px'
        header.classList.remove('sticky-active');
        headerContainerMain.classList.remove('sticky-container');
        headerLogo.style.height = '';
        headerLogo.style.marginTop = '';
        headerLogo.style.paddingTop = '0px';
        headerMargin.style.display = 'none';
            if (window.innerWidth > 1200) {
                headerContainerTop.style.display = 'flex';
            }
        }
}
window.addEventListener('scroll', (e) => {
    scrollOffset()
})

// OFFCANVAS SEARCH

var searchBtn = document.querySelector('.search-btn')
var offcanvas = document.querySelector('.offcanvas-search')
var offcanvasClose = document.querySelector('.offcanvas-close a')

searchBtn.addEventListener('click', () => {
    offcanvas.classList.remove('offcanvas-not-visible');

})

offcanvasClose.addEventListener('click', () => {
    offcanvas.classList.add('offcanvas-not-visible');
})

// MOBILE MENU BTN

var menuBtn = document.querySelector('.menu-btn')
var mobileMenu = document.querySelector('.mobile-menu')

menuBtn.addEventListener('click', () => {
    if (menuBtn.classList.contains('menu-btn-active')) {
        menuBtn.classList.remove('menu-btn-active');
        mobileMenu.classList.remove('mobile-menu-active');
    }
    else {
        menuBtn.classList.add('menu-btn-active')
        mobileMenu.classList.add('mobile-menu-active');
    }
})

// HOT NOW MOBILE

var hotNow = document.querySelector('.main-tags h3')
var hotNowA = document.querySelectorAll('.main-tags a')

if (hotNow) {
hotNow.addEventListener('click', () => {
    if (hotNow.classList.contains('hotnow-active')) {
        hotNow.classList.remove('hotnow-active');
        hotNowA.forEach(el => {
        el.style.display = 'none';
    })
    }else {
        hotNow.classList.add('hotnow-active');
        hotNowA.forEach(el => {
            el.style.display = 'flex';
        })
    }
})
}

