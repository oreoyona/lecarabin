
(function onInit(){
  const submitBtn = document.getElementsByClassName("submitBtn");
  for (let el of submitBtn){
    el.classList.add("btn-primary")
  }
})();

const login_btn = document.getElementById("login_btn");
const login_form = document.getElementById("login-form");
const new_account_btn = document.getElementById("new-account-link");
const inscription_form = document.getElementById("inscription-form");
const login_link = document.getElementById("login-link");
const inscription_btn = document.getElementById("inscripton-btn");


new_account_btn.addEventListener("click", ()=>{
    login_form.style.display = "none";
    inscription_form.style.display = "flex";

})

login_link.addEventListener("click", ()=>{
    login_form.style.display = 'flex';
    inscription_form.style.display = 'none';
})
