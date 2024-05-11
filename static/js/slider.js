const slides = document.querySelectorAll('.slide');
const next = document.querySelector('#next');
const prev = document.querySelector('#prev');
const close = document.querySelector('#close');
const mainSlider = document.querySelector('#main-slider');
const plot = document.querySelector('#plot-btn');
const runtime = document.querySelector('#runtime');
const runtimeSearch = document.querySelector('#runtimeSearch');



const auto = true;
const intervalTime = 10000;
let slideInterval;


const nextSlide = () => {
    // Get current class
    const current = document.querySelector('.current');
    // Remove Class
    current.classList.remove('current');
    // Check for next slide
    if(current.nextElementSibling){
        // Add Current to next sibling
        current.nextElementSibling.classList.add('current');
    }else{
        // Add Current to start
        slides[0].classList.add('current');
    }
    setTimeout(()=>current.classList.remove('current'))
}

const prevSlide = () => {
    
    const current = document.querySelector('.current');
    
    current.classList.remove('current');
    if(current.previousElementSibling){
        current.previousElementSibling.classList.add('current');
    }else{
        slides[slides.length -1].classList.add('current');
    }
    setTimeout(()=>current.classList.remove('current'))
}

// Button Events
next.addEventListener('click', e => {
    nextSlide();
    if(auto){
        clearInterval(slides);
        slideInterval = setInterval(nextSlide, intervalTime);
    }
});
prev.addEventListener('click', e => {
    prevSlide();
    if(auto){
        clearInterval(slides);
        slideInterval = setInterval(nextSlide, intervalTime);
    }
});



// Auto Slide
if (auto){
    slideInterval = setInterval(nextSlide, intervalTime);
}

document.getElementById("slider").addEventListener('click', e => {
    mainSlider.style.opacity = 0;
    setTimeout(() => {
        mainSlider.style.display = 'none';
    }, 500);
    
});

close.addEventListener('click', e => {
    mainSlider.style.opacity = 0;
    setTimeout(() => {
        mainSlider.style.display = 'none';
    }, 500);
    
});

plot.addEventListener('click', e => {
    // mainSlider.classList.add('active');
    init();
    
});

document.addEventListener("DOMContentLoaded",()=>{
    // Get the current URL
    const currentURL = window.location.href;
    
    // Remove the URL parameters
    const [baseURL, params] = currentURL.split('plot?');
    
    if (currentURL.includes('plot')) {
        result = confirm("Graphs Successfully Plotted. Do you want to view Graphs?");
        
        if (result) {
            loader.style.display = 'flex';
            loader.style.opacity = 1;
        
            mainSlider.style.display = 'block';
            setTimeout(()=>{
                loader.style.opacity = 0;
                loader.style.display ='none';
                   
                mainSlider.style.opacity = 1; 
                
            }, 4000);
        } else {
            mainSlider.classList.remove('active');
        }
    }
    // Update the URL using replaceState()
    window.history.replaceState({}, document.title, baseURL);
     
})



const loader = document.querySelector('.loader');

function init(){
    loader.style.display = 'flex';
    loader.style.opacity = 1;

    mainSlider.style.display = 'block';
    setTimeout(()=>{
        loader.style.opacity = 0;
        loader.style.display ='none';
           
        mainSlider.style.opacity = 1; 
        
    }, 4000);
};


function runtimeRemove(){
    runtime.style.opacity = 0;
    setTimeout(()=>{
        runtime.style.display = 'none';
    }, 500);
}

function runtimeActive(){
    loader.style.display = 'flex';
    loader.style.opacity = 1;

    runtime.style.display = 'flex';
    setTimeout(()=>{
        loader.style.opacity = 0;
        loader.style.display ='none';
        
        runtime.style.opacity = 1;    
        
    }, 2000);
    
}

function runtimeActiveSearch(){
    loader.style.display = 'flex';
    loader.style.opacity = 1;

    runtimeSearch.style.display = 'flex';
    setTimeout(()=>{
        loader.style.opacity = 0;
        loader.style.display ='none';

        runtimeSearch.style.opacity = 1;  
        
    }, 2000);

}


function runtimeSearchRemove(){
    runtimeSearch.style.opacity = 0;
    setTimeout(() => {
        runtimeSearch.style.display = 'none';
    }, 500);
}
