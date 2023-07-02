const menu = document.getElementById("menu");
const search = document.getElementById("search");
const burger = document.getElementById("header-burger")

menu.addEventListener('click', ()=>{
  burger.style.transform = 'translateX(0)';
})

document.addEventListener('mouseup', (e)=>{
  if(!burger.contains(e.target)){
    burger.style.transform = 'translateX(-100vw)';
  }
})
